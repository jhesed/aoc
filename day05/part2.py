"""Created by Jhesed Tacadena Dec 05, 2020.

Advent of Code Day 5: https://adventofcode.com/2020/day/5

Output:
    My Seat ID: 696
    Maximum Seat ID: 938
"""
from math import ceil, floor

# Constants

MIN_ROW = 0
MAX_ROW = 127

MIN_COL = 0
MAX_COL = 7

MULTIPLIER = 8
OFFSET = 70


def find_seat_ids(inputs: list) -> list:
    """Returns all seat ids given input."""

    seat_ids = []

    for line in inputs:
        current_row = [MIN_ROW, MAX_ROW]
        current_column = [MIN_COL, MAX_COL]

        for char in line:

            if char == "F":
                current_row[1] = floor((current_row[0] + current_row[1]) / 2)
            elif char == "B":
                current_row[0] = ceil((current_row[0] + current_row[1]) / 2)
            elif char == "L":
                current_column[1] = floor(
                    (current_column[0] + current_column[1]) / 2
                )
            elif char == "R":
                current_column[0] = ceil(
                    (current_column[0] + current_column[1]) / 2
                )

        current_seat_id = current_row[0] * MULTIPLIER + current_column[0]
        seat_ids.append(current_seat_id)

    return seat_ids


def find_missing_seat_id(seat_ids: list) -> int:
    """Retrieves missing seat id from seat_ids."""
    print(seat_ids)
    for index, value in enumerate(seat_ids):
        if value != (missing_seat_id := index + OFFSET):
            return missing_seat_id

    # Nothing is missing in list
    return -1


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        all_seat_ids = find_seat_ids(inputs=_inputs)
        sorted_seat_ids = sorted(all_seat_ids)
        max_seat_id = sorted_seat_ids[-1]
        missing_seat_id = find_missing_seat_id(seat_ids=sorted_seat_ids)

        print(f"Max Seat ID: {max_seat_id}")
        print(f"Missing (my) Seat ID: {missing_seat_id}")
