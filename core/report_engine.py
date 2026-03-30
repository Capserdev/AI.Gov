from utils.constants import COMBINED_WEIGHTS, VOICE_BINARY_WEIGHTS, HANDWRITING_WEIGHTS

def compute_handwriting_ensemble(results):
    if "ensemble" in results: return results["ensemble"]
    if not results: return 0.0
    return sum(results.values()) / len(results)

def compute_voice_ensemble(results):
    if not results: return 0.0
    s = w = 0.0
    for k, weight in VOICE_BINARY_WEIGHTS.items():
        if k in results: s += results[k]*weight; w += weight
    return round(s/w, 4) if w else 0.0

def compute_combined_score(hw=None, voice=None, survey=None):
    src = {}
    if hw is not None: src["handwriting"] = hw
    if voice is not None: src["voice"] = voice
    if survey is not None: src["survey"] = survey
    if not src: return 0.0
    s = w = 0.0
    for k, v in src.items(): wt = COMBINED_WEIGHTS.get(k, 0.25); s += v*wt; w += wt
    return round(s/w, 4)

def get_modality_breakdown(hw=None, voice=None, survey=None):
    b = {}
    if hw is not None: b["handwriting"] = hw
    if voice is not None: b["voice"] = voice
    if survey is not None: b["survey"] = survey
    return b
