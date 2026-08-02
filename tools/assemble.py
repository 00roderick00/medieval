#!/usr/bin/env python3
"""Assemble manuscript.md (book order, per-chapter endnote conversion) and
research/master-status.md (flag worklist) from the chapter drafts.
Run from the repo root: python3 tools/assemble.py
"""
import re, subprocess

ORDER = [("ch00-intro","Introduction — The Return Swing"),
 ("ch01","Chapter 1 — The Return of the Middle Ages"),
 ("ch02","Chapter 2 — The New Church"),
 ("ch03","Chapter 3 — Bastard Feudalism, Inc."),
 ("ch04","Chapter 4 — The Condottieri"),
 ("ch05","Chapter 5 — The Undermighty Kings"),
 ("ch06","Chapter 6 — 1450: The Year the Walls Fell"),
 ("ch07","Chapter 7 — Cade and the Communes"),
 ("ch08","Chapter 8 — Private Justice, Private War"),
 ("ch09","Chapter 9 — The King's Two Bodies, Broken"),
 ("ch10","Chapter 10 — The Artillery State"),
 ("ch11","Chapter 11 — The New Monarchies"),
 ("ch12","Chapter 12 — Not Modernity, But Tudor"),
 ("coda","Coda — A Note on Method and Sources")]

APPX = [("appendix-a","Appendix A — The Neomedievalism Literature, Annotated"),
 ("appendix-b","Appendix B — The Comparative Register"),
 ("appendix-c","Appendix C — Leading Indicators"),
 ("appendix-d","Appendix D — A Reader's Guide")]

TOKENS = ["Rogers","Curry","DeVries","Contamine","Vale","Pollard","Watts","Stevenson",
 "Gairdner","Escouchy","Blondel","Berry Herald","Chartier","Perroy","Depreter","Kriehn",
 "Kaminsky","Kadens","Johnson","Ross 2021","Lander","Edwards","Green 1874","Plowden",
 "Maitland","Cerny","Friedrichs","Kobrin","Bull","Baaz","Kelemen","Anderson","Ruggie",
 "Osiander","Teschke","Wilkinson","Pistor","Girardi","Fetzer","Margalit","Norris",
 "Green & Pahontu","Silver","Manza","Funke","Douenne","Ashcroft","Commynes","Giovio",
 "Heimpel","Bachrach","Vaughan","Bronk","Watling","Vershinin","Hammes","Kaplan",
 "Homer-Dixon","Holsinger","Rengger","Taylor","Collinson","Miller, Hoover","Özel",
 "Ekinci","Rot. Parl.","Golden Bull","DSA","DMA","GDPR","MiCA","EUR-Lex","GAO","OBR",
 "OECD","NAO","SEC","CRS ","CRS/","R48887","GSA","MHLW","Draghi","NATO","Pub. L.",
 "10-K","DEF 14A","UNCTAD","SIA/BCG","SIAC","ICC","LCIA","HKIAC","UNCITRAL","ICSID",
 "Oversight Board","Meta,","Apple,","World Bank","EU Tax Observatory","Statistics Bureau",
 "Wagner","ISW","RUSI","CSIS","ISIS,","Ukrainian Air Force","Zelensky","Shmyhal",
 "Syrskyi","Kostenko","NYT","Politico","Guardian","Reuters","FT,","Economist",
 "Military.com","Defense One","army.mil","Tudor Chamber Books","Landesarchiv","DHI",
 "Britannica","N.D. Cal","9th Cir","F.4th","CJEU","Irish DPC","Commission","NPC",
 "Qiushi","White House","arXiv","EBSCO","McDowell","TrendForce","Epoch","Stanford",
 "McSheffrey","Avalon","GHDI","Fordham","Vickers","Kleineke","Lunenfeld","punctum",
 "Bloomberg","CNBC","The Information","WSJ","DoD","DOT&E","CENTCOM","Herodote"]

def is_cite(par):
    inner = par[1:-1]
    if inner.startswith("r. ") or re.fullmatch(r"[0-9–\-— ,c\.~%$€£a-z]*", inner):
        return False
    return any(tok in inner for tok in TOKENS)

def convert(body, chap):
    notes=[]
    def repl(m):
        par=m.group(0)
        if not is_cite(par): return par
        notes.append(par[1:-1])
        return f"[^{chap}-{len(notes)}]"
    out=re.sub(r"\([^()]{4,400}\)", repl, body)
    return out, notes

def extract_body(path):
    t=open(path).read()
    m=re.search(r"\n---\n", t)
    start=m.end() if m else 0
    for pat in [r"\n---\n\n\*Draft ends", r"\n---\n\n\*Assembled", r"\n## Revisions \(post-review", r"\nSTATUS:"]:
        mm=re.search(pat, t[start:])
        if mm: return t[start:start+mm.start()]
    return t[start:]

def build_manuscript():
    parts=["# The Artillery State\n## Cannon, Code, and the Return of the Consolidator\n\n"
    "*Assembled manuscript — regenerate with tools/assemble.py. Working flags ([GAP], "
    "[TRANS. CLAUDE], [RE-CHECK AT PRESS], [BRIDGE], [BOOK'S ARGUMENT], [ANALOGY-ONLY]) are "
    "left visible by design; the master worklist is research/master-status.md. Author–date "
    "citations converted to per-chapter endnotes; date-only parentheticals remain inline.*\n"]
    total=0
    for i,(folder,title) in enumerate(ORDER):
        body=extract_body(f"{folder}/draft.md")
        body,notes=convert(body, i)
        total+=len(notes)
        parts.append(f"\n\n---\n\n# {title}\n{body}")
        if notes:
            parts.append("\n\n#### Notes\n")
            for j,n in enumerate(notes,1):
                parts.append(f"[^{i}-{j}]: {n}\n")
    for folder,title in APPX:
        t=open(f"{folder}/appendix.md").read()
        m=re.search(r"\n---\n", t); start=m.end() if m else 0
        mm=re.search(r"\nSTATUS:", t[start:])
        body=t[start:start+mm.start()] if mm else t[start:]
        parts.append(f"\n\n---\n\n# {title}\n{body}")
    open("manuscript.md","w").write("".join(parts))
    return total

def build_status():
    FILES = [("Intro","ch00-intro/draft.md")]+[(f"Ch{i}",f"ch{i:02d}/draft.md") for i in range(1,13)]+\
            [("Coda","coda/draft.md"),("App C","appendix-c/appendix.md")]
    rows=[]
    for ch,path in FILES:
        t=open(path).read()
        for m in re.finditer(r"\[(GAP[^\]]*|TRANS\. CLAUDE|RE-CHECK AT PRESS[^\]]*|BRIDGE[^\]]*)\]", t):
            if "*Draft ends" in t[:m.start()]: continue
            flag=m.group(1)
            kind=("GAP" if flag.startswith("GAP") else "TRANS. CLAUDE" if flag.startswith("TRANS")
                  else "RE-CHECK AT PRESS" if flag.startswith("RE-CHECK") else "BRIDGE")
            pre=" ".join(t[max(0,m.start()-110):m.start()].split())[-90:]
            detail=" ".join(flag.split())
            if len(detail)>110: detail=detail[:107]+"…"
            secs=[s for s in re.finditer(r"(?m)^## ([IVX]+)\.", t[:m.start()])]
            sec=secs[-1].group(1) if secs else "—"
            rows.append((ch,sec,kind,detail,pre))
    counts={}
    for r in rows: counts[r[2]]=counts.get(r[2],0)+1
    out=["# Master Status Report — Rewrite Worklist\n",
    f"\n*Regenerated by tools/assemble.py. {len(rows)} flags: "
    +", ".join(f"{v} {k}" for k,v in sorted(counts.items()))
    +". Ordered by chapter; § = draft section; footer voice-ledgers excluded; [END BRIDGE] not counted.*\n\n",
    "| Ch. | § | Flag | Flag detail | Context (preceding text) |\n|---|---|---|---|---|\n"]
    for ch,sec,kind,detail,pre in rows:
        out.append(f"| {ch} | {sec} | {kind} | {detail.replace('|',chr(92)+'|')} | …{pre.replace('|',chr(92)+'|')} |\n")
    out.append("""
## Standing items not flagged inline

- **Browser pulls (blocked at fetch, ch12 sources.md):** the Jeddah joint
  statement verbatim; the Section 232 semiconductor tariff instrument;
  the CRS R48887 original PDF (integrated from the EveryCRSReport mirror).
- **Acquisition list:** see retrieval-master.md (authoritative) — the
  gated spine works named in each chapter's footer.
- **Perplexity second-opinion runs:** reserved in every critiques.md; none
  yet run against the drafts.
- **Word-count deltas:** every chapter runs below its outline weight; the
  expansion path is the acquisition list plus the [BRIDGE] and voice
  passes (see each draft footer).
""")
    open("research/master-status.md","w").write("".join(out))
    return len(rows), counts

if __name__=="__main__":
    n=build_manuscript()
    r,c=build_status()
    wc=subprocess.run(["wc","-w","manuscript.md"],capture_output=True,text=True).stdout.strip()
    print(f"manuscript: {wc}; endnotes: {n}; flags: {r} {c}")
