from pathlib import Path

base = Path(__file__).parent
incoming = base / "incoming"
data = base / "data"

incoming.mkdir(exist_ok=True)
data.mkdir(exist_ok=True)

for name in ["test1.txt", "test2.txt", "test3.pdf", "notes.docx", "readme"]:
    (incoming / name).write_text("test", encoding="utf-8")

(data / "jobs.csv").write_text(
    "file,words,status\n"
    "invoice1.docx,1200,done\n"
    "api_guide.docx,3500,pending\n"
    "readme.docx,800,done\n",
    encoding="utf-8",
)

print("Test files ready.")