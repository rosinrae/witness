#! /bin/env python2
"""A simple command line journaling application"""


# lhx?

from __future__ import print_function
from datetime import date
from os import path, makedirs
from argparse import ArgumentParser


TITLEFORMAT = "%Y-%m-%d.txt"              # strftime formatting
ENTRY_DIR = path.expanduser("~/journal")  # may use ~ for user dir elision


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
    entry = path.join(path.expanduser(ENTRY_DIR), make_title())

    # Ensure that our journalling dir exists
    if not path.exists(ENTRY_DIR):
        makedirs(ENTRY_DIR)

    if len(args.text) > 0:
        # Put together line
        line = " ".join(args.text)

        # write!
        with open(entry, 'a') as outfile:
            outfile.write(line)
            outfile.write('\n')

    elif path.isfile(entry):
        with open(entry) as outfile:
            print(outfile.read(), end="")


if __name__ == "__main__":
    main()
