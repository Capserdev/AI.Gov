import streamlit as st
from components.cards import section_header, divider, info_card
from components.charts import risk_ring, multi_ring
from core.report_engine import compute_handwriting_ensemble, compute_voice_ensemble, compute_combined_score, get_modality_breakdown
from utils.session import get_risk_color, get_risk_label

def render():
    section_header("My Report","Unified risk assessment combining all diagnostic modalities.")
    hw = compute_handwriting_ensemble(st.session_state.get("handwriting_results",{})) or None
    vc = compute_voice_ensemble(st.session_state.get("voice_results",{})) or None
    sv = st.session_state.get("survey_score")
    if not any([hw,vc,sv]):
        st.markdown('<div class="nt-card-static" style="text-align:center;padding:3rem 1.5rem;"><div style="font-family:var(--font-display);font-size:1.3rem;color:var(--text);margin-bottom:0.75rem;">No data yet</div><div style="font-size:0.88rem;color:var(--text-secondary);">Complete at least one analysis to generate your report.</div></div>', unsafe_allow_html=True)
        return
    combined = compute_combined_score(hw,vc,sv); breakdown = get_modality_breakdown(hw,vc,sv)
    st.session_state["combined_score"] = combined
    c1,c2 = st.columns(2)
    with c1: multi_ring(breakdown,220,"Combined Assessment") if len(breakdown)>1 else risk_ring(combined,220,"Overall Risk")
    with c2:
        clr=get_risk_color(combined); lbl=get_risk_label(combined)
        st.markdown(f'<div style="padding:1.5rem 0;"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted);margin-bottom:0.5rem;">UNIFIED RISK ASSESSMENT</div><div style="font-family:var(--font-display);font-size:2.2rem;color:{clr};margin-bottom:0.25rem;">{int(combined*100)}%</div><div style="font-size:1rem;color:{clr};margin-bottom:1rem;">{lbl}</div></div>', unsafe_allow_html=True)
        info = {"handwriting":("Handwriting","#4f9cf9","40%"),"voice":("Voice","#a78bfa","35%"),"survey":("Survey","#22c55e","25%")}
        for k,v in breakdown.items():
            n,c,w = info.get(k,(k,"#4f9cf9","—"))
            st.markdown(f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;"><span style="width:10px;height:10px;border-radius:50%;background:{c};flex-shrink:0;"></span><span style="font-size:0.82rem;color:var(--text);flex:1;">{n}</span><span style="font-family:var(--font-mono);font-size:0.75rem;color:{c};">{int(v*100)}%</span><span style="font-family:var(--font-mono);font-size:0.6rem;color:var(--text-muted);">w={w}</span></div>', unsafe_allow_html=True)
    divider(); section_header("Modality Breakdown")
    c1,c2,c3 = st.columns(3)
    with c1: info_card("HANDWRITING", f"Score: {int(hw*100)}%" if hw else "No drawings uploaded.","#4f9cf9")
    with c2: info_card("VOICE", f"Score: {int(vc*100)}%" if vc else "No recordings uploaded.","#a78bfa")
    with c3: info_card("SURVEY", f"Score: {int(sv*100)}%" if sv else "Survey not completed.","#22c55e")
    divider()
    st.markdown('<div class="nt-card-static" style="border-left:3px solid var(--amber);"><div style="font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--amber);margin-bottom:0.5rem;">MEDICAL DISCLAIMER</div><div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.6;">NeuroTrace is a research screening tool and is <strong>not</strong> a substitute for professional medical diagnosis. Results should be discussed with a qualified healthcare provider.</div></div>', unsafe_allow_html=True)
