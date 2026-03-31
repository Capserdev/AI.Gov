import streamlit as st

def inject_theme():
    st.markdown("""
    <style>
    :root {
        --bg: #0a0e1a;
        --bg-secondary: #111827;
        --accent: #4f9cf9;
        --accent-dim: rgba(79,156,249,0.15);
        --text: #e2e8f0;
        --text-secondary: #94a3b8;
        --border: rgba(79,156,249,0.2);
        --font-mono: 'Courier New', monospace;
        --radius: 12px;
    }
    body, .stApp { background-color: var(--bg); color: var(--text); }
    .nt-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }
    .nt-stat {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1rem;
        text-align: center;
    }
    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--accent);
    }
    .stat-label {
        font-size: 0.75rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.25rem;
    }
    .stButton > button {
        background: var(--accent-dim);
        border: 1px solid var(--border);
        color: var(--accent);
        border-radius: 8px;
        font-family: var(--font-mono);
        font-size: 0.8rem;
        letter-spacing: 0.05em;
    }
    .stButton > button:hover {
        background: var(--accent);
        color: var(--bg);
    }
    </style>
    """, unsafe_allow_html=True)
