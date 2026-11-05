import csv 
from datetime import datetime

def write_log(log_path, name, folder):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()

    with open(log_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "folder", "time"])

        if is_new:
            writer.writeheader()

        writer.writerow({
            "file": name,
            "folder":folder,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })    

# Test
# base = Path(__file__).parent
# write_log(base / "log.csv", "test1.txt", "folder_txt")
# write_log(base / "log.csv", "test3.pdf", "folder_pdf")  