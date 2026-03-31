import os, base64, streamlit as st
from utils.constants import TABS
from utils.session import navigate_to

def _img_b64(path):
    try:
        with open(os.path.abspath(path), "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

def render_navbar():
    active = st.session_state.get("active_tab", "overview")

    aigov_path = os.path.join(os.path.dirname(__file__), "..", "assets", "aigov.png")
    aigov_b64 = _img_b64(aigov_path)
    aigov_html = (
        f'<img src="data:image/png;base64,{aigov_b64}" '
        f'style="height:24px;border-radius:3px;opacity:0.9;vertical-align:middle;margin-left:10px;" />'
        if aigov_b64 else ""
    )

    links_html = "".join(
        f'<a class="nt-nav-link {"active" if key == active else ""}" href="?tab={key}">{label}</a>'
        for key, label in TABS
    )

    st.markdown(
        f'<div class="nt-navbar">'
        f'<div class="nt-logo">NeuroTrace{aigov_html}</div>'
        f'<nav class="nt-nav-links">{links_html}</nav>'
        f'</div>',
        unsafe_allow_html=True
    )
