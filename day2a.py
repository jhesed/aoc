"""
    Created by Jhesed Tacadena Dec 01, 2020

    Advent of Code Day 2: https://adventofcode.com/2020/day/2
"""


def count_valid_passwords(inputs: list) -> int:
    """ Counts valid password based on rules"""
    counter = 0
    for line in inputs:
        rule, character, password = line.split()
        min_occurrence, max_occurrence = rule.split("-")
        min_occurrence = int(min_occurrence)
        max_occurrence = int(max_occurrence)
        character = character.replace(":", "")
        if min_occurrence <= password.count(character) <= max_occurrence:
            counter += 1

    return counter


if __name__ == "__main__":
    with open("data/day2.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        print(f"ANSWER: {count_valid_passwords(inputs=_inputs)}")
