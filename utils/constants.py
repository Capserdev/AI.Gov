HANDWRITING_MODEL_DIR = "models/handwriting"
VOICE_MODEL_DIR = "models/voice"
HANDWRITING_MODELS = {
    "meander": "MeanderModel_finetune_best.keras",
    "spiral": "SpiralModel_1_finetune_best.keras",
    "wave": "WaveModel_finetune_best.keras",
}
VOICE_MODELS = {
    "ahh": "PD_vs_HC_AHH.joblib",
    "vowels": "PD_vs_HC_vowels.joblib",
    "text": "PD_vs_HC_text.joblib",
    "fourclass": "Vowels_4class_HC_PD_PSP_MSA.joblib",
}
HANDWRITING_WEIGHTS = {"meander": 0.33, "spiral": 0.34, "wave": 0.33}
VOICE_BINARY_WEIGHTS = {"ahh": 0.35, "vowels": 0.35, "text": 0.30}
COMBINED_WEIGHTS = {"handwriting": 0.40, "voice": 0.35, "survey": 0.25}
N_MFCC = 13
SAMPLE_RATE = 22050
N_VOICE_FEATURES = 36
IMG_SIZE = 224
TTA_PASSES = 4
TABS = [
    ("overview", "OVERVIEW"),
    ("handwriting", "HANDWRITING"),
    ("voice", "VOICE"),
    ("survey", "SURVEY"),
    ("report", "REPORT"),
    ("science", "SCIENCE"),
    ("platform", "STACK"),
]
