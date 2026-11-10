import pypdf, glob, os
for f in glob.glob(r".\sources\*.pdf"):
    out = f[:-4] + ".txt"
    r = pypdf.PdfReader(f)
    parts = []
    for i, p in enumerate(r.pages):
        parts.append(f"\n===== PAGE {i+1} =====\n" + (p.extract_text() or ""))
    open(out, "w", encoding="utf-8").write("".join(parts))
    print(os.path.basename(out), len(r.pages), "pages")
