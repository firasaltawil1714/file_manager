import csv

def read_pending_words(csv_path):
    if not csv_path.exists():
        print(f"Not found: {csv_path.name}")
        return 0

    total = 0

    with open(csv_path,encoding= "utf-8", newline="") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            print("CSV is empty")
            return 0

        for row in reader:
            if row.get("status").lower().strip() == "pending":
                total += int(row["words"])

    return total
