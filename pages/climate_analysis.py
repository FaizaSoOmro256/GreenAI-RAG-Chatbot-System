"""
Climate Analysis Page

This module provides advanced climate data analysis tools including:
- Power Spectral Density (PSD) Analysis
- Climate Cycles Analysis using FFT
- Climate Anomalies Analysis
- Seasonal Decomposition Analysis
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import signal
from statsmodels.tsa.seasonal import seasonal_decompose
from utils.sensor_integration import get_district_climate_trend
from data.district_data import sindh_district_climate_info
from sensors.district_sensor_manager import DistrictSensorManager

# Add custom CSS for headers
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        padding: 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 3px solid #1E88E5;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2196F3;
        padding: 0.5rem 0;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #2196F3;
    }
    </style>
""", unsafe_allow_html=True)

def plot_psd_analysis(data, sampling_rate=1, title="Power Spectral Density Analysis"):
    """Compute and plot the Power Spectral Density of climate data."""
    try:
        # Compute PSD using Welch's method
        frequencies, psd = signal.welch(data, sampling_rate, nperseg=min(256, len(data)))
        
        # Create the plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=frequencies,
            y=psd,
            mode='lines',
            name='PSD'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Frequency (Hz)',
            yaxis_title='Power/Frequency (dB/Hz)',
            template='plotly_white'
        )
        
        return fig
    except Exception as e:
        return None

def plot_climate_cycles(data, sampling_rate=1, title="Climate Cycles Analysis"):
    """Analyze climate cycles using Fast Fourier Transform."""
    try:
        # Compute FFT
        fft = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(data), 1/sampling_rate)
        
        # Get positive frequencies and their amplitudes
        pos_freqs = freqs[1:len(freqs)//2]
        amplitudes = np.abs(fft[1:len(freqs)//2])
        
        # Create the plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=pos_freqs,
            y=amplitudes,
            mode='lines',
            name='FFT Amplitude'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Frequency (Hz)',
            yaxis_title='Amplitude',
            template='plotly_white'
        )
        
        return fig
    except Exception as e:
        return None

def plot_climate_anomalies(data, window=30, title="Climate Anomalies Analysis"):
    """Visualize climate anomalies using rolling statistics."""
    try:
        # Calculate rolling mean and standard deviation
        rolling_mean = pd.Series(data).rolling(window=window).mean()
        rolling_std = pd.Series(data).rolling(window=window).std()
        
        # Calculate anomalies (data points outside 2 standard deviations)
        upper_bound = rolling_mean + 2 * rolling_std
        lower_bound = rolling_mean - 2 * rolling_std
        
        # Create the plot
        fig = go.Figure()
        
        # Add the main data
        fig.add_trace(go.Scatter(
            y=data,
            mode='lines',
            name='Original Data'
        ))
        
        # Add the rolling mean
        fig.add_trace(go.Scatter(
            y=rolling_mean,
            mode='lines',
            name='Rolling Mean',
            line=dict(color='red')
        ))
        
        # Add the bounds
        fig.add_trace(go.Scatter(
            y=upper_bound,
            mode='lines',
            name='Upper Bound',
            line=dict(color='gray', dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            y=lower_bound,
            mode='lines',
            name='Lower Bound',
            line=dict(color='gray', dash='dash'),
            fill='tonexty'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Time',
            yaxis_title='Value',
            template='plotly_white'
        )
        
        return fig
    except Exception as e:
        return None

def plot_seasonal_decomposition(data, period=12, title="Seasonal Decomposition Analysis"):
    """Analyze and plot the seasonal decomposition of climate data."""
    try:
        # Convert data to pandas Series with datetime index
        dates = pd.date_range(start='2020-01-01', periods=len(data), freq='M')
        series = pd.Series(data, index=dates)
        
        # Perform seasonal decomposition
        decomposition = seasonal_decompose(series, model='additive', period=period)
        
        # Create subplots
        fig = go.Figure()
        
        # Add trend
        fig.add_trace(go.Scatter(
            x=dates,
            y=decomposition.trend,
            mode='lines',
            name='Trend',
            line=dict(color='blue')
        ))
        
        # Add seasonal
        fig.add_trace(go.Scatter(
            x=dates,
            y=decomposition.seasonal,
            mode='lines',
            name='Seasonal',
            line=dict(color='green')
        ))
        
        # Add residual
        fig.add_trace(go.Scatter(
            x=dates,
            y=decomposition.resid,
            mode='lines',
            name='Residual',
            line=dict(color='red')
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title='Time',
            yaxis_title='Value',
            template='plotly_white',
            height=800  # Make the plot taller to accommodate all components
        )
        
        return fig
    except Exception as e:
        return None

def show_district_info(district: str):
    """Display district information card."""
    if district not in sindh_district_climate_info:
        st.error(f"No information available for {district}")
        return
        
    info = sindh_district_climate_info[district]
    
    # Create columns for the info card
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style='background-color: #f0f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 class="section-header" style='margin-top: 0;'>{district}</h2>
            <p><strong>Region:</strong> {info['region']}</p>
            <p><strong>Area:</strong> {info['area']} km²</p>
            <p><strong>Population:</strong> {info['population']} million</p>
            <p><strong>Climate:</strong> {info['climate']}</p>
            <p><strong>Temperature Range:</strong> {info['temperature']}</p>
            <p><strong>Rainfall:</strong> {info['rainfall']}</p>
            <p><strong>Humidity:</strong> {info['humidity']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background-color: #f0f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h3 style='color: #2196F3; margin-top: 0; margin-bottom: 15px;'>Key Challenges</h3>
            <p>{info['challenges']}</p>
            <h3 style='color: #2196F3; margin-top: 15px; margin-bottom: 15px;'>Future Projection</h3>
            <p>{info['future_projection']}</p>
        </div>
        """, unsafe_allow_html=True)

def show_climate_analysis():
    """Display the climate analysis page."""
    st.markdown('<h1 class="main-header">Climate Data Analysis</h1>', unsafe_allow_html=True)
    
    # Create a container for analysis controls
    with st.container():
        st.markdown('<h2 class="section-header">Analysis Controls</h2>', unsafe_allow_html=True)
        
        # Create three columns for controls
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # District selection
            districts = sorted(list(sindh_district_climate_info.keys()))
            selected_district = st.selectbox("Select District", districts)
        
        with col2:
            # Variable selection
            variables = ["Temperature", "Humidity", "Rainfall", "Air Quality"]
            selected_variable = st.selectbox("Select Variable", variables)
        
        with col3:
            # Analysis type selection
            analysis_types = ["PSD Analysis", "Climate Cycles", "Climate Anomalies", "Seasonal Decomposition", "Air Quality Heat Map"]
            selected_analysis = st.selectbox("Select Analysis Type", analysis_types)
    
    # Display district information
    show_district_info(selected_district)
    
    # Create a container for visualization controls
    with st.container():
        st.markdown('<h2 class="section-header">Visualization Controls</h2>', unsafe_allow_html=True)
        
        # Create two columns for visualization controls
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Time range selection
            time_ranges = ["Last 30 days", "Last 90 days", "Last 180 days", "Last 365 days"]
            time_range = st.selectbox("Select Time Range", time_ranges)
            
            # Aggregation method
            aggregation_methods = ["Daily", "Weekly", "Monthly"]
            aggregation = st.selectbox("Select Aggregation Method", aggregation_methods)
        
        with viz_col2:
            # Chart type selection
            chart_types = ["Line Chart", "Bar Chart", "Area Chart"]
            selected_chart_type = st.selectbox("Select Chart Type", chart_types)
            
            # Show/hide options
            show_trend = st.checkbox("Show Trend Line", value=True)
            show_forecast = st.checkbox("Show Forecast", value=False)
    
    try:
        if selected_variable == "Air Quality" or selected_analysis == "Air Quality Heat Map":
            # Get air quality data
            sensor_manager = DistrictSensorManager()
            air_quality_sensor = sensor_manager.sensors[selected_district]['air_quality']
            
            if air_quality_sensor:
                # Get current reading
                current_reading = air_quality_sensor.read_sensor()
                if current_reading:
                    current_aqi = current_reading['aqi']
                    st.markdown('<h2 class="section-header">Air Quality Metrics</h2>', unsafe_allow_html=True)
                    st.metric("Current Air Quality Index", f"{current_aqi:.1f}")
                    
                    # Get historical AQI data
                    aqi_history = air_quality_sensor.get_aqi_history(
                        days=30 if time_range == "Last 30 days" else 7,
                        aggregation=aggregation.lower()
                    )
                    
                    if not aqi_history.empty:
                        st.markdown('<h2 class="section-header">Air Quality Heat Map</h2>', unsafe_allow_html=True)
                        # Create heat map
                        fig = go.Figure(data=go.Heatmap(
                            z=[aqi_history['aqi'].values],
                            x=aqi_history.index,
                            y=['AQI'],
                            colorscale='RdYlGn_r',  # Red for high AQI, green for low
                            zmin=0,
                            zmax=500,
                            colorbar=dict(
                                title='AQI',
                                titleside='right',
                                titlefont=dict(size=14)
                            )
                        ))
                        
                        fig.update_layout(
                            title='Air Quality Index Heat Map',
                            xaxis_title='Time',
                            yaxis_title='',
                            height=200,
                            margin=dict(l=0, r=0, t=30, b=0)
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Display additional air quality metrics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("PM2.5", f"{current_reading['pm25']:.1f} µg/m³")
                        with col2:
                            st.metric("PM10", f"{current_reading['pm10']:.1f} µg/m³")
                        with col3:
                            st.metric("CO2", f"{current_reading['co2']:.1f} ppm")
                    else:
                        st.warning("No historical air quality data available for visualization.")
                else:
                    st.warning("No current air quality data available.")
            else:
                st.warning("No air quality sensor available for the selected district.")
            return
        
        # Get climate data for other variables
        climate_data = get_district_climate_trend(selected_district)
        
        if climate_data is None or selected_variable.lower() not in climate_data:
            st.error(f"No data available for {selected_variable} in {selected_district}")
            return
        
        # Extract the data series
        data = climate_data[selected_variable.lower()]
        
        # Create the appropriate plot based on selected analysis
        st.markdown(f'<h2 class="section-header">{selected_analysis}</h2>', unsafe_allow_html=True)
        
        if selected_analysis == "PSD Analysis":
            fig = plot_psd_analysis(
                data,
                title=f"Power Spectral Density Analysis - {selected_variable} in {selected_district}"
            )
        elif selected_analysis == "Climate Cycles":
            fig = plot_climate_cycles(
                data,
                title=f"Climate Cycles Analysis - {selected_variable} in {selected_district}"
            )
        elif selected_analysis == "Climate Anomalies":
            fig = plot_climate_anomalies(
                data,
                title=f"Climate Anomalies Analysis - {selected_variable} in {selected_district}"
            )
        else:  # Seasonal Decomposition
            fig = plot_seasonal_decomposition(
                data,
                title=f"Seasonal Decomposition Analysis - {selected_variable} in {selected_district}"
            )
        
        if fig:
            st.plotly_chart(fig, use_container_width=True)
            
            # Display statistical summary
            st.markdown('<h2 class="section-header">Statistical Summary</h2>', unsafe_allow_html=True)
            stats_df = pd.DataFrame({
                'Metric': ['Mean', 'Standard Deviation', 'Minimum', 'Maximum'],
                'Value': [
                    np.mean(data),
                    np.std(data),
                    np.min(data),
                    np.max(data)
                ]
            })
            st.dataframe(stats_df)
            
            # Add download button for the data
            csv = pd.DataFrame({selected_variable: data}).to_csv(index=False)
            st.download_button(
                label="Download Data",
                data=csv,
                file_name=f"{selected_district}_{selected_variable.lower()}_data.csv",
                mime="text/csv"
            )
        else:
            st.error("Error generating the analysis plot. Please try again.")
            
    except Exception as e:
        st.error("An error occurred while analyzing the climate data. Please try again.")

if __name__ == "__main__":
    show_climate_analysis() 