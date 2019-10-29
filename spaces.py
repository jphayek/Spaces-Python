#Prend en parametre un dossier et remplace dans ce dossier tous les noms des fichiers contenant des espace en underscore.
import argparse
from pathlib import Path

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


def main():
    args = parse_args()
    files = [
        file
        for file in Path(args.path).glob("*" if not args.recurse else "**/*")
        if file.is_file()
    ]
    for file in files:
        new_name = file.name.replace(args.search, args.replace)
        file.rename(file.parent / new_name)


main()