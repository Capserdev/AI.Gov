import streamlit as st
import math

def risk_ring(score, size=180, label="Risk Score"):
    from utils.session import get_risk_color, get_risk_label
    color = get_risk_color(score)
    rl = get_risk_label(score)
    pct = int(score * 100)
    r = 70
    circ = 2 * math.pi * r
    off = circ * (1 - score)
    st.markdown(f'<div style="text-align:center;padding:1rem 0;"><svg width="{size}" height="{size}" viewBox="0 0 200 200"><circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="12"/><circle cx="100" cy="100" r="{r}" fill="none" stroke="{color}" stroke-width="12" stroke-linecap="round" stroke-dasharray="{circ}" stroke-dashoffset="{off}" transform="rotate(-90 100 100)"/><text x="100" y="90" text-anchor="middle" font-family="Georgia,serif" font-size="36" fill="{color}">{pct}%</text><text x="100" y="115" text-anchor="middle" font-size="10" letter-spacing="2" fill="#64748b">{rl.upper()}</text></svg><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);margin-top:0.25rem;">{label}</div></div>', unsafe_allow_html=True)

def multi_ring(scores, size=200, label="Ensemble"):
    from utils.session import get_risk_color
    colors = {"handwriting": "#4f9cf9", "voice": "#a78bfa", "survey": "#22c55e"}
    radii = [75, 58, 41]
    rings = ""
    for i, (key, score) in enumerate(scores.items()):
        if i >= 3: break
        r = radii[i]; c = 2*math.pi*r; off = c*(1-score); col = colors.get(key, "#4f9cf9")
        rings += f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="8"/><circle cx="100" cy="100" r="{r}" fill="none" stroke="{col}" stroke-width="8" stroke-linecap="round" stroke-dasharray="{c}" stroke-dashoffset="{off}" transform="rotate(-90 100 100)"/>'
    avg = sum(scores.values()) / max(len(scores), 1)
    pct = int(avg * 100); color = get_risk_color(avg)
    st.markdown(f'<div style="text-align:center;padding:1rem 0;"><svg width="{size}" height="{size}" viewBox="0 0 200 200">{rings}<text x="100" y="96" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="{color}">{pct}%</text><text x="100" y="114" text-anchor="middle" font-size="9" letter-spacing="2" fill="#64748b">COMBINED</text></svg><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);margin-top:0.25rem;">{label}</div></div>', unsafe_allow_html=True)

def score_bars(scores, colors=None):
    dc = {"meander":"#4f9cf9","spiral":"#a78bfa","wave":"#22c55e","ahh":"#4f9cf9","vowels":"#a78bfa","text":"#f59e0b"}
    if colors is None: colors = dc
    for key, score in scores.items():
        pct = int(score * 100); c = colors.get(key, "#4f9cf9"); name = key.replace("_"," ").title()
        st.markdown(f'<div style="margin-bottom:0.85rem;"><div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;"><span style="font-size:0.82rem;color:var(--text);">{name}</span><span style="font-family:var(--font-mono);font-size:0.75rem;color:{c};">{pct}%</span></div><div class="nt-result-bar"><div class="nt-result-bar-fill" style="width:{pct}%;background:{c};"></div></div></div>', unsafe_allow_html=True)
