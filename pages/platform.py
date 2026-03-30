import os, streamlit as st
from components.cards import section_header, divider
from utils.constants import HANDWRITING_MODEL_DIR, VOICE_MODEL_DIR, HANDWRITING_MODELS, VOICE_MODELS

def render():
    section_header("Platform","Technical architecture, model status, and system information.")
    arch = [("Frontend","Streamlit","Python-native web framework with reactive data flow and custom CSS."),("Vision Models","TensorFlow / Keras","EfficientNetV2B0 pretrained on ImageNet, fine-tuned on HandPD dataset with 4x TTA."),("Voice Models","scikit-learn / joblib","SVC pipelines trained on acoustic features from PC-GITA dataset."),("Feature Extraction","librosa","36 acoustic features: 13 MFCC mean/std, jitter, shimmer, HNR, ZCR, spectral."),("Ensemble","Custom","Weighted averaging: handwriting (40%), voice (35%), survey (25%)."),("Deployment","Local / Streamlit Cloud","Runs locally or deploys to Streamlit Cloud. Demo mode without models.")]
    for i in range(0,len(arch),3):
        cols = st.columns(3)
        for j,col in enumerate(cols):
            if i+j<len(arch):
                nm,tc,dc = arch[i+j]
                with col: st.markdown(f'<div class="nt-card" style="height:100%;"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.35rem;">{nm}</div><div style="font-family:var(--font-display);font-size:1rem;color:var(--text);margin-bottom:0.5rem;">{tc}</div><div style="font-size:0.8rem;color:var(--text-secondary);line-height:1.55;">{dc}</div></div>', unsafe_allow_html=True)
    divider()
    st.markdown('<div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);margin-bottom:1rem;">MODEL STATUS</div>', unsafe_allow_html=True)
    hw_cols = st.columns(3)
    for col,(nm,key) in zip(hw_cols,[("Meander","meander"),("Spiral","spiral"),("Wave","wave")]):
        with col:
            fname=HANDWRITING_MODELS[key]; path=os.path.join(HANDWRITING_MODEL_DIR,fname); live=os.path.exists(path)
            sc="live" if live else "demo"; dot="var(--green)" if live else "var(--amber)"; st_text="LOADED" if live else "NOT FOUND"
            st.markdown(f'<div class="nt-card-static" style="margin-bottom:0.75rem;"><div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:0.85rem;color:var(--text);">{nm}</span><span class="nt-status-pill {sc}"><span class="pulse-dot" style="background:{dot};"></span>{st_text}</span></div><div style="font-family:var(--font-mono);font-size:0.6rem;color:var(--text-muted);margin-top:0.35rem;">{fname}</div></div>', unsafe_allow_html=True)
    v_cols = st.columns(4)
    for col,(nm,key) in zip(v_cols,[("Ahh","ahh"),("Vowels","vowels"),("Text","text"),("4-Class","fourclass")]):
        with col:
            fname=VOICE_MODELS[key]; path=os.path.join(VOICE_MODEL_DIR,fname); live=os.path.exists(path)
            sc="live" if live else "demo"; dot="var(--green)" if live else "var(--amber)"; st_text="LOADED" if live else "NOT FOUND"
            st.markdown(f'<div class="nt-card-static" style="margin-bottom:0.75rem;"><div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:0.85rem;color:var(--text);">{nm}</span><span class="nt-status-pill {sc}"><span class="pulse-dot" style="background:{dot};"></span>{st_text}</span></div><div style="font-family:var(--font-mono);font-size:0.6rem;color:var(--text-muted);margin-top:0.35rem;">{fname}</div></div>', unsafe_allow_html=True)
    divider()
    st.markdown('<div class="nt-card-static" style="border-left:3px solid var(--amber);"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--amber);margin-bottom:0.5rem;">MEDICAL DISCLAIMER</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.6;">NeuroTrace is a research tool for NC HOSA Medical Innovations. It is <strong>not</strong> a certified medical device and has not been approved by the FDA. Always consult a qualified healthcare provider.</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;margin-top:2rem;"><div style="font-family:var(--font-mono);font-size:0.55rem;letter-spacing:0.1em;color:var(--text-muted);">NEUROTRACE v1.0 &middot; NC HOSA 2026 &middot; MEDICAL INNOVATIONS</div></div>', unsafe_allow_html=True)
