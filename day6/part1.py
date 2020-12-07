"""Created by Jhesed Tacadena Dec 05, 2020.

Advent of Code Day 5: https://adventofcode.com/2020/day/5

Output:
    6273
"""
import re
from functools import reduce


def count_unique_answers(inputs: list) -> int:
    """Counts unique answers from people."""
    return reduce(reduction_rule, inputs, 0)


def reduction_rule(current_total: int, current_line: str) -> int:
    """Counts unique answers in a group of people and sum them from another
    group of people.

    Logic:
        - Let current_line = bdmceunt
                             ubcdjqvnmte
                             mcgetfndul
                             dcenmtu
        - current_line.replace("\n", "") == 'bdmceuntubcdjqvnmtemcgetfnduldcenmtu'
        - list(...) == ['b', 'd', 'm', 'c', 'e', 'u', 'n', 't', 'u', 'b',
                        'c', 'd', 'j', 'q', 'v', 'n', 'm', 't', 'e', 'm',
                        'c', 'g', 'e', 't', 'f', 'n', 'd', 'u', 'l', 'd', 'c',
                        'e', 'n', 'm', 't', 'u']
        - set(...) == {'m', 'q', 'b', 'j', 'v', 'g', 'f', 'l', 'c', 'e',
                       'n', 't', 'u', 'd'}
        - len(...) == 14

    :param current_total: e.g. total of unique answers from previous batch
    of answers
    :param current_line: line to be processed today
    """
    return current_total + len(set(list(current_line.replace("\n", ""))))


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        blank_line_regex = r"(?:\r?\n){2,}"
        _inputs = re.split(blank_line_regex, _file.read().strip())
        answer = count_unique_answers(inputs=_inputs)
        print(f"Total: {answer}")
