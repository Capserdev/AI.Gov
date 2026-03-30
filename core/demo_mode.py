import hashlib

def _seed(s, lo=0.25, hi=0.85):
    h = int(hashlib.md5(s.encode()).hexdigest()[:8], 16)
    return lo + (h % 1000) / 1000.0 * (hi - lo)

def demo_handwriting_predict(model, filename):
    return round(_seed(f"hw_{model}_{filename}", 0.15, 0.75), 4)

def demo_voice_binary_predict(task, filename):
    return round(_seed(f"voice_{task}_{filename}", 0.20, 0.70), 4)

def demo_voice_4class_predict(filename):
    hc=_seed(filename+"_hc",0.10,0.50); pd=_seed(filename+"_pd",0.15,0.55)
    psp=_seed(filename+"_psp",0.05,0.25); msa=_seed(filename+"_msa",0.05,0.20)
    t=hc+pd+psp+msa
    return {"Healthy Control":round(hc/t,4),"Parkinson's Disease":round(pd/t,4),"PSP":round(psp/t,4),"MSA":round(msa/t,4)}
