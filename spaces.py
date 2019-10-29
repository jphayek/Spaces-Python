"Prend en parametre un dossier et remplace dans ce dossier tous les noms des fichiers contenant des espace en underscore."
import argparse
from pathlib import Path

__version__ = "0.0.1"


def parse_args():
    parser = argparse.ArgumentParser(description="Searches and replaces in filenames.")
    parser.add_argument("path", help="Root directory in which to search for files.")
    parser.add_argument("--search", default=" ", help="Character to search.")
    parser.add_argument(
        "--replace", default="_", help="Character to use as a replacement."
    )
    parser.add_argument(
        "--recurse",
        action="store_true",
        help="Give to replace recursively in directories.",
    )

    return parser.parse_args()


def fix_names(path, search=" ", replace="_", recurse=False):
    files = [
        file
        for file in Path(path).glob("*" if not recurse else "**/*")
        if file.is_file()
    ]
    for file in files:
        new_name = file.name.replace(search, replace)
        file.rename(file.parent / new_name)


def main():
    args = parse_args()
    fix_names(args.path, args.search, args.replace, args.recurse)


if __name__ == "__main__":
    main()