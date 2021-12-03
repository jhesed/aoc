"""Created by Jhesed Tacadena Dec 10, 2020.

Advent of Code Day 10: https://adventofcode.com/2020/day/10

Output:

Answer: 386869246296064

# TODO: Unfinished yet. Refer to part2_recursive.py for now
"""
import time

from day10.common import ACCEPTABLE_DIFF


def count_number_of_ways(inputs: list) -> int:
    number_of_ways = {}
    for index, current_number in enumerate(inputs):

        if current_number not in number_of_ways:
            number_of_ways[current_number] = []

        allowed_values = (
            current_number + i for i in range(1, ACCEPTABLE_DIFF + 1)
        )

        for next_number in inputs[index + 1 :]:
            if next_number not in allowed_values:
                # Our list is sorted, so once we get value > than this, next
                # values will also be the same
                break
            number_of_ways[current_number].append(next_number)

    # TODO: (unfinished)
    counter = 1
    print(number_of_ways)
    for parent, children in number_of_ways.items():
        if children:
            counter *= len(children)
    print(counter)


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        _inputs = sorted([int(i) for i in _file.read().splitlines()])
        answer = count_number_of_ways(inputs=_inputs)
        print(f"Answer: {answer}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
