"""Created by Jhesed Tacadena Dec 10, 2020.

Advent of Code Day 10: https://adventofcode.com/2020/day/10

Output:

Answer: 386869246296064
"""
import time

from day10.common import ACCEPTABLE_DIFF, generate_unique_key


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
    start_time = time.time()
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
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
