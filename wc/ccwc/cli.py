import sys
from io import TextIOWrapper
from pathlib import Path
from typing import List, TextIO, Union

import click


def _count_fileinput(
    f: Union[TextIO, TextIOWrapper],
    filename: Path,
    count: bool,
    lines: bool,
    words: bool,
    m: bool,
) -> List[int]:
    values = []

    line_counts = 0
    word_counts = 0
    byte_counts = 0
    char_counts = 0

    for line in f:
        if lines:
            line_counts += 1

        if words:
            word_counts += len(line.split())

        if count:
            byte_counts += len(line.encode()) + int(filename is not None)

        if m:
            char_counts += len(line) + 1

    if lines:
        values.append(line_counts)

    if words:
        values.append(word_counts)

    if m:
        values.append(char_counts)

    if count:
        values.append(byte_counts)

    return values


@click.command()
@click.argument(
    "filename",
    type=click.Path(exists=True, path_type=Path),
    required=False,
    default=None,
)
@click.option(
    "-c",
    "--count",
    is_flag=True,
    help="Count the number of bytes in the file",
    default=None,
)
@click.option(
    "-l",
    "--lines",
    is_flag=True,
    help="Count the number of lines in the file",
    default=None,
)
@click.option(
    "-w",
    "--words",
    is_flag=True,
    help="Count the number of words in the file",
    default=None,
)
@click.option(
    "-m",
    is_flag=True,
    help="Count the number of characters in the file (supports multibyte characters)",
    default=None,
)
def main(filename: Path, count: bool, lines: bool, words: bool, m: bool):
    if sys.stdin.isatty() and not filename.exists():
        filename = None

    if all(flag is None for flag in [count, lines, words, m]):
        count = True
        lines = True
        words = True

    values = []

    if filename:
        with filename.open() as f:
            values = _count_fileinput(f, filename, count, lines, words, m)
    else:
        values = _count_fileinput(sys.stdin, None, count, lines, words, m)

    value_str = " ".join([f"{value:8}" for value in values])

    print(f"{value_str} {filename.name if filename else ''}")
