"""Created by Jhesed Tacadena Dec 10, 2020.

Advent of Code Day 10: https://adventofcode.com/2020/day/10

Output:

Answer: 386869246296064
"""
from day10.common import ACCEPTABLE_DIFF


def generate_unique_key(joltage: int):
    """Simply generates a string of key to avoid collision with other
    numbers."""
    return f"KEY{joltage}"


def count_number_of_ways(
    data: list, current_joltage: int, current_index: int, info: dict
) -> int:
    """Count possible number of ways allowed in rule."""

    if current_joltage == max(data):
        return 1

    key = generate_unique_key(joltage=current_joltage)  # e.g. KEY123
    if key in info:
        return info[key]

    ways_counter = 0
    acceptable_joltages = [
        i
        for i in data
        if current_joltage < i <= (current_joltage + ACCEPTABLE_DIFF)
    ]
    for aj in acceptable_joltages:
        ways_counter += count_number_of_ways(data, aj, current_index + 1, info)

    info[key] = ways_counter
    return ways_counter


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = sorted([int(i) for i in _file.read().splitlines()])
        answer = count_number_of_ways(
            data=_inputs, current_joltage=0, current_index=0, info={}
        )
        print(f"Answer: {answer}")
