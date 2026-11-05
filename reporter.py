from openpyxl import Workbook 

def write_report(report_path, total_words, files_sorted):
    report_path.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Report"

    ws.append(["Metric", "Value"])
    ws.append(["Words pending", total_words])
    ws.append(["Files sorted", files_sorted])

    wb.save(report_path)