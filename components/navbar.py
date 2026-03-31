import streamlit as st
from utils.constants import TABS
from utils.session import navigate_to

def render_navbar():
    active = st.session_state.get("active_tab", "overview")
    logo = '<div class="nt-logo">Neuro<span>Trace</span></div>'
    nav_items = ""
    for key, label in TABS:
        cls = "nt-nav-btn active" if key == active else "nt-nav-btn"
        nav_items += f'<div class="{cls}">{label}</div>'
    st.markdown(f'<div class="nt-navbar">{logo}{nav_items}</div>', unsafe_allow_html=True)
    cols = st.columns(len(TABS))
    for i, (key, label) in enumerate(TABS):
        with cols[i]:
            if st.button(label, key=f"nav_{key}"):
                navigate_to(key)
                st.rerun()
