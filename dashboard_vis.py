# app_greenai_metrics.py
# Streamlit dashboard to visualize multilingual RAG chatbot metrics with interactive graphs
# How to run:
#   1) pip install streamlit pandas numpy plotly scikit-learn
#   2) streamlit run app_greenai_metrics.py

import io
import base64
from dataclasses import dataclass
from typing import List, Dict

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ===============
# UI CONFIG
# ===============
st.set_page_config(
    page_title="GreenAI • RAG Metrics Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Minimal theming via custom CSS for a clean, modern look ---
st.markdown(
    """
    <style>
      .css-18ni7ap, .css-1d391kg {padding-top: 1rem;} /* reduce top padding */
      .metric-card {
        background: linear-gradient(180deg, #e8f5e9 0%, #ffffff 80%);
        border: 1px solid #dceadf;
        box-shadow: 0 8px 24px rgba(31, 76, 36, 0.08);
        border-radius: 18px;
        padding: 18px 18px 10px 18px;
      }
      .pill {display:inline-block;padding:4px 10px;border-radius:999px;background:#e8f5e9;border:1px solid #cde7d1;color:#245a2f;font-weight:600;font-size:12px}
      .small {font-size:12px;color:#4a5a4d}
      .caption {font-size:13px;color:#647b6a}
      .stMetric {background: #f8fff9;border-radius: 16px;padding:8px;border:1px solid #e3f1e5}
      .stDownloadButton button {border-radius:12px}
      .section-title {font-weight:800;font-size:20px;margin:0 0 8px 0}
      .subtle {color:#3a5a40}
      .footnote {font-size:12px;color:#6d826f}
    </style>
    """,
    unsafe_allow_html=True,
)

# ===============
# DATA MODELS
# ===============
@dataclass
class LangMetrics:
    language: str
    precision: float
    recall: float
    f1: float
    samples: int = 1000         # total test items for the language
    prevalence: float = 0.5     # proportion of positives ("correct" cases) in [0,1]

    def to_row(self):
        return {
            "Language": self.language,
            "Precision": round(self.precision, 3),
            "Recall": round(self.recall, 3),
            "F1": round(self.f1, 3),
            "Samples": self.samples,
            "Prevalence": round(self.prevalence, 3),
        }

# ===============
# HELPERS
# ===============

def derive_confusion_counts(precision: float, recall: float, samples: int, prevalence: float):
    """Compute TP, FP, FN, TN from precision/recall and assumptions on samples & prevalence.
    Values are rounded to integers and clipped to avoid negatives.
    """
    samples = max(1, int(samples))
    prevalence = float(np.clip(prevalence, 0.0001, 0.9999))
    positives = samples * prevalence
    negatives = samples - positives

    # TP and FN from recall
    tp = recall * positives
    fn = max(0.0, positives - tp)

    # FP from precision (if precision==0, avoid div-by-zero)
    if precision <= 0:
        fp = positives  # worst case fallback
    else:
        fp = tp * (1 - precision) / max(precision, 1e-9)

    tn = negatives - fp

    # Round & clip
    tp_i = int(round(tp))
    fn_i = int(round(fn))
    fp_i = int(round(max(0.0, fp)))
    tn_i = int(round(max(0.0, tn)))

    # Adjust if rounding drifts totals
    total = tp_i + fn_i + fp_i + tn_i
    if total != samples:
        diff = samples - total
        # Prefer adjusting TN first, then FP, then FN, then TP
        for key in ["tn_i", "fp_i", "fn_i", "tp_i"]:
            if diff == 0:
                break
            val = locals()[key]
            new_val = max(0, val + diff)
            diff -= (new_val - val)
            if key == "tn_i":
                tn_i = new_val
            elif key == "fp_i":
                fp_i = new_val
            elif key == "fn_i":
                fn_i = new_val
            else:
                tp_i = new_val

    return tp_i, tn_i, fp_i, fn_i


def metrics_from_confusion(tp: int, tn: int, fp: int, fn: int) -> Dict[str, float]:
    """Compute derived metrics from confusion counts."""
    eps = 1e-9
    precision = tp / (tp + fp + eps)
    recall = tp / (tp + fn + eps)
    specificity = tn / (tn + fp + eps)
    accuracy = (tp + tn) / max(tp + tn + fp + fn, 1)
    f1 = 2 * precision * recall / max(precision + recall + eps, eps)
    return {
        "Precision": precision,
        "Recall": recall,
        "Specificity": specificity,
        "Accuracy": accuracy,
        "F1": f1,
    }


def download_link(df: pd.DataFrame, filename: str, label: str):
    csv = df.to_csv(index=False).encode("utf-8")
    b64 = base64.b64encode(csv).decode()
    href = f'<a download="{filename}" href="data:text/csv;base64,{b64}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

# ===============
# DEFAULT DATA
# ===============
def default_rows() -> List[LangMetrics]:
    return [
        LangMetrics("English", 0.90, 0.88, 0.89, samples=1000, prevalence=0.5),
        LangMetrics("Urdu",    0.87, 0.85, 0.86, samples=1000, prevalence=0.5),
        LangMetrics("Sindhi",  0.84, 0.82, 0.83, samples=1000, prevalence=0.5),
    ]

# ===============
# SIDEBAR – DATA ENTRY / UPLOAD
# ===============
st.sidebar.markdown("<span class='pill'>GreenAI · RAG Metrics</span>", unsafe_allow_html=True)
st.sidebar.header("Data Source")

with st.sidebar.expander("Upload CSV (optional)", expanded=False):
    st.write("Provide a CSV with columns: Language, Precision, Recall, F1, Samples, Prevalence")
    uploaded = st.file_uploader("Choose a CSV", type=["csv"])

if uploaded is not None:
    df_src = pd.read_csv(uploaded)
    # Basic cleanup
    expected = ["Language", "Precision", "Recall", "F1", "Samples", "Prevalence"]
    missing = [c for c in expected if c not in df_src.columns]
    if missing:
        st.error(f"CSV missing columns: {missing}")
        st.stop()
else:
    df_src = pd.DataFrame([m.to_row() for m in default_rows()])

# Manual overrides
st.sidebar.header("Assumptions & Overrides")
col_a, col_b = st.sidebar.columns(2)
rounding = col_a.checkbox("Round labels to 2 decimals", True)
show_values = col_b.checkbox("Show values on bars", True)

st.sidebar.caption("Prevalence is the proportion of positive cases (e.g., 'correct' responses) in your test set.")

# Per-language controls
st.sidebar.subheader("Per-Language Settings")
for idx in range(len(df_src)):
    with st.sidebar.expander(f"{df_src.at[idx, 'Language']} settings", expanded=False):
        df_src.at[idx, "Samples"] = st.number_input(
            f"Samples · {df_src.at[idx, 'Language']}", min_value=1, step=10, value=int(df_src.at[idx, "Samples"])
        )
        df_src.at[idx, "Prevalence"] = st.slider(
            f"Prevalence (positives) · {df_src.at[idx, 'Language']}", 0.0, 1.0, float(df_src.at[idx, "Prevalence"]), 0.01
        )

# ===============
# HEADER
# ===============
left, right = st.columns([0.7, 0.3])
with left:
    st.markdown("<div class='section-title'>🌿 GreenAI — Multilingual RAG Performance Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtle'>Track and compare Precision, Recall, F1, and confusion metrics across languages. Upload your own results or use the defaults to start.</div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='pill' style='float:right;'>Live · Interactive</div>", unsafe_allow_html=True)

st.divider()

# ===============
# TOP METRICS: GROUPED BAR (Precision/Recall/F1)
# ===============
long = df_src.melt(id_vars=["Language", "Samples", "Prevalence"], value_vars=["Precision", "Recall", "F1"],
                   var_name="Metric", value_name="Score")

fig_bars = px.bar(
    long, x="Language", y="Score", color="Metric", barmode="group",
    title="Precision · Recall · F1 by Language",
    hover_data=["Samples", "Prevalence"],
)
fig_bars.update_layout(
    yaxis=dict(range=[0, 1.0], tickformat=".2f"),
    legend_title_text="Metric",
    margin=dict(l=10, r=10, t=60, b=10),
)
if show_values:
    fig_bars.update_traces(texttemplate="%{y:.2f}" if rounding else "%{y}", textposition="outside", cliponaxis=False)

st.plotly_chart(fig_bars, use_container_width=True)

# ===============
# CONFUSION MATRICES (derived)
# ===============
cm_tabs = st.tabs([f"{lang}" for lang in df_src["Language"].tolist()])

all_rows = []

for i, tab in enumerate(cm_tabs):
    with tab:
        row = df_src.iloc[i]
        lang = row["Language"]
        tp, tn, fp, fn = derive_confusion_counts(row["Precision"], row["Recall"], int(row["Samples"]), float(row["Prevalence"]))

        cm = np.array([[tp, fn], [fp, tn]])
        # Order: [[TP, FN], [FP, TN]] for display clarity

        derived = metrics_from_confusion(tp, tn, fp, fn)
        summary_df = pd.DataFrame({
            "Metric": ["Precision", "Recall", "Specificity", "Accuracy", "F1"],
            "Value": [derived[m] for m in ["Precision", "Recall", "Specificity", "Accuracy", "F1"]],
        })

        st.markdown(f"### {lang} — Confusion Metrics")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Precision", f"{derived['Precision']:.2f}")
        kpi2.metric("Recall", f"{derived['Recall']:.2f}")
        kpi3.metric("Accuracy", f"{derived['Accuracy']:.2f}")
        kpi4.metric("F1", f"{derived['F1']:.2f}")

        # Heatmap figure
        heat = go.Figure(data=go.Heatmap(
            z=cm,
            x=["Pred: Positive", "Pred: Negative"],
            y=["Actual: Positive", "Actual: Negative"],
            zmin=0,
            colorscale="Greens",
            hoverongaps=False,
            text=cm,
            texttemplate="%{text}",
        ))
        heat.update_layout(title=f"{lang} — Confusion Matrix (derived)", margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(heat, use_container_width=True)

        # Show raw counts
        counts_df = pd.DataFrame({
            "": ["TP", "TN", "FP", "FN"],
            "Count": [tp, tn, fp, fn]
        })
        st.dataframe(counts_df, use_container_width=True, hide_index=True)

        all_rows.append({
            "Language": lang,
            "TP": tp,
            "TN": tn,
            "FP": fp,
            "FN": fn,
            **{k: round(v, 4) for k, v in derived.items()},
            "Samples": int(row["Samples"]),
            "Prevalence": float(row["Prevalence"]),
        })

# ===============
# COMPARISON: ACCURACY / SPECIFICITY
# ===============
comp_df = pd.DataFrame(all_rows)

col1, col2 = st.columns(2)
with col1:
    fig_acc = px.bar(comp_df, x="Language", y="Accuracy", title="Accuracy by Language")
    fig_acc.update_layout(yaxis=dict(range=[0, 1.0], tickformat=".2f"), margin=dict(l=10, r=10, t=60, b=10))
    if show_values:
        fig_acc.update_traces(texttemplate="%{y:.2f}" if rounding else "%{y}", textposition="outside")
    st.plotly_chart(fig_acc, use_container_width=True)

with col2:
    fig_spec = px.bar(comp_df, x="Language", y="Specificity", title="Specificity by Language")
    fig_spec.update_layout(yaxis=dict(range=[0, 1.0], tickformat=".2f"), margin=dict(l=10, r=10, t=60, b=10))
    if show_values:
        fig_spec.update_traces(texttemplate="%{y:.2f}" if rounding else "%{y}", textposition="outside")
    st.plotly_chart(fig_spec, use_container_width=True)

st.divider()

# ===============
# RAG-SPECIFIC INSIGHTS (Optional Section)
# ===============
st.markdown("<div class='section-title'>📌 RAG-Specific Diagnostics</div>", unsafe_allow_html=True)
st.caption("Optional: Track retrieval and generation quality indicators for your GreenAI system.")

c1, c2, c3 = st.columns(3)
with c1:
    p_at_k = st.slider("Precision@K (retrieval)", 0.0, 1.0, 0.72, 0.01)
    cov = st.slider("Context Coverage (0–1)", 0.0, 1.0, 0.81, 0.01)
with c2:
    faith = st.slider("Faithfulness (no hallucination)", 0.0, 1.0, 0.86, 0.01)
    ans = st.slider("Answer Usefulness", 0.0, 1.0, 0.83, 0.01)
with c3:
    lat = st.slider("Avg. Latency (s)", 0.2, 10.0, 2.3, 0.1)
    ctoks = st.slider("Avg. Context Tokens", 64, 4000, 850, 16)

rag_df = pd.DataFrame({
    "Metric": ["Precision@K", "Coverage", "Faithfulness", "Usefulness"],
    "Score": [p_at_k, cov, faith, ans],
})
fig_rag = px.bar(rag_df, x="Metric", y="Score", title="RAG Retrieval/Generation Quality")
fig_rag.update_layout(yaxis=dict(range=[0, 1.0], tickformat=".2f"), margin=dict(l=10, r=10, t=60, b=10))
st.plotly_chart(fig_rag, use_container_width=True)

# Latency distribution mock (adjustable by user via avg latency)
np.random.seed(7)
latencies = np.clip(np.random.lognormal(mean=np.log(lat), sigma=0.35, size=500), 0, 20)
fig_lat = px.histogram(x=latencies, nbins=30, marginal="box", title="Response Latency Distribution (simulated)")
fig_lat.update_layout(margin=dict(l=10, r=10, t=60, b=10), xaxis_title="Latency (s)", yaxis_title="Count")
st.plotly_chart(fig_lat, use_container_width=True)

st.caption("You can replace simulated latency with your real logs by uploading a CSV of response times and plotting similarly.")

# ===============
# EXPORT
# ===============
st.divider()
st.subheader("Export Results")
st.dataframe(comp_df, use_container_width=True)

c_exp1, c_exp2 = st.columns([0.25, 0.75])
with c_exp1:
    csv_bytes = comp_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Metrics CSV", data=csv_bytes, file_name="greenai_confusion_metrics.csv", mime="text/csv")
with c_exp2:
    st.markdown("<span class='footnote'>Tip: Use the CSV export in your report appendix and embed screenshots of the charts above in your Discussion section.</span>", unsafe_allow_html=True)

st.markdown("""
---
<div class='caption'>Developed for GreenAI · Multilingual RAG Chatbot — Streamlit dashboard template.</div>
""", unsafe_allow_html=True)
