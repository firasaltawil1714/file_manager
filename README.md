# file_manager
A small project I built while learning automation.
It sorts files into folders by type, reads a CSV file of translation jobs,
and writes a short Excel report.
## What it does
1. Takes the files in `incoming/` and moves them into folders by extension:
   `folder_txt`, `folder_pdf`, `folder_docx`, and `folder_other` for anything else.
   If a file with the same name is already in the target folder, it skips it.
2. Reads `data/jobs.csv` and adds up the words of the jobs marked `pending`.
3. Saves the result in `report.xlsx` (words pending and number of files sorted).

## Project structure

- `main.py` - runs everything in order
- `sorter.py` - moves the files
- `reader.py` - reads the CSV
- `reporter.py` - writes the Excel report
- `make_test_files.py` - creates test files so I can run it again and again

## How to run

    pip install openpyxl
    python make_test_files.py
    python main.py
