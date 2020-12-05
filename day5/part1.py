"""Created by Jhesed Tacadena Dec 05, 2020.

Advent of Code Day 5: https://adventofcode.com/2020/day/5

Output:
"""
from math import floor, ceil

MIN_ROW = 0
MAX_ROW = 127

MIN_RL = 0
MAX_RL = 7

MULTIPLIER = 8


def count_x(inputs: list) -> int:
    """Counts x """

    seat_ids = []
    max_current_seat_id = 0
    max_row = []
    max_rl = []

    for j, line in enumerate(inputs):

        current_row = [MIN_ROW, MAX_ROW]
        current_rl = [MIN_RL, MAX_RL]
        current_seat_id = 0

        for i, char in enumerate(line):
            if char == "F":
                current_row[1] = floor((current_row[0] + current_row[1]) / 2)
            elif char == "B":
                current_row[0] = ceil((current_row[0] + current_row[1]) / 2)

            if char == "L":
                current_rl[1] = floor((current_rl[0] + current_rl[1]) / 2)
            elif char == "R":
                current_rl[0] = ceil((current_rl[0] + current_rl[1]) / 2)

            print(f"[{i}] {char} current_row: {current_row}")
            print(f"[{i}] {char} current_rl: {current_rl}")

        current_seat_id = current_row[0] * MULTIPLIER + current_rl[0]
        if current_seat_id > max_current_seat_id:
            max_current_seat_id = current_seat_id
            max_row = current_row
            max_rl = current_rl

        print(f"row: {current_row}")
        print(f"column: {current_rl}")
        print(f"[{j}] current_seat_id: {current_seat_id}")
        seat_ids.append(current_seat_id)

    print(f"max row: {max_row}")
    print(f"max column: {max_rl}")
    print(f"Seat IDS {sorted(seat_ids)}")

    for x, z in enumerate(sorted(seat_ids)):
        if z != (x + 70):
            print(f"My Seat ID: {(z -1)}")
            break

    return max_current_seat_id


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        print(f"ANSWER: {count_x(inputs=_inputs)}")
