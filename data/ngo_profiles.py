# NGO profiles: operational briefs per district for NGOs working in Sindh
# Keep focused, high-signal, and localized (Urdu/Sindhi). English for NGOs by default in app.

from typing import Dict

# Minimal starter dataset; extend over time
# Keys must be Title Case district names (e.g., "Badin", "Thatta", "Sukkur")
NGO_BRIEFS_EN: Dict[str, str] = {
    "Thatta": (
        "NGO Operational Brief — Thatta:\n\n"
        "Priority areas:\n"
        "- Coastal villages (Kharo Chan, Keti Bunder) exposed to storm surge and saline intrusion.\n\n"
        "Coordination:\n"
        "- Work with PDMA Sindh, Local Government, Health and Education via UC focal points; share a one‑page 3W.\n\n"
        "Kits & logistics:\n"
        "- Preposition safe water/ORS, hygiene and basic medical kits, tarps/rope, lights/power banks; arrange boats/trucks.\n\n"
        "Vulnerable groups:\n"
        "- Fishers’ families, pregnant women, persons with disabilities and remote hamlets; prioritize contact and access.\n\n"
        "Indicators:\n"
        "- Track reach, inclusion and complaints; publish a daily 3W update."
    ),
    "Badin": (
        "NGO Operational Brief — Badin:\n\n"
        "Priority areas:\n"
        "- Coastal UCs facing urban flooding and salinity, with agriculture and water stress.\n\n"
        "Coordination:\n"
        "- Align with PDMA, Local Government, Water/Agriculture offices, Health/Rescue; name focal points.\n\n"
        "Kits & services:\n"
        "- Water filtration/ORS, chlorination and hygiene, plus shade/cooling points where needed.\n\n"
        "Risk & access:\n"
        "- Verify evacuation centres/routes and boat access; push alerts by SMS/WhatsApp.\n\n"
        "Indicators:\n"
        "- Water access, WASH quality, complaints, and standard kit coverage."
    ),
    "Sukkur": (
        "NGO Operational Brief — Sukkur:\n\n"
        "Priority areas:\n"
        "- Riverbank/kacha areas at risk of flooding and erosion.\n\n"
        "Coordination:\n"
        "- Coordinate with PDMA, District Administration, WAPDA/IRSA, Health and Roads.\n\n"
        "Kits & services:\n"
        "- Dry food, safe water, ORS/first aid, tarps/rope.\n\n"
        "Access:\n"
        "- Secure boats/trucks; confirm bridge/routes and shelter readiness.\n\n"
        "Monitoring:\n"
        "- 3W coverage, equity of reach, complaints and inclusion indicators."
    ),
}

NGO_BRIEFS_URDU: Dict[str, str] = {
    "Thatta": (
        "این جی او آپریشنل بریف — ٹھٹھہ:\n\n"
        "ترجیحی علاقے:\n"
        "- ساحلی دیہات (کھارو چھان، کیٹی بندر)؛ سمندری طغیانی/کھارا پانی۔\n\n"
        "ہم آہنگی:\n"
        "- PDMA سندھ، مقامی حکومت، صحت، تعلیم (UC فوکل پوائنٹس)؛ ایک صفحہ 3W شیئر کریں۔\n\n"
        "کٹس و لاجسٹکس:\n"
        "- صاف پانی/ORS، حفظان صحت و طبی کٹس، ترپال/رسی، لائٹس/پاور بینک؛ کشتی/ٹرک کا انتظام۔\n\n"
        "حساس گروپس:\n"
        "- ماہی گیر خاندان، حاملہ خواتین، معذور افراد، دور دراز بستیاں؛ رابطہ اور رسائی کو ترجیح دیں۔\n\n"
        "اشاریے:\n"
        "- رسائی، شمولیت اور شکایات؛ روزانہ 3W اپڈیٹ۔"
    ),
    "Badin": (
        "این جی او آپریشنل بریف (بدین):\n"
        "- ترجیحی علاقے: ساحلی UC؛ شہری سیلاب/نمکیات؛ زرعی/پانی تناؤ\n"
        "- ہم آہنگی: PDMA، لوکل گورنمنٹ، واٹر/ایگریکلچر دفاتر؛ ریسکیو/ہیلتھ\n"
        "- کٹس/سروسز: پانی فلٹریشن/ORS، کلورینیشن، ہائجین، سایہ/کولنگ پوائنٹس\n"
        "- رسک مینجمنٹ: انخلا مراکز/روٹس؛ کشتی رسائی؛ وارننگ SMS/واٹس ایپ\n"
        "- اشاریے: پانی تک رسائی، WASH معیار، شکایات، معیاری کٹس کی تقسیم"
    ),
    "Sukkur": (
        "این جی او آپریشنل بریف (سکھر):\n"
        "- ترجیحی علاقے: دریائی کنارے/کچے کے علاقے؛ سیلاب/دریائی کٹاؤ\n"
        "- ہم آہنگی: PDMA، ضلعی انتظامیہ، واپڈا/آئی آر ایس اے، صحت/روڈز\n"
        "- کٹس/سروسز: خشک خوراک، صاف پانی، ORS/فرسٹ ایڈ، ترپال/رسي\n"
        "- رسائی: کشتی/ٹرک؛ پل/روٽس کی دستیابی؛ شیلٹرز کی تصدیق\n"
        "- مانیٹرنگ: 3W، پوش/غریب تک رسائی، شکایات، شمولیت"
    ),
}

NGO_BRIEFS_SINDHI: Dict[str, str] = {
    "Thatta": (
        "اين جي او آپريشنل بريف — ٺٽو:\n"
        "ترجيحي علائقا:\n"
        "- سامونڊي ڳوٺ (کاھرو ڇاڻ، ڪيٽي بندر)؛ طوفاني ڇڙواڳ/کارو پاڻي.\n\n"
        "هم آهنگي:\n"
        "- PDMA سنڌ، مڪاني حڪومت، صحت/تعليم (UC فوڪل)؛ هڪ صفحي جو 3W شيئر ڪريو.\n\n"
        "ڪِٽس/لاجسٽڪس:\n"
        "- صاف پاڻي/ORS، هائجين/طبي ڪِٽس، ٽارپ/رسي، بتيون/پاور بئنڪ؛ ٻيڙو/ٽرڪ جو بندوبست.\n\n"
        "حساس گروپ:\n"
        "- ماهيگير خاندان، حامله، معذور، پري بستا؛ پهچ ۽ رابطي کي اوليت.\n\n"
        "اشارا:\n"
        "- رسائي، شموليت، شڪايتون؛ روزانو 3W اپڊيٽ."
    ),
    "Badin": (
        "اين جي او آپريشنل بريف (بدين):\n"
        "- ترجيحي علائقا: سامونڊي UC؛ شهري ٻوڏ/نَمڪيات؛ زراعت/پاڻي دٻاءُ\n"
        "- هم آهنگي: PDMA، لوڪل گورنمينٽ، واٽر/ايگريڪلچر آفيسون؛ ريسڪيو/هيلٿ\n"
        "- ڪِٽس/سروسز: پاڻي فلٽريشن/ORS، ڪلورينيشن، هائجين، ڇانوَ/ڪولنگ پوائنٽس\n"
        "- رسڪ: انخلا مرڪز/روٽس؛ ٻيڙي رسائي؛ خبرداري SMS/واٽس ايپ\n"
        "- اشاري: پاڻي تائين رسائي، WASH معيار، شڪايتون، معياري ڪِٽس ورڇ"
    ),
    "Sukkur": (
        "اين جي او آپريشنل بريف (سکر):\n"
        "- ترجيحي علائقا: درياهه ڪنارا/ڪچو علائقو؛ ٻوڏ/دريائي ڪٽاوَ\n"
        "- هم آهنگي: PDMA، ضلعي انتظاميا، WAPDA/IRSA، صحت/روڊز\n"
        "- ڪِٽس/سروسز: سڪي خوراڪ، صاف پاڻي، ORS/فرسٽ ايڊ، ترپال/رسي\n"
        "- رسائي: ٻيڙو/ٽرڪ؛ پل/روٽس؛ شيلٽرز جي تصديق\n"
        "- مانيٽرنگ: 3W، امير/غريب تائين رسائي، شڪايتون، شموليت"
    ),
}

# -----------------------
# Category fallback (English)
# -----------------------

_COASTAL = {
    "Thatta", "Badin", "Sujawal"
}
_RIVERINE = {
    "Sukkur", "Khairpur", "Ghotki", "Shikarpur", "Jacobabad", "Kashmore"
}
_ARID = {
    "Tharparkar", "Umerkot"
}
_URBAN = {
    "Karachi", "Karachi Central", "Karachi East", "Karachi West", "Karachi South", "Karachi Malir", "Karachi Korangi", "Hyderabad"
}
_MIXED = {
    "Dadu", "Jamshoro", "Sanghar", "Naushahro Feroze", "Matiari", "Tando Allahyar", "Tando Muhammad Khan", "Mirpurkhas", "Shaheed Benazirabad", "Nawabshah", "Larkana"
}


def _category_for_district(district_title: str) -> str:
    d = (district_title or "").strip()
    if not d:
        return "mixed"
    if d in _COASTAL:
        return "coastal"
    if d in _RIVERINE:
        return "riverine"
    if d in _ARID:
        return "arid"
    if d in _URBAN:
        return "urban"
    return "mixed"


def _fallback_brief_en(dname: str, category: str) -> str:
    if category == "coastal":
        return (
            f"NGO Operational Brief — {dname}:\n\n"
            "Priority areas:\n"
            "- Coastal UCs/hamlets exposed to storm surge and saline intrusion.\n\n"
            "Coordination:\n"
            "- PDMA, Local Government, Health; UC focal points; daily 3W.\n\n"
            "Kits & logistics:\n"
            "- Safe water/ORS, hygiene/medical kits, tarps/rope, lights/power banks; boats/trucks with fuel.\n\n"
            "Vulnerable groups:\n"
            "- Fishers’ families, pregnant women, persons with disabilities, remote hamlets.\n\n"
            "Indicators:\n"
            "- Reach, inclusion, complaints; daily situation update."
        )
    if category == "riverine":
        return (
            f"NGO Operational Brief — {dname}:\n\n"
            "Priority areas:\n"
            "- Riverbank/kacha settlements at risk of floods and erosion.\n\n"
            "Coordination:\n"
            "- PDMA, District Admin, WAPDA/IRSA, Health/Roads; set focal points and share 3W.\n\n"
            "Kits & logistics:\n"
            "- Dry food, safe water, ORS/first aid, tarps/rope; boats/trucks staged near river access.\n\n"
            "Access & protection:\n"
            "- Verify bridges/embankments and shelter readiness; prioritize vulnerable households.\n\n"
            "Monitoring:\n"
            "- 3W coverage, equity of reach, complaints and inclusion."
        )
    if category == "arid":
        return (
            f"NGO Operational Brief — {dname}:\n\n"
            "Priority areas:\n"
            "- Water‑stressed villages facing drought and heat.\n\n"
            "Coordination:\n"
            "- PDMA, Local Government, Health/Agriculture; agree alert and response triggers.\n\n"
            "Kits & services:\n"
            "- Water trucking/filters/chlorination based on tests; ORS points and heat messaging.\n\n"
            "Livelihoods & protection:\n"
            "- Fodder/feed where critical; register vulnerable households for proactive checks.\n\n"
            "Monitoring:\n"
            "- Weekly water access, WASH quality and complaints."
        )
    if category == "urban":
        return (
            f"NGO Operational Brief — {dname}:\n\n"
            "Priority risks:\n"
            "- Urban flooding, heat and water quality hotspots.\n\n"
            "Coordination:\n"
            "- PDMA, City/LG, Health, Roads; UC/ward focal points; 3W map of shelters.\n\n"
            "Kits & logistics:\n"
            "- Water/ORS, hygiene, tarps/rope, lights/power; preposition near schools/wards used as shelters.\n\n"
            "Inclusion & access:\n"
            "- Ensure accessible, well‑lit WASH and safe spaces; traffic and road diversions planned.\n\n"
            "Monitoring:\n"
            "- Daily sitrep with reach, inclusion and complaints."
        )
    # mixed
    return (
        f"NGO Operational Brief — {dname}:\n\n"
        "Priority areas:\n"
        "- Flood‑prone UCs and water‑stressed villages.\n\n"
        "Coordination:\n"
        "- PDMA, District Admin, Health/Agriculture; UC focal points; short 3W.\n\n"
        "Kits & services:\n"
        "- Safe water/ORS, hygiene and first aid kits, tarps/rope; preposition near at‑risk UCs.\n\n"
        "Access & protection:\n"
        "- Verify shelters and routes; prioritize vulnerable groups.\n\n"
        "Monitoring:\n"
        "- Reach, inclusion, complaints; daily update."
    )


def get_ngo_brief(district_title: str, lang: str = "english") -> str:
    """Return NGO brief for a district title. Defaults to English. Empty string if not found."""
    d = (district_title or "").strip()
    if not d:
        return ""
    l = lang.lower()
    if l == "sindhi":
        return NGO_BRIEFS_SINDHI.get(d, "")
    if l == "urdu":
        return NGO_BRIEFS_URDU.get(d, "")
    # English: first, try explicit briefs; else fallback by category
    explicit = NGO_BRIEFS_EN.get(d)
    if explicit:
        return explicit
    category = _category_for_district(d)
    return _fallback_brief_en(d, category) 