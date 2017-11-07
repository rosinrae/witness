#! /bin/env python3


# lhx?

from datetime import date
from os import path, makedirs
from argparse import ArgumentParser


TITLEFORMAT = "%Y-%m-%d.txt"       # strftime formatting
ENTRY_DIR = "/home/brynr/journal"  # must be absolute


def make_title():
    """Produces a title for the journal entry file"""
    return date.today().strftime(TITLEFORMAT)


def parse_args():
    """Parses out arguments. Really must find a way to abstract this."""
    arg = ArgumentParser()
    arg.add_argument("text", nargs='*', help="text to record")
    return arg.parse_args()


def main():
    """Main function. Does the work."""

    # Parse arguments out
    args = parse_args()

    # Generate fully resolved name for entry
    entry = path.join(ENTRY_DIR, make_title())

    # Ensure that our journalling dir exists
    makedirs(ENTRY_DIR, exist_ok="true")

    # Put together line
    line = " ".join(args.text) + '\n'

    # write!
    with open(entry, 'a', encoding="UTF-8") as outfile:
        outfile.write(line)


if __name__ == "__main__":
    main()
