import streamlit as st
st.set_page_config(page_title="NeuroTrace", page_icon="NT", layout="wide", initial_sidebar_state="collapsed")
from utils.session import init_session_state
init_session_state()

# Read active tab from URL query param (?tab=overview)
from utils.constants import TABS
valid_tabs = [k for k, _ in TABS]
qp_tab = st.query_params.get("tab", None)
if qp_tab in valid_tabs:
    st.session_state["active_tab"] = qp_tab

from styles.theme import inject_theme
inject_theme()
st.markdown('<style>[data-testid="stSidebar"]{display:none!important}[data-testid="stSidebarCollapsedControl"]{display:none!important}</style>', unsafe_allow_html=True)
from components.navbar import render_navbar
render_navbar()
from utils.session import get_active_tab
tab = get_active_tab()
if tab=="overview": from pages.overview import render; render()
elif tab=="handwriting": from pages.handwriting import render; render()
elif tab=="voice": from pages.voice import render; render()
elif tab=="survey": from pages.lifestyle import render; render()
elif tab=="report": from pages.report import render; render()
elif tab=="science": from pages.science import render; render()
elif tab=="platform": from pages.platform import render; render()
else: from pages.overview import render; render()
from components.cards import page_footer; page_footer()
