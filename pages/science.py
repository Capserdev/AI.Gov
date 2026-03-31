import os, streamlit as st
from components.cards import section_header, divider, info_card

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")

def fig(path, caption):
    full = os.path.join(ASSETS, path)
    if os.path.exists(full):
        st.image(full, use_container_width=True)
        st.markdown(
            f'<div style="font-family:var(--font-sans);font-size:0.78rem;line-height:1.55;'
            f'color:var(--text-muted);text-align:left;margin-top:0.5rem;margin-bottom:1.75rem;">'
            f'{caption}</div>',
            unsafe_allow_html=True
        )

def render():
    section_header("The Science", "Understanding the digital biomarkers and clinical research behind NeuroTrace.")
    st.markdown(
        '<div class="nt-card-static" style="margin-bottom:1.5rem;">'
        '<div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);margin-bottom:0.75rem;">THE CLINICAL NEED</div>'
        '<div style="font-size:0.9rem;color:var(--text-secondary);line-height:1.7;">'
        'Parkinson\'s disease affects over <strong style="color:var(--text);">10 million people worldwide</strong>. '
        'The average time from symptom onset to diagnosis is <strong style="color:var(--text);">1–2 years</strong>, '
        'and up to <strong style="color:var(--text);">30% of early diagnoses are incorrect</strong>. '
        'NeuroTrace offers a free, non-invasive, AI-powered screening tool that can be administered in under 5 minutes.'
        '</div></div>',
        unsafe_allow_html=True
    )

    # ── PIPELINE ─────────────────────────────────────────────────────────────
    divider()
    section_header("System Pipeline", "From multimodal recording to feature extraction, model training, and evaluation.")
    fig("fig_pipeline.png", "Figure 2. Overall pipeline from multimodal recording to feature extraction, model training, and evaluation.")

    # ── HANDWRITING ──────────────────────────────────────────────────────────
    divider()
    section_header("Handwriting Biomarkers", "How motor control deficits manifest in drawing tasks.")

    c1, c2, c3 = st.columns(3)
    with c1: info_card("MICROGRAPHIA", "Progressive reduction in handwriting size present in up to 63% of PD patients. The meander and wave tests are particularly sensitive to this decline.")
    with c2: info_card("TREMOR PATTERNS", "Resting tremor at 4–6 Hz is the hallmark motor symptom. Spiral drawings capture tremor-induced oscillations extracted by CNN feature maps.")
    with c3: info_card("BRADYKINESIA", "Slowness of movement affects drawing fluency. Wave patterns reveal hesitation points that correlate with UPDRS motor scores.")

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        fig("fig_drawings.png", "Figure 1. Example meander, spiral, and wave drawings from one healthy control and one participant with Parkinson's disease. Differences in curvature, spacing, and tremor motivate automated analysis.")
    with c2:
        fig("fig_gradcam.png", "Figure 2. Grad-CAM visualizations of handwriting models. Red regions mark strokes that contributed most strongly to PD predictions, often near irregular or tremor-like segments.")

    c1, c2 = st.columns(2)
    with c1:
        fig("fig_roc_handwriting_and_4class.png", "Figure 3 & 6. ROC curves for PD vs HC handwriting models (AUC 0.947–0.973) and normalized confusion matrix for the four-class voice SVM.")
    with c2:
        fig("fig_confusion_pdvshc.png", "Figure 12. PD vs HC confusion matrices at standard and PD-optimized thresholds. Lower thresholds increase PD recall at the cost of more false positives in healthy controls.")

    # ── VOICE ────────────────────────────────────────────────────────────────
    divider()
    section_header("Vocal Biomarkers", "Acoustic features that indicate neurodegenerative changes.")

    feats = [
        ("Jitter", "Cycle-to-cycle pitch perturbation. Elevated jitter indicates irregular vocal fold vibration. Normal: <1.04%, PD typical: 1.5–3%."),
        ("Shimmer", "Cycle-to-cycle amplitude variation. Reflects reduced neuromuscular control of vocal intensity. Normal: <3.81%, PD typical: 4–8%."),
        ("HNR", "Harmonic-to-Noise Ratio. Lower HNR indicates breathier, rougher voice quality. Normal: >20 dB, PD typical: 10–18 dB."),
        ("MFCC", "13 Mel-Frequency Cepstral Coefficient means and standard deviations form the core feature set encoding articulatory patterns."),
        ("Spectral Features", "Centroid, bandwidth, rolloff, and flatness characterize frequency distribution. PD shows reduced spectral variability."),
        ("ZCR", "Zero Crossing Rate reflects signal noisiness. Higher ZCR correlates with breathier phonation common in PD."),
    ]
    for i in range(0, len(feats), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(feats):
                with col: info_card(feats[i+j][0], feats[i+j][1])

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        fig("fig_voice_transparency.png", "Figure 3 & 4. Signal-to-model transparency showing raw waveform, mel-spectrogram, and 36-dimensional feature vector for HC, PD, PSP, and MSA. Feature fingerprint shows class-level separation across all 36 features.")
    with c2:
        fig("fig_roc_voice.png", "Figure 9. ROC and accuracy across voice tasks. Vowels AUC = 0.932, AHH AUC = 0.967, Text+Spont AUC = 0.852 — showing clinically meaningful PD screening performance.")

    c1, c2 = st.columns(2)
    with c1:
        fig("fig_threshold.png", "Figure 10. Threshold tradeoff for the text-based PD vs HC model. The chosen operating point keeps PD recall very high while preserving useful precision and accuracy.")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)

    # ── CONDITIONS ───────────────────────────────────────────────────────────
    divider()
    section_header("Conditions", "The four conditions assessed by NeuroTrace.")
    conds = [
        ("Parkinson's Disease", "#ef4444", "The most common neurodegenerative movement disorder. Cardinal features: resting tremor, rigidity, bradykinesia, postural instability."),
        ("PSP", "#f59e0b", "Progressive Supranuclear Palsy. A rare tauopathy causing vertical gaze palsy and postural instability. Often misdiagnosed as PD."),
        ("MSA", "#a78bfa", "Multiple System Atrophy. A synucleinopathy affecting the autonomic nervous system, cerebellum, and basal ganglia."),
        ("Healthy Control", "#22c55e", "Individuals without neurodegenerative disease. Serve as the baseline comparison group for all models."),
    ]
    c1, c2 = st.columns(2)
    for i, (n, c, d) in enumerate(conds):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(
                f'<div class="nt-card" style="margin-bottom:1rem;border-left:3px solid {c};">'
                f'<div style="font-family:var(--font-display);font-size:1.05rem;color:var(--text);margin-bottom:0.5rem;">{n}</div>'
                f'<div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.6;">{d}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
