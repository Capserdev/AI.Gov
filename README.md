# NeuroTrace — AI-Powered Parkinson's Screening Platform

> Presented at the **AI Presidential Challenge 2026**
> Built by Luis Cruz

NeuroTrace is a multimodal machine learning platform for non-invasive Parkinson's disease screening. It combines handwriting analysis, vocal biomarkers, and lifestyle assessment into a unified web application powered by deep learning and support vector machines.

---

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://capserdev-ai-gov.streamlit.app)

---

## What It Does

NeuroTrace screens for Parkinson's disease (PD) and atypical parkinsonian syndromes (PSP, MSA) using three complementary modalities:

| Modality | Method | Models |
|---|---|---|
| **Handwriting** | Meander, spiral, and wave drawing analysis | EfficientNetV2-B0 (transfer learning) |
| **Voice** | Sustained vowels, "ahh" phonation, short text | RBF-kernel SVM |
| **Survey** | Clinically-validated lifestyle questionnaire | Rule-based scoring |

Results from all three modalities are combined into a weighted ensemble risk score.

---

## Model Performance

### Handwriting Models (PD vs. Healthy Control)
| Task | Accuracy | AUC |
|---|---|---|
| Meander | 94.6% | 0.968 |
| Spiral (ensemble) | 90.0% | 0.947 |
| Wave | 93.3% | 0.973 |

### Voice Models
| Task | Accuracy | AUC |
|---|---|---|
| Sustained "ahh" | 90.9% | 0.967 |
| Sustained vowels | 79.5% | 0.932 |
| Short text | 86.7% | 0.852 |
| 4-class (HC / PD / PSP / MSA) | 85.7% | — |

---

## Project Structure

```
neurotrace/
├── app.py                      # Main Streamlit entry point
├── requirements.txt
├── runtime.txt
│
├── pages/
│   ├── overview.py             # Landing page
│   ├── handwriting.py          # Handwriting upload + analysis
│   ├── voice.py                # Voice recording + analysis
│   ├── lifestyle.py            # Survey
│   ├── report.py               # Combined risk report
│   ├── science.py              # Paper figures + methodology
│   └── platform.py             # Tech stack overview
│
├── core/
│   ├── handwriting_engine.py   # TensorFlow model loading + TTA inference
│   ├── voice_engine.py         # Feature extraction + SVM inference
│   ├── survey_engine.py        # Survey scoring
│   ├── report_engine.py        # Ensemble score computation
│   └── demo_mode.py            # Simulated predictions (no models needed)
│
├── components/
│   ├── navbar.py               # HTML navbar with query-param navigation
│   ├── cards.py                # UI components (stat cards, section headers, footer)
│   └── charts.py               # Risk ring + score bar charts
│
├── models/
│   ├── handwriting/            # .keras model files (EfficientNetV2-B0)
│   └── voice/                  # .joblib SVM model files
│
├── assets/                     # Paper figures and logo images
├── styles/
│   └── theme.py                # Global CSS theme injection
└── utils/
    ├── constants.py            # Model paths, weights, tab config
    └── session.py              # Session state helpers
```

---

## Running Locally

```bash
git clone https://github.com/Capserdev/AI.Gov.git
cd AI.Gov
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install tensorflow>=2.15.0  # Required for live handwriting inference
streamlit run app.py
```

Open http://localhost:8501.

> **Note:** Without TensorFlow installed, the handwriting tab runs in **DEMO MODE** with simulated predictions. All other tabs work normally.

---

## How the Handwriting Models Work

1. User uploads a meander, spiral, or wave drawing
2. Image is resized to 224x224 and normalized to [0, 1]
3. EfficientNetV2-B0 (fine-tuned on PD vs. HC drawings) outputs a sigmoid probability
4. **Test-Time Augmentation (TTA)**: 4 augmented versions (original, flipped, rotated) are averaged for a more robust prediction
5. The three drawing scores are combined via weighted ensemble

Grad-CAM visualizations show the models focus on stroke irregularities, tremor-like oscillations, and regions of amplitude variation — consistent with known PD motor symptoms.

---

## How the Voice Models Work

1. Audio is resampled to 16 kHz mono, silence-trimmed, and amplitude-normalized
2. 36 acoustic features are extracted: 13 MFCC means + 13 MFCC stds, pitch (F0), spectral centroid, bandwidth, rolloff, flatness, ZCR
3. Features are standardized and passed to an RBF-kernel SVM
4. Binary models (PD vs. HC) are trained separately for AHH, vowels, and text tasks
5. A 4-class model (HC / PD / PSP / MSA) is trained on sustained vowels only

---

## Research Background

This project is based on original research studying short voice tasks and handwriting drawings as digital biomarkers for Parkinson's disease, PSP, and MSA classification.

**Paper:** Classifying Parkinson's Disease, PSP, and MSA: A Multimodal Machine Learning Study on Short Voice Tasks and Spiral/Wave Handwriting

**Datasets used:**
- Parkinson's Disease voice dataset (multiple sound recording types)
- Archive3 handwriting dataset (meander, spiral, wave drawings)
- Combined handwriting test set: 254 images (balanced HC/PD)

---

## Disclaimer

NeuroTrace is a **research and screening tool only**. It is not a medical device and does not provide clinical diagnoses. All results should be interpreted by a qualified healthcare professional.

---

## Tech Stack

| Component | Technology |
|---|---|
| Web framework | Streamlit 1.55 |
| Handwriting models | TensorFlow / Keras, EfficientNetV2-B0 |
| Voice models | scikit-learn, SVM (RBF kernel) |
| Audio processing | librosa, soundfile |
| Image processing | Pillow, NumPy |
| Charts | Plotly |
| Deployment | Streamlit Community Cloud |
