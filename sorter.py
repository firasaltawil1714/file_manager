import shutil
from logger import write_log

def sort_files(source, base, log_path):
    moved = []

    for file in source.glob("*"):
        if not file.is_file():  
            continue

        file_sh = file.suffix.lower()
        print(f"DEBUG: {file.name!r} suffix={file_sh!r}")
        if file_sh == ".txt":
            folder_name = "folder_txt"
        elif file_sh == ".pdf":
            folder_name = "folder_pdf"
        elif file_sh == ".docx":
            folder_name = "folder_docx"
        else:
            folder_name = "folder_other" 
        target = base / folder_name
        target.mkdir(exist_ok=True, parents=True)
        destination = target / file.name
        if destination.exists():
            print(f"File {file.name} already exists in {folder_name}. Skipping.")
            continue

        shutil.move(file, destination)
        print(f"Moved: {file.name} -> {folder_name}")
        moved.append(file.name)
        write_log(log_path, file.name, folder_name)

    return moved