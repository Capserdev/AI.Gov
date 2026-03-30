import os, numpy as np, streamlit as st
from PIL import Image
from utils.constants import HANDWRITING_MODEL_DIR, HANDWRITING_MODELS, IMG_SIZE, TTA_PASSES, HANDWRITING_WEIGHTS

@st.cache_resource
def load_handwriting_models():
    models = {}
    try:
        import tensorflow as tf
        for name, fname in HANDWRITING_MODELS.items():
            path = os.path.join(HANDWRITING_MODEL_DIR, fname)
            if os.path.exists(path):
                models[name] = tf.keras.models.load_model(path)
    except ImportError: pass
    return models

def predict_single(model, img):
    arr = np.array(img.convert("RGB").resize((IMG_SIZE,IMG_SIZE),Image.LANCZOS),dtype=np.float32)/255.0
    tta = [arr, np.fliplr(arr), np.flipud(arr), np.rot90(arr)]
    batch = np.stack(tta[:TTA_PASSES])
    preds = model.predict(batch, verbose=0)
    avg = float(np.mean(preds[:,1]) if preds.shape[-1]==2 else np.mean(preds))
    return round(avg, 4)
