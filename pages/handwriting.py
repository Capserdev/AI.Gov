import os, streamlit as st
from PIL import Image
from components.cards import section_header, divider
from components.charts import risk_ring, score_bars
from utils.constants import HANDWRITING_MODEL_DIR, HANDWRITING_MODELS, HANDWRITING_WEIGHTS
from utils.session import get_risk_color, get_risk_label
from core.demo_mode import demo_handwriting_predict

def render():
    demo = not any(os.path.exists(os.path.join(HANDWRITING_MODEL_DIR,f)) for f in HANDWRITING_MODELS.values())
    section_header("Handwriting Analysis","Upload meander, spiral, and wave drawings for motor control assessment.")
    sc = "demo" if demo else "live"; dot = "var(--amber)" if demo else "var(--green)"
    st.markdown(f'<span class="nt-status-pill {sc}"><span class="pulse-dot" style="background:{dot};"></span>{"DEMO" if demo else "LIVE"} MODE</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if not demo:
        from core.handwriting_engine import load_handwriting_models, predict_single
        models = load_handwriting_models()
    results = st.session_state.get("handwriting_results", {})
    panels = [("meander","Meander Drawing","Upload a meander/zigzag pattern tracing","#4f9cf9"),("spiral","Spiral Drawing","Upload an Archimedean spiral tracing","#a78bfa"),("wave","Wave Drawing","Upload a sinusoidal wave tracing","#22c55e")]
    cols = st.columns(3)
    for col,(key,title,desc,color) in zip(cols,panels):
        with col:
            st.markdown(f'<div class="nt-card-static" style="border-left:3px solid {color};"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:{color};margin-bottom:0.35rem;">{title.upper()}</div><div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:0.75rem;">{desc}</div></div>', unsafe_allow_html=True)
            up = st.file_uploader(f"Upload {title}", type=["png","jpg","jpeg","bmp","tiff"], key=f"hw_{key}", label_visibility="collapsed")
            if up:
                img = Image.open(up); st.image(img, use_column_width=True)
                score = demo_handwriting_predict(key, up.name) if demo else (predict_single(models[key], img) if key in models else demo_handwriting_predict(key, up.name))
                results[key] = score; st.session_state["handwriting_results"] = results
                c = get_risk_color(score)
                st.markdown(f'<div style="text-align:center;padding:0.75rem 0;"><div style="font-family:var(--font-display);font-size:1.8rem;color:{c};">{int(score*100)}%</div><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);">{get_risk_label(score)}</div></div>', unsafe_allow_html=True)
    if results:
        divider(); section_header("Handwriting Ensemble","Weighted combination of all uploaded drawing analyses.")
        ens = 0.0; tw = 0.0
        for k,w in HANDWRITING_WEIGHTS.items():
            if k in results: ens += results[k]*w; tw += w
        if tw: ens = round(ens/tw, 4)
        c1,c2 = st.columns(2)
        with c1: risk_ring(ens, label="Handwriting Risk")
        with c2: st.markdown("<br>", unsafe_allow_html=True); score_bars({k:v for k,v in results.items() if k!="ensemble"},{"meander":"#4f9cf9","spiral":"#a78bfa","wave":"#22c55e"})
        st.session_state["handwriting_results"]["ensemble"] = ens
