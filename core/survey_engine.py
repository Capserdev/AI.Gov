QUESTIONS = [
    {"id":"tremor","text":"Do you experience involuntary shaking or tremor in your hands at rest?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":1.0,"category":"Motor Symptoms"},
    {"id":"handwriting","text":"Has your handwriting become noticeably smaller or more cramped over time?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.9,"category":"Motor Symptoms"},
    {"id":"voice_change","text":"Have others told you your voice has become softer, hoarse, or monotone?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.85,"category":"Motor Symptoms"},
    {"id":"balance","text":"Do you experience difficulty with balance or a tendency to shuffle your feet?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.9,"category":"Motor Symptoms"},
    {"id":"stiffness","text":"Do you feel unusual stiffness in your limbs that does not go away with movement?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.85,"category":"Motor Symptoms"},
    {"id":"smell","text":"Have you noticed a reduced sense of smell or difficulty identifying common scents?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.7,"category":"Non-Motor Symptoms"},
    {"id":"sleep","text":"Do you act out your dreams while sleeping (kicking, punching, yelling)?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.8,"category":"Non-Motor Symptoms"},
    {"id":"constipation","text":"Do you experience chronic constipation without a clear dietary cause?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.5,"category":"Non-Motor Symptoms"},
    {"id":"depression","text":"Have you experienced persistent feelings of depression or anxiety that are new?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.5,"category":"Non-Motor Symptoms"},
    {"id":"dizziness","text":"Do you feel dizzy or lightheaded when standing up?","type":"likert","options":["Never","Rarely","Sometimes","Often","Very Often"],"weight":0.45,"category":"Non-Motor Symptoms"},
    {"id":"family_history","text":"Do you have a first-degree relative diagnosed with Parkinson's disease?","type":"yesno","weight":0.7,"category":"Risk Factors"},
    {"id":"age","text":"What is your age range?","type":"select","options":["Under 40","40-49","50-59","60-69","70-79","80+"],"weight":0.6,"category":"Risk Factors"},
]

def compute_survey_score(answers):
    tw = ws = 0.0
    for q in QUESTIONS:
        qid = q["id"]
        if qid not in answers: continue
        a = answers[qid]; w = q["weight"]; tw += w
        if q["type"] == "likert":
            opts = q["options"]
            ws += (opts.index(a) / max(len(opts)-1,1)) * w if a in opts else 0
        elif q["type"] == "yesno":
            ws += (1.0 if a == "Yes" else 0.0) * w
        elif q["type"] == "select" and qid == "age":
            ws += {"Under 40":0.05,"40-49":0.15,"50-59":0.35,"60-69":0.60,"70-79":0.80,"80+":0.95}.get(a,0) * w
    return round(ws/tw, 4) if tw else 0.0

def get_answered_count(answers):
    return len([k for k in answers if answers[k] is not None])
