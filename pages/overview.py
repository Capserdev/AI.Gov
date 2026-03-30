import os, streamlit as st
from components.cards import stat_card, model_card, section_header, divider
from utils.session import navigate_to
from utils.constants import HANDWRITING_MODEL_DIR, VOICE_MODEL_DIR, HANDWRITING_MODELS, VOICE_MODELS

def render():
    st.markdown("""<div class="nt-hero"><div class="nt-hero-badge">NC HOSA 2026 &middot; MEDICAL INNOVATIONS</div><h1>Parkinson's screening<br>through <span>digital biomarkers</span></h1><p>NeuroTrace combines handwriting analysis, vocal biomarkers, and lifestyle assessment into a unified, non-invasive screening tool powered by deep learning.</p></div>""", unsafe_allow_html=True)
    c1,c2,c3 = st.columns([1,2,1])
    with c2:
        b1,b2 = st.columns(2)
        with b1:
            if st.button("Start Screening", key="hero_start", type="primary", use_container_width=True):
                navigate_to("handwriting"); st.rerun()
        with b2:
            if st.button("Learn More", key="hero_learn", type="secondary", use_container_width=True):
                navigate_to("science"); st.rerun()
    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: stat_card("10M+","People affected globally","fade-up-1")
    with c2: stat_card("7","ML models","fade-up-2")
    with c3: stat_card("3","Diagnostic modalities","fade-up-3")
    with c4: stat_card("89%","Avg model accuracy","fade-up-4")
    divider()
    section_header("How it works","Three complementary modalities for comprehensive screening.")
    c1,c2,c3 = st.columns(3)
    with c1: st.markdown('<div class="nt-card" style="text-align:center;height:100%;"><div style="font-family:var(--font-mono);font-size:2rem;color:var(--accent);margin-bottom:0.5rem;">01</div><div style="font-family:var(--font-display);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Handwriting Analysis</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.55;">Upload meander, spiral, and wave drawings. EfficientNetV2B0 models with 4x TTA detect micrographia and tremor patterns.</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="nt-card" style="text-align:center;height:100%;"><div style="font-family:var(--font-mono);font-size:2rem;color:var(--purple);margin-bottom:0.5rem;">02</div><div style="font-family:var(--font-display);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Voice Analysis</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.55;">Record sustained vowels and connected speech. SVC models analyze jitter, shimmer, and MFCC features.</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="nt-card" style="text-align:center;height:100%;"><div style="font-family:var(--font-mono);font-size:2rem;color:var(--green);margin-bottom:0.5rem;">03</div><div style="font-family:var(--font-display);font-size:1.1rem;color:var(--text);margin-bottom:0.5rem;">Lifestyle Survey</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.55;">Clinically-validated questionnaire assessing motor symptoms, non-motor indicators, and established risk factors.</div></div>', unsafe_allow_html=True)
    divider()
    section_header("Models","Seven specialized models across two diagnostic modalities.")
    c1,c2,c3 = st.columns(3)
    for col,(name,mt,desc,key) in zip([c1,c2,c3],[("Meander Model","VISION","EfficientNetV2B0 fine-tuned on meander drawing patterns to detect tremor irregularities.","meander"),("Spiral Model","VISION","EfficientNetV2B0 fine-tuned on Archimedean spiral drawings for tremor amplitude analysis.","spiral"),("Wave Model","VISION","EfficientNetV2B0 fine-tuned on sinusoidal wave tracings for motor control assessment.","wave")]):
        with col: model_card(name,mt,desc,os.path.exists(os.path.join(HANDWRITING_MODEL_DIR,HANDWRITING_MODELS[key])))
    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    for col,(name,mt,desc,key) in zip([c1,c2,c3,c4],[("PD vs HC — Ahh","SVC","Binary classifier on sustained phonation for vocal fold rigidity.","ahh"),("PD vs HC — Vowels","SVC","Binary classifier on sustained vowel production for articulatory deficits.","vowels"),("PD vs HC — Text","SVC","Binary classifier on connected speech for prosodic abnormalities.","text"),("4-Class Differential","SVC","Multi-class model: Healthy, PD, PSP, MSA differentiation.","fourclass")]):
        with col: model_card(name,mt,desc,os.path.exists(os.path.join(VOICE_MODEL_DIR,VOICE_MODELS[key])))
