import json
import os
import subprocess
from pathlib import Path

from rich import print

# pip install rich


def list_directory_files(directory):
    """list files in specified directory"""
    for filepath in Path(directory).glob("**/*"):
        if filepath.is_dir():
            continue
        yield filepath.absolute()


def write_json(filename, data):
    """write to json file"""
    with open(filename, "w", encoding="utf-8") as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True


if __name__ == "__main__":
    os.chdir(str(Path(__file__).parent))

    # **** iterate over files ****
    data = []
    directory = "pdf-files-unidecoded"
    files = list_directory_files(directory=directory)
    for index, path in enumerate(files, start=1):
        command = f"exiftool {path}"
        print(f"{index}) command: [green]{command}[/green]\n")

        # **** use exiftool ****
        try:
            response = subprocess.check_output(command, timeout=10)
            response = response.decode("utf-8")
            parsed = {
                key.strip(): value.strip()
                for key, value in (line.split(":", 1) for line in response.splitlines())
            }
            data.append(parsed)
            print(response)
            print()
        except subprocess.CalledProcessError as err:
            print(err)
            print()
        except KeyboardInterrupt:
            print()
            continue

    # **** write to json file ****
    output = f"{directory}-exif.json"
    write_json(filename=output, data=data)
    print(f"saved to: [cyan]{output}[/cyan]")
