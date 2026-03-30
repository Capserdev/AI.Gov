import os, streamlit as st
from components.cards import section_header, divider
from components.charts import risk_ring, score_bars
from utils.constants import VOICE_MODEL_DIR, VOICE_MODELS
from utils.session import get_risk_color, get_risk_label
from core.demo_mode import demo_voice_binary_predict, demo_voice_4class_predict
from core.report_engine import compute_voice_ensemble

def render():
    demo = not any(os.path.exists(os.path.join(VOICE_MODEL_DIR,f)) for f in VOICE_MODELS.values())
    section_header("Voice Analysis","Upload audio recordings for vocal biomarker assessment.")
    sc = "demo" if demo else "live"; dot = "var(--amber)" if demo else "var(--green)"
    st.markdown(f'<span class="nt-status-pill {sc}"><span class="pulse-dot" style="background:{dot};"></span>{"DEMO" if demo else "LIVE"} MODE</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if not demo:
        from core.voice_engine import load_voice_models, extract_features, predict_binary, predict_4class
        models = load_voice_models()
    section_header("Binary Classification","PD vs Healthy Control across three vocal tasks.")
    tasks = [("ahh","Sustained Ahh","Record a sustained 'Ahh' sound for 3-5 seconds","#4f9cf9"),("vowels","Sustained Vowels","Record sustained vowel sounds (A, E, I, O, U)","#a78bfa"),("text","Connected Speech","Record yourself reading a short passage aloud","#f59e0b")]
    vr = st.session_state.get("voice_results", {})
    cols = st.columns(3)
    for col,(key,title,desc,color) in zip(cols,tasks):
        with col:
            st.markdown(f'<div class="nt-card-static" style="border-left:3px solid {color};"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:{color};margin-bottom:0.35rem;">{title.upper()}</div><div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:0.75rem;">{desc}</div></div>', unsafe_allow_html=True)
            up = st.file_uploader(f"Upload {title}", type=["wav","mp3","ogg","m4a","flac"], key=f"v_{key}", label_visibility="collapsed")
            if up:
                st.audio(up)
                score = demo_voice_binary_predict(key, up.name) if demo else (predict_binary(models[key], extract_features(up.getvalue(), up.name)) if key in models else demo_voice_binary_predict(key, up.name))
                vr[key] = score; st.session_state["voice_results"] = vr
                c = get_risk_color(score)
                st.markdown(f'<div style="text-align:center;padding:0.75rem 0;"><div style="font-family:var(--font-display);font-size:1.8rem;color:{c};">{int(score*100)}%</div><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);">{get_risk_label(score)}</div></div>', unsafe_allow_html=True)
    if vr:
        divider(); c1,c2 = st.columns(2)
        with c1: risk_ring(compute_voice_ensemble(vr), label="Voice Risk")
        with c2: st.markdown("<br>", unsafe_allow_html=True); score_bars(vr,{"ahh":"#4f9cf9","vowels":"#a78bfa","text":"#f59e0b"})
    divider()
    section_header("Differential Diagnosis","4-class model: Healthy Control, Parkinson's Disease, PSP, and MSA.")
    up4 = st.file_uploader("Upload audio for differential diagnosis", type=["wav","mp3","ogg","m4a","flac"], key="v_4class")
    if up4:
        st.audio(up4)
        cp = demo_voice_4class_predict(up4.name) if demo else (predict_4class(models["fourclass"], extract_features(up4.getvalue(), up4.name)) if "fourclass" in models else demo_voice_4class_predict(up4.name))
        st.session_state["voice_4class"] = cp
        clrs = {"Healthy Control":"#22c55e","Parkinson's Disease":"#ef4444","PSP":"#f59e0b","MSA":"#a78bfa"}
        st.markdown("<br>", unsafe_allow_html=True)
        cols4 = st.columns(4)
        for col,(cn,prob) in zip(cols4,cp.items()):
            with col:
                c = clrs.get(cn,"#4f9cf9")
                st.markdown(f'<div class="nt-card" style="text-align:center;"><div style="font-family:var(--font-display);font-size:1.6rem;color:{c};">{int(prob*100)}%</div><div style="font-family:var(--font-mono);font-size:0.55rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--text-muted);margin-top:0.25rem;">{cn.upper()}</div></div>', unsafe_allow_html=True)
        top = max(cp, key=cp.get)
        st.markdown(f'<div style="text-align:center;margin-top:1.5rem;"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:0.25rem;">PRIMARY INDICATION</div><div style="font-family:var(--font-display);font-size:1.25rem;color:{clrs.get(top,"#4f9cf9")};">{top}</div></div>', unsafe_allow_html=True)
