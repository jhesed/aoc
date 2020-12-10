"""Created by Jhesed Tacadena Dec 10, 2020.

Advent of Code Day 10: https://adventofcode.com/2020/day/10

Output:

Answer: 386869246296064
"""
from day10.common import ACCEPTABLE_DIFF


def generate_unique_key(joltage: int):
    """Simply generates a string of key to avoid collision with other numbers
    in e.g. the dictionary.

    :param joltage: e.g. 10
    :return: e.g. KEY10
    """
    return f"KEY{joltage}"


def count_number_of_ways(
    data: list,
    current_joltage: int,
    current_index: int,
    ways_info: dict,
    max_value: int,
) -> int:
    """Count possible number of ways in joltage list."""

    if current_joltage == max_value:
        return 1

    key = generate_unique_key(joltage=current_joltage)  # e.g. KEY123
    if key in ways_info:
        return ways_info[key]

    ways_counter = 0
    acceptable_joltages = []
    for joltage in data[current_index:]:
        if not (
            current_joltage < joltage <= (current_joltage + ACCEPTABLE_DIFF)
        ):
            # Our list is sorted, so once we get value > than this, next
            # values will also be the same
            break

        acceptable_joltages.append(joltage)

    for aj in acceptable_joltages:
        ways_counter += count_number_of_ways(
            data, aj, current_index + 1, ways_info, max_value
        )

    ways_info[key] = ways_counter
    return ways_counter


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = sorted([int(i) for i in _file.read().splitlines()])
        _max_value = max(_inputs)
        _ways_info = {}
        answer = count_number_of_ways(
            data=_inputs,
            current_joltage=0,
            current_index=0,
            ways_info=_ways_info,
            max_value=_max_value,
        )
        print(f"Answer: {answer}")
