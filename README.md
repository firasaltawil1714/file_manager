# file_manager
A small project I built while learning automation.
It sorts files into folders by type, reads a CSV file of translation jobs,
and writes a short Excel report.
## What it does
1. Takes the files in `incoming/` and moves them to folders by extension: `folder_txt`, `folder_pdf`, `folder_docx`. Anything else goes to `folder_other`.
2. If a file with the same name is already in the target folder, it skips it.
3. Writes every moved file (name, folder, time) to `logs/log.csv`.
4. Reads `data/jobs.csv` and adds up the words of the jobs marked `pending`.
5. Saves the result in `reports/report.xlsx`.

## Project structure

- `main.py` runs everything in order
- `sorter.py` moves the files
- `logger.py` writes the log
- `reader.py` reads the CSV
- `reporter.py` writes the Excel report
- `make_test_files.py` creates test files, so the project can be run again and again

## How to run

    pip install openpyxl
    python make_test_files.py
    python main.py
## Ideas for later

- Run it automatically on a schedule
- Send the report by email