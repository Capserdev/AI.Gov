import os, tempfile, numpy as np, streamlit as st
from utils.constants import VOICE_MODEL_DIR, VOICE_MODELS, N_MFCC, SAMPLE_RATE, N_VOICE_FEATURES

@st.cache_resource
def load_voice_models():
    models = {}
    try:
        import joblib
        for name, fname in VOICE_MODELS.items():
            path = os.path.join(VOICE_MODEL_DIR, fname)
            if os.path.exists(path): models[name] = joblib.load(path)
    except ImportError: pass
    return models

def extract_features(audio_bytes, filename="audio.wav"):
    import librosa
    suffix = os.path.splitext(filename)[1] or ".wav"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(audio_bytes); tmp_path = tmp.name
    try: y, sr = librosa.load(tmp_path, sr=SAMPLE_RATE, mono=True)
    finally: os.unlink(tmp_path)
    feats = []
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    feats.extend(np.mean(mfccs,axis=1).tolist()); feats.extend(np.std(mfccs,axis=1).tolist())
    pitches,_ = librosa.piptrack(y=y,sr=sr); pv=pitches[pitches>0]
    feats.append(float(np.mean(np.abs(np.diff(pv)))/np.mean(pv)) if len(pv)>1 else 0.0)
    rms=librosa.feature.rms(y=y)[0]
    feats.append(float(np.mean(np.abs(np.diff(rms)))/(np.mean(rms)+1e-10)) if len(rms)>1 else 0.0)
    ac=np.correlate(y[:min(len(y),sr)],y[:min(len(y),sr)],mode="full"); ac=ac[len(ac)//2:]
    feats.append(float(10*np.log10(ac[0]/(np.mean(np.abs(ac[1:]))+1e-10)+1e-10)) if len(ac)>1 and ac[0]>0 else 0.0)
    feats.append(float(np.mean(librosa.feature.zero_crossing_rate(y=y))))
    feats.append(float(np.mean(librosa.feature.spectral_centroid(y=y,sr=sr))))
    feats.append(float(np.mean(librosa.feature.spectral_bandwidth(y=y,sr=sr))))
    feats.append(float(np.mean(librosa.feature.spectral_rolloff(y=y,sr=sr))))
    feats.append(float(np.mean(librosa.feature.spectral_flatness(y=y))))
    while len(feats)<N_VOICE_FEATURES: feats.append(0.0)
    return np.array(feats[:N_VOICE_FEATURES],dtype=np.float64).reshape(1,-1)

def predict_binary(model, features):
    try:
        p = model.predict_proba(features)
        return round(float(p[0,1] if p.shape[1]==2 else p[0,0]),4)
    except AttributeError:
        d = model.decision_function(features)
        return round(float(1/(1+np.exp(-float(d[0])))),4)

def predict_4class(model, features):
    names = ["Healthy Control","Parkinson's Disease","PSP","MSA"]
    try:
        p = model.predict_proba(features)[0]
        return {n: round(float(p[i]),4) if i<len(p) else 0.0 for i,n in enumerate(names)}
    except AttributeError:
        pred = int(model.predict(features)[0])
        r = {n:0.0 for n in names}
        if pred < len(names): r[names[pred]] = 1.0
        return r
