import streamlit as st

def inject_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500&display=swap');

    :root {
        --bg:          #f0ede8;
        --bg-alt:      #e8e4de;
        --border:      #d4cfc8;
        --border-dark: #b0ab a3;
        --text:        #0d0d0d;
        --text-muted:  #3d3a36;
        --text-dim:    #6b6560;
        --accent:      #1a1a1a;
        --green:       #3a7a4a;
        --amber:       #8a6a20;
        --red:         #8a2a2a;
        --font-serif:  'Playfair Display', Georgia, 'Times New Roman', serif;
        --font-sans:   'Inter', system-ui, sans-serif;
        --font-mono:   'Courier New', 'Lucida Console', monospace;
        --radius:      4px;
        --radius-pill: 100px;
    }

    /* ── Base ── */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: var(--bg) !important;
        color: var(--text) !important;
        font-family: var(--font-sans) !important;
    }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stStatusWidget"] { display: none !important; }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    /* ── Navbar ── */
    .nt-navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.1rem 0 1.1rem 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 0;
        background: var(--bg);
    }
    .nt-logo {
        font-family: var(--font-serif);
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--text);
        letter-spacing: -0.01em;
    }
    .nt-nav-links {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    .nt-nav-links a, .nt-nav-btn-label {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--text-muted);
        text-decoration: none;
        cursor: pointer;
    }
    .nt-nav-btn-label.active { color: var(--text); }

    /* ── Section label (e.g. "01 OVERVIEW") ── */
    .nt-section-label {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid var(--border);
    }
    .nt-section-num {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        letter-spacing: 0.1em;
        color: var(--text-dim);
    }
    .nt-section-name {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--text-muted);
    }

    /* ── Hero ── */
    .nt-hero {
        padding: 5rem 0 3.5rem 0;
    }
    .nt-hero h1 {
        font-family: var(--font-serif) !important;
        font-size: 3.2rem !important;
        font-weight: 400 !important;
        line-height: 1.15 !important;
        color: var(--text) !important;
        margin: 0 0 1.25rem 0 !important;
        letter-spacing: -0.02em;
    }
    .nt-hero h1 span { font-style: italic; }
    .nt-hero p {
        font-size: 1rem;
        color: var(--text-muted);
        line-height: 1.7;
        max-width: 560px;
        margin-bottom: 2rem;
    }

    /* ── Pill badge ── */
    .nt-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        border: 1px solid var(--border-dark, #c0bbb3);
        border-radius: var(--radius-pill);
        padding: 0.35rem 0.85rem;
        font-family: var(--font-mono);
        font-size: 0.58rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--text-muted);
        background: transparent;
    }
    .nt-pill-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--green);
        flex-shrink: 0;
    }

    /* ── Cards ── */
    .nt-card {
        background: var(--bg-alt);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .nt-card-plain {
        border-top: 1px solid var(--border);
        padding: 1.25rem 0;
        margin-bottom: 0;
    }
    .nt-card-static {
        background: transparent;
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }

    /* ── Stat cards ── */
    .nt-stat {
        border-top: 1px solid var(--border);
        padding: 1.5rem 0 1rem 0;
    }
    .stat-value {
        font-family: var(--font-serif);
        font-size: 2.4rem;
        font-weight: 400;
        color: var(--text);
        letter-spacing: -0.02em;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .stat-label {
        font-family: var(--font-mono);
        font-size: 0.6rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--text-dim);
    }

    /* ── Section titles ── */
    .nt-section-title {
        font-family: var(--font-serif);
        font-size: 1.9rem;
        font-weight: 400;
        color: var(--text);
        letter-spacing: -0.02em;
        margin-bottom: 0.4rem;
    }
    .nt-section-subtitle {
        font-size: 0.88rem;
        color: var(--text-muted);
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }

    /* ── Divider ── */
    .nt-divider {
        border: none;
        border-top: 1px solid var(--border);
        margin: 2.5rem 0;
    }

    /* ── Result bar ── */
    .nt-result-bar {
        height: 3px;
        background: var(--border);
        border-radius: 2px;
        overflow: hidden;
    }
    .nt-result-bar-fill {
        height: 100%;
        border-radius: 2px;
        background: var(--text);
        transition: width 0.4s ease;
    }

    /* ── Status pill ── */
    .nt-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.2rem 0.6rem;
        border-radius: var(--radius-pill);
        font-family: var(--font-mono);
        font-size: 0.55rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        border: 1px solid var(--border);
        color: var(--text-muted);
    }
    .nt-status-pill.live { border-color: var(--green); color: var(--green); }
    .nt-status-pill.demo { border-color: var(--amber); color: var(--amber); }
    .pulse-dot {
        width: 5px; height: 5px;
        border-radius: 50%;
        flex-shrink: 0;
    }

    /* ── Navbar ── */
    .nt-navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 0;
    }
    .nt-logo {
        font-family: var(--font-serif);
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--text);
        letter-spacing: -0.01em;
        white-space: nowrap;
        display: flex;
        align-items: center;
    }
    .nt-nav-links {
        display: flex;
        gap: 1.75rem;
        align-items: center;
        flex-wrap: nowrap;
    }
    .nt-nav-link {
        font-family: var(--font-mono);
        font-size: 0.62rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--text-muted);
        white-space: nowrap;
        text-decoration: none;
        transition: color 0.15s;
        user-select: none;
    }
    .nt-nav-link:hover { color: var(--text); }
    .nt-nav-link.active { color: var(--text); }

    /* ── Streamlit widget overrides (non-navbar buttons) ── */
    .stButton > button {
        background: transparent;
        border: 1px solid var(--border-dark, #c0bbb3);
        border-radius: var(--radius-pill);
        color: var(--text);
        font-family: var(--font-mono);
        font-size: 0.65rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 0.5rem 1.25rem;
        transition: all 0.15s;
    }
    .stButton > button:hover {
        background: var(--text);
        color: var(--bg);
        border-color: var(--text);
    }
    .stFileUploader {
        background: var(--bg-alt) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
    }
    .stRadio > label, .stSelectbox > label {
        font-family: var(--font-mono) !important;
        font-size: 0.65rem !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        color: var(--text-muted) !important;
    }
    .stProgress > div > div {
        background: var(--border) !important;
    }
    .stProgress > div > div > div {
        background: var(--text) !important;
    }

    /* ── Footer ── */
    .nt-footer {
        border-top: 1px solid var(--border);
        margin-top: 4rem;
        padding: 2rem 0 1.5rem 0;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 2rem;
    }
    .nt-footer-disclaimer {
        font-family: var(--font-mono);
        font-size: 0.55rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--text-dim);
        line-height: 1.8;
        max-width: 600px;
    }
    .nt-footer-copy {
        font-family: var(--font-mono);
        font-size: 0.55rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--text-dim);
        white-space: nowrap;
    }
    </style>
    """, unsafe_allow_html=True)
