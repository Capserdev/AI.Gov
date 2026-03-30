import streamlit as st

def init_session_state():
    defaults = {
        "active_tab": "overview",
        "handwriting_results": {},
        "voice_results": {},
        "voice_4class": {},
        "survey_answers": {},
        "survey_score": None,
        "combined_score": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def navigate_to(tab_name):
    st.session_state["active_tab"] = tab_name

def get_active_tab():
    return st.session_state.get("active_tab", "overview")

def get_risk_color(score):
    if score < 0.30: return "#22c55e"
    elif score < 0.60: return "#f59e0b"
    elif score < 0.80: return "#f97316"
    else: return "#ef4444"

def get_risk_label(score):
    if score < 0.30: return "Low Risk"
    elif score < 0.60: return "Moderate Risk"
    elif score < 0.80: return "Elevated Risk"
    else: return "High Risk"
