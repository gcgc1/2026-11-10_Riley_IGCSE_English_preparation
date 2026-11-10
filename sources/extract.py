import pypdf, sys
r = pypdf.PdfReader(r".\sources\0500-syllabus-2027-2029.pdf")
out = []
for i, p in enumerate(r.pages):
    out.append(f"\n===== PAGE {i+1} =====\n" + (p.extract_text() or ""))
open(r".\sources\0500-syllabus-2027-2029.txt","w",encoding="utf-8").write("".join(out))
print(len(r.pages), "pages")
