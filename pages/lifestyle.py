import streamlit as st
from components.cards import section_header, divider
from components.charts import risk_ring
from core.survey_engine import QUESTIONS, compute_survey_score, get_answered_count

def render():
    section_header("Lifestyle Survey","Clinically-validated questionnaire assessing motor symptoms, non-motor indicators, and risk factors.")
    if "survey_answers" not in st.session_state: st.session_state["survey_answers"] = {}
    ans = st.session_state["survey_answers"]
    total = len(QUESTIONS); answered = get_answered_count(ans)
    st.progress(answered/total if total else 0)
    st.markdown(f'<div style="font-family:var(--font-mono);font-size:0.65rem;letter-spacing:0.1em;color:var(--text-muted);margin-bottom:1.5rem;text-align:right;">{answered} / {total} COMPLETED</div>', unsafe_allow_html=True)
    cats = {}
    for q in QUESTIONS:
        cats.setdefault(q["category"],[]).append(q)
    for cat,qs in cats.items():
        st.markdown(f'<div style="font-family:var(--font-mono);font-size:0.65rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);margin:1.5rem 0 0.75rem 0;">{cat}</div>', unsafe_allow_html=True)
        for q in qs:
            qid = q["id"]
            st.markdown(f'<div class="nt-card-static" style="margin-bottom:0.5rem;padding:1.25rem;"><div style="font-size:0.9rem;color:var(--text);line-height:1.55;margin-bottom:0.75rem;">{q["text"]}</div></div>', unsafe_allow_html=True)
            if q["type"] == "likert":
                cur = ans.get(qid); idx = q["options"].index(cur) if cur in q["options"] else 0
                ans[qid] = st.radio(q["text"], q["options"], index=idx, key=f"s_{qid}", horizontal=True, label_visibility="collapsed")
            elif q["type"] == "yesno":
                cur = ans.get(qid,"No")
                ans[qid] = st.radio(q["text"], ["No","Yes"], index=1 if cur=="Yes" else 0, key=f"s_{qid}", horizontal=True, label_visibility="collapsed")
            elif q["type"] == "select":
                cur = ans.get(qid); opts = q["options"]; idx = opts.index(cur) if cur in opts else 0
                ans[qid] = st.selectbox(q["text"], opts, index=idx, key=f"s_{qid}", label_visibility="collapsed")
    st.session_state["survey_answers"] = ans
    divider()
    score = compute_survey_score(ans); st.session_state["survey_score"] = score
    section_header("Survey Risk Assessment")
    c1,c2 = st.columns([1,2])
    with c1: risk_ring(score, label="Survey Risk")
    with c2:
        from utils.session import get_risk_label, get_risk_color
        lbl=get_risk_label(score); clr=get_risk_color(score)
        st.markdown(f'<div style="padding:1rem 0;"><div style="font-family:var(--font-display);font-size:1.5rem;color:{clr};margin-bottom:0.5rem;">{lbl}</div><div style="font-size:0.88rem;color:var(--text-secondary);line-height:1.65;">Based on your responses, your lifestyle risk factor score is <strong>{int(score*100)}%</strong>. This score reflects self-reported symptoms and should be interpreted alongside the handwriting and voice analyses.</div></div>', unsafe_allow_html=True)
