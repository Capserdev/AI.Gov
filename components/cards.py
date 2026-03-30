import streamlit as st

def stat_card(value, label, delay="fade-up"):
    st.markdown(f'<div class="nt-stat {delay}"><div class="stat-value">{value}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

def info_card(title, body, color="var(--accent)"):
    st.markdown(f'<div class="nt-card"><div style="font-family:var(--font-mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;color:{color};margin-bottom:0.5rem;">{title}</div><div style="font-size:0.9rem;color:var(--text-secondary);line-height:1.6;">{body}</div></div>', unsafe_allow_html=True)

def model_card(name, mtype, desc, is_live):
    sc = "live" if is_live else "demo"
    st_text = "LIVE" if is_live else "DEMO"
    dot = "var(--green)" if is_live else "var(--amber)"
    st.markdown(f'<div class="nt-card" style="height:100%;"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;"><span style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);">{mtype}</span><span class="nt-status-pill {sc}"><span class="pulse-dot" style="background:{dot};"></span>{st_text}</span></div><div style="font-family:var(--font-display);font-size:1.15rem;color:var(--text);margin-bottom:0.5rem;">{name}</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.55;">{desc}</div></div>', unsafe_allow_html=True)

def section_header(title, subtitle=""):
    st.markdown(f'<div class="nt-section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="nt-section-subtitle">{subtitle}</div>', unsafe_allow_html=True)

def divider():
    st.markdown('<hr class="nt-divider">', unsafe_allow_html=True)
