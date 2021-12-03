"""Created by Jhesed Tacadena Dec 05, 2020.

Advent of Code Day 5: https://adventofcode.com/2020/day/5

Output:
    3254
"""
import re
from functools import reduce


def count_unique_answers(inputs: list) -> int:
    """Counts unique answers from people."""
    return reduce(count_total_same_answers, inputs, 0)


def count_total_same_answers(current_total: int, current_line: str) -> int:
    """Counts total number of same answers for all groups. Refer to part1 for
    more sample.

    :param current_total: e.g. total of unique answers from previous batch
    of answers
    :param current_line: line to be processed today
    """
    return current_total + len(
        reduce(count_same_answers_per_group, current_line.split())
    )


def count_same_answers_per_group(
    previous_answer: str, current_answer: str
) -> set:
    """
        Logic:
        - Let previous_answer = 'bdmceunt'
        - Let current_answer = 'ubcdjqvnmte'
        - set(previous_answer) == {'n', 'u', 'j', 'q', 'b', 'v', 'c',
                                   'm', 'e', 't', 'd'}
        - set(current_answer) == {'n', 'u', 'b', 'm', 'e', 'c', 't', 'd'}
        - (...).intersection(...) == {'n', 'u', 'b', 'c', 'e', 'd', 't', 'm'}

    :param previous_answer: answer from previous person in same group
    :param current_answer: answer from current person in same group
    """

    return set(current_answer).intersection(set(previous_answer))


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        blank_line_regex = r"(?:\r?\n){2,}"
        _inputs = re.split(blank_line_regex, _file.read().strip())
        answer = count_unique_answers(inputs=_inputs)
        print(f"Total: {answer}")
