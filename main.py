from pathlib import Path
from sorter import sort_files
from reader import read_pending_words
from reporter import write_report

def main():
    base = Path(__file__).parent

    log_path = base / "logs" / "log.csv"
    report_path = base / "reports" / "report.xlsx"

    moved = sort_files(base / "incoming", base, log_path)
    total = read_pending_words(base / "data" / "jobs.csv")
    write_report(report_path, total, len(moved))

    print(f"Done. Files sorted: {len(moved)}, words pending: {total}")

    
if __name__ == "__main__":
    main()
