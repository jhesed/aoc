"""Created by Jhesed Tacadena Dec 13, 2020.

Advent of Code Day 13: https://adventofcode.com/2020/day/13

Output:
    Thank God I found you 471793476184394
    Elapsed time (seconds): 0.0
"""
import time
from collections import OrderedDict
from functools import reduce
from math import gcd

EXCLUDE = "x"


def compute_lcm(numbers: list) -> int:
    """
    Computes LCM of multiple numbers.
    # TODO: Turns out I only need to support 2 numbers;
    #       But this initial version supports multiple numbers
    """
    return reduce(
        lambda previous_number, next_number: previous_number
        * next_number
        // gcd(previous_number, next_number),
        numbers,
    )


def find_earliest_timestamp(inputs: list) -> int:
    """Finds the earliest timestamp such that all of the listed
    bus IDs depart at
    offsets matching their positions in the list."""

    # Get bus numbers
    bus_numbers = inputs[1].split(",")
    print(f"bus numbers: {bus_numbers}")

    # Get offset of bus numbers
    offsets = OrderedDict(
        {
            bus_number: bus_numbers.index(bus_number)
            for bus_number in bus_numbers
            if bus_number != EXCLUDE
        }
    )
    print(f"offsets: {offsets}")

    # Exclude "x" from bus numbers
    valid_bus_numbers = [
        int(bus_number) for bus_number in bus_numbers if bus_number != EXCLUDE
    ]

    current_index = 0
    increment = valid_bus_numbers[0]
    for bus_number in valid_bus_numbers[1:]:
        while True:
            offset = int(offsets[str(bus_number)])
            current_index += increment
            if (current_index + offset) % bus_number == 0:
                break
        increment = compute_lcm(numbers=[increment, bus_number])

    print(f"Thank God I found you {current_index}")
    return current_index


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        answer = find_earliest_timestamp(inputs=_file.read().splitlines())
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
