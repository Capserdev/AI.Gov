import streamlit as st
from components.cards import section_header, divider, info_card

def render():
    section_header("The Science","Understanding the digital biomarkers and clinical research behind NeuroTrace.")
    st.markdown('<div class="nt-card-static" style="margin-bottom:1.5rem;"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">THE CLINICAL NEED</div><div style="font-size:0.9rem;color:var(--text-secondary);line-height:1.7;">Parkinson\'s disease affects over <strong style="color:var(--text);">10 million people worldwide</strong>. The average time from symptom onset to diagnosis is <strong style="color:var(--text);">1-2 years</strong>, and up to <strong style="color:var(--text);">30% of early diagnoses are incorrect</strong>. NeuroTrace offers a free, non-invasive, AI-powered screening tool that can be administered in under 5 minutes.</div></div>', unsafe_allow_html=True)
    divider()
    section_header("Handwriting Biomarkers","How motor control deficits manifest in drawing tasks.")
    c1,c2,c3 = st.columns(3)
    with c1: info_card("MICROGRAPHIA","Progressive reduction in handwriting size present in up to 63% of PD patients. The meander and wave tests are particularly sensitive to this decline.","#4f9cf9")
    with c2: info_card("TREMOR PATTERNS","Resting tremor at 4-6 Hz is the hallmark motor symptom. Spiral drawings capture tremor-induced oscillations extracted by CNN feature maps.","#a78bfa")
    with c3: info_card("BRADYKINESIA","Slowness of movement affects drawing fluency. Wave patterns reveal hesitation points that correlate with UPDRS motor scores.","#22c55e")
    divider()
    section_header("Vocal Biomarkers","Acoustic features that indicate neurodegenerative changes.")
    feats = [("Jitter","Cycle-to-cycle pitch perturbation. Elevated jitter indicates irregular vocal fold vibration. Normal: <1.04%, PD typical: 1.5-3%."),("Shimmer","Cycle-to-cycle amplitude variation. Reflects reduced neuromuscular control of vocal intensity. Normal: <3.81%, PD typical: 4-8%."),("HNR","Harmonic-to-Noise Ratio. Lower HNR indicates breathier, rougher voice quality. Normal: >20dB, PD typical: 10-18dB."),("MFCC","13 Mel-Frequency Cepstral Coefficient means and standard deviations form the core feature set encoding articulatory patterns."),("Spectral Features","Centroid, bandwidth, rolloff, and flatness characterize frequency distribution. PD shows reduced spectral variability."),("ZCR","Zero Crossing Rate reflects signal noisiness. Higher ZCR correlates with breathier phonation common in PD.")]
    for i in range(0,len(feats),3):
        cols = st.columns(3)
        for j,col in enumerate(cols):
            if i+j<len(feats):
                with col: info_card(feats[i+j][0],feats[i+j][1])
    divider()
    section_header("Conditions","The four conditions assessed by NeuroTrace.")
    conds = [("Parkinson's Disease","#ef4444","The most common neurodegenerative movement disorder. Cardinal features: resting tremor, rigidity, bradykinesia, postural instability."),("PSP","#f59e0b","Progressive Supranuclear Palsy. A rare tauopathy causing vertical gaze palsy and postural instability. Often misdiagnosed as PD."),("MSA","#a78bfa","Multiple System Atrophy. A synucleinopathy affecting the autonomic nervous system, cerebellum, and basal ganglia."),("Healthy Control","#22c55e","Individuals without neurodegenerative disease. Serve as the baseline comparison group for all models.")]
    c1,c2 = st.columns(2)
    for i,(n,c,d) in enumerate(conds):
        with (c1 if i%2==0 else c2):
            st.markdown(f'<div class="nt-card" style="margin-bottom:1rem;border-left:3px solid {c};"><div style="font-family:var(--font-display);font-size:1.05rem;color:var(--text);margin-bottom:0.5rem;">{n}</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.6;">{d}</div></div>', unsafe_allow_html=True)
