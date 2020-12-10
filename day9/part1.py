"""Created by Jhesed Tacadena Dec 09, 2020.

Advent of Code Day 9: https://adventofcode.com/2020/day/9

Output:
    Total Shiny Objects:
"""

PREAMBLE = 25


def count_values(inputs: list) -> int:
    """TODO."""

    current_index = 0
    for _ in inputs:

        previous_x_values = inputs[current_index - PREAMBLE : current_index]
        current_value = int(inputs[current_index])
        print(f"[{current_index}] {current_value}: {previous_x_values:}")
        current_index += 1

        if len(previous_x_values) != PREAMBLE:
            continue
        is_valid = False

        for i in previous_x_values:
            i = int(i)
            for j in previous_x_values:

                j = int(j)
                print(f"[{current_value}] {i} + {j} = {i + j}")
                if i + j == current_value:
                    is_valid = True
                    break
        if not is_valid:
            print()
            return current_value


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        total_count = count_values(_inputs)
        print(f"Answer: {total_count}")
