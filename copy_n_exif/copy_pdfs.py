import os
import re
import shutil
from pathlib import Path
from string import ascii_letters, digits

from rich import inspect, print
from unidecode import unidecode

# pip install Unidecode rich


def list_directory_files(directory):
    """list files in specified directory"""
    for filepath in Path(directory).glob("**/*"):
        if filepath.is_dir():
            continue
        yield filepath.absolute()


def sanitize_name(name):
    """sanitize file name by removing non ascii characters, and filling substrings with dashes

    https://stackoverflow.com/questions/3878555/how-to-replace-repeated-instances-of-a-character-with-a-single-instance-of-that
    """
    new_name = Path(unidecode(name))
    new_name_chars = [c if c in allowed_chars else "-" for c in new_name.stem]
    new_name = "".join(new_name_chars).strip("-") + new_name.suffix
    new_name = re.sub("\-\-+", "-", new_name)
    return new_name


if __name__ == "__main__":
    os.chdir(str(Path(__file__).parent))

    # ***** list pdf files *****
    directory = Path("pdf-files")
    files = list_directory_files(directory)
    pdf_files = filter(lambda item: item.name.endswith(".pdf"), files)
    unidecoded_directory = Path(directory.name + "-unidecoded")
    unidecoded_directory.mkdir(exist_ok=True)

    # ***** move to unidecoded directory *****
    allowed_chars = ascii_letters + digits
    for index, path in enumerate(pdf_files, start=1):
        new_name = sanitize_name(path.name)
        new_path = unidecoded_directory.joinpath(new_name)
        print(f"{index}) [yellow]{path.name}[/yellow] -> [cyan]{new_path.name}[/cyan]")
        shutil.copy2(path, new_path)
