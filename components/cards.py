import streamlit as st

def stat_card(value, label, delay=""):
    st.markdown(
        f'<div class="nt-stat">'
        f'<div class="stat-value">{value}</div>'
        f'<div class="stat-label">{label}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def info_card(title, body, color="var(--text)"):
    st.markdown(
        f'<div class="nt-card">'
        f'<div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-dim);margin-bottom:0.6rem;">{title}</div>'
        f'<div style="font-size:0.85rem;color:var(--text-muted);line-height:1.65;">{body}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def model_card(name, mtype, desc, is_live):
    status = "LIVE" if is_live else "DEMO"
    pill_cls = "live" if is_live else "demo"
    dot_color = "var(--green)" if is_live else "var(--amber)"
    st.markdown(
        f'<div class="nt-card">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">'
        f'<span style="font-family:var(--font-mono);font-size:0.55rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-dim);">{mtype}</span>'
        f'<span class="nt-status-pill {pill_cls}"><span class="pulse-dot" style="background:{dot_color};"></span>{status}</span>'
        f'</div>'
        f'<div style="font-family:var(--font-serif);font-size:1rem;color:var(--text);margin-bottom:0.5rem;">{name}</div>'
        f'<div style="font-size:0.8rem;color:var(--text-muted);line-height:1.6;">{desc}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def section_header(title, subtitle="", num=""):
    label = f'<div class="nt-section-label"><span class="nt-section-num">{num}</span><span class="nt-section-name">{title}</span></div>' if num else \
            f'<div class="nt-section-label"><span class="nt-section-name">{title}</span></div>'
    st.markdown(label, unsafe_allow_html=True)
    if subtitle:
        st.markdown(
            f'<div style="font-family:var(--font-serif);font-size:1.6rem;font-weight:400;color:var(--text);letter-spacing:-0.02em;margin-bottom:1rem;">{subtitle}</div>',
            unsafe_allow_html=True
        )

def divider():
    st.markdown('<hr class="nt-divider">', unsafe_allow_html=True)

def page_footer():
    st.markdown(
        '<div style="margin-top:3rem;padding:1.5rem 0 1rem;border-top:1px solid var(--border);'
        'text-align:center;font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;'
        'text-transform:uppercase;color:var(--text-dim);">'
        'Conceptualized and developed in the United States&nbsp;🇺🇸'
        '</div>',
        unsafe_allow_html=True
    )
