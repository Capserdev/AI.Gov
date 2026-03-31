import os, streamlit as st
from components.cards import stat_card, model_card, section_header, divider
from utils.session import navigate_to
from utils.constants import HANDWRITING_MODEL_DIR, VOICE_MODEL_DIR, HANDWRITING_MODELS, VOICE_MODELS

def render():
    # Hero
    st.markdown("""
    <div class="nt-hero">
        <div style="margin-bottom:2rem;">
            <div class="nt-pill"><span class="nt-pill-dot"></span>AI Presidential Challenge 2026</div>
        </div>
        <h1>Parkinson's screening<br>through <span>digital biomarkers</span></h1>
        <p>NeuroTrace combines handwriting analysis, vocal biomarkers, and lifestyle assessment
        into a unified, non-invasive screening tool powered by deep learning.</p>
    </div>
    """, unsafe_allow_html=True)

    b1, b2, _ = st.columns([1, 1, 4])
    with b1:
        if st.button("Start Screening", key="hero_start"):
            navigate_to("handwriting"); st.rerun()
    with b2:
        if st.button("Learn More", key="hero_learn"):
            navigate_to("science"); st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    divider()

    # Stats
    c1, c2, c3, c4 = st.columns(4)
    with c1: stat_card("10M+", "People affected globally")
    with c2: stat_card("7", "ML models")
    with c3: stat_card("3", "Diagnostic modalities")
    with c4: stat_card("89%", "Avg model accuracy")

    divider()
    section_header("How it works", "Three complementary modalities for comprehensive screening.")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="nt-card-plain">
            <div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-dim);margin-bottom:0.75rem;">01 — Handwriting</div>
            <div style="font-family:var(--font-serif);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Drawing Analysis</div>
            <div style="font-size:0.82rem;color:var(--text-muted);line-height:1.65;">EfficientNetV2B0 models detect micrographia and tremor patterns in meander, spiral, and wave drawings.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="nt-card-plain">
            <div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-dim);margin-bottom:0.75rem;">02 — Voice</div>
            <div style="font-family:var(--font-serif);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Vocal Biomarkers</div>
            <div style="font-size:0.82rem;color:var(--text-muted);line-height:1.65;">SVC models analyze jitter, shimmer, and MFCC features from sustained vowels and connected speech.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="nt-card-plain">
            <div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-dim);margin-bottom:0.75rem;">03 — Survey</div>
            <div style="font-family:var(--font-serif);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Lifestyle Assessment</div>
            <div style="font-size:0.82rem;color:var(--text-muted);line-height:1.65;">Clinically-validated questionnaire assessing motor symptoms, non-motor indicators, and risk factors.</div>
        </div>
        """, unsafe_allow_html=True)

    divider()
    section_header("Models", "Seven specialized models across two diagnostic modalities.")

    c1, c2, c3 = st.columns(3)
    for col, (name, mt, desc, key) in zip([c1, c2, c3], [
        ("Meander Model", "VISION", "EfficientNetV2B0 fine-tuned on meander drawing patterns to detect tremor irregularities.", "meander"),
        ("Spiral Model",  "VISION", "EfficientNetV2B0 fine-tuned on Archimedean spiral drawings for tremor amplitude analysis.", "spiral"),
        ("Wave Model",    "VISION", "EfficientNetV2B0 fine-tuned on sinusoidal wave tracings for motor control assessment.", "wave"),
    ]):
        with col:
            model_card(name, mt, desc, os.path.exists(os.path.join(HANDWRITING_MODEL_DIR, HANDWRITING_MODELS[key])))

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, (name, mt, desc, key) in zip([c1, c2, c3, c4], [
        ("PD vs HC — Ahh",    "SVC", "Binary classifier on sustained phonation for vocal fold rigidity.", "ahh"),
        ("PD vs HC — Vowels", "SVC", "Binary classifier on sustained vowel production.", "vowels"),
        ("PD vs HC — Text",   "SVC", "Binary classifier on connected speech.", "text"),
        ("4-Class Differential", "SVC", "Multi-class: Healthy, PD, PSP, MSA differentiation.", "fourclass"),
    ]):
        with col:
            model_card(name, mt, desc, os.path.exists(os.path.join(VOICE_MODEL_DIR, VOICE_MODELS[key])))

    # Footer
    st.markdown("""
    <div class="nt-footer">
        <div class="nt-footer-disclaimer">
            NeuroTrace is a research screening tool and is not a substitute for professional
            medical diagnosis. This tool has not been evaluated or approved by the FDA.
            Always consult a qualified healthcare professional for medical advice, diagnosis,
            or treatment. Do not use this tool as the sole basis for any medical decision.
        </div>
        <div class="nt-footer-copy">NeuroTrace &nbsp;·&nbsp; © 2026</div>
    </div>
    """, unsafe_allow_html=True)
