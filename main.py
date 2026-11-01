from pathlib import Path
from sorter import sort_files
from reader import read_pending_words
from reporter import write_report
import sorter

def main():
    base = Path(__file__).parent

    moved = sort_files(base / "incoming", base)
    total = read_pending_words(base / "data" / "jobs.csv")
    write_report(base / "report.xlsx", total, len(moved))

    print(f"Done. Files sorted: {len(moved)}, words pending: {total}")

    print("USING:", sorter.__file__)
    
if __name__ == "__main__":
    main()
