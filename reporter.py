from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font 

def write_report(report_path, total_words, files_sorted):
    report_path.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"

    
    ws.append(["Metric", "Value"])
    ws.append(["Report date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    ws.append(["Files sorted", files_sorted])
    ws.append(["Words pending", total_words])

    for cell in ws[1]:
        cell.font = Font(bold=True)

    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 22

    wb.save(report_path)