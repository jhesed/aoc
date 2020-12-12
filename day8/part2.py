"""Created by Jhesed Tacadena Dec 08, 2020.

Advent of Code Day 8: https://adventofcode.com/2020/day/8

Output:
    answer: 758
"""
from day8.common import ACCUMULATE, JUMP, NO_OPERATION


def find_all_jmp_indexes(inputs: list) -> list:
    """Retrieves all indices of `jmp` in input file."""

    all_jmp_indexes = []
    for index, line in enumerate(inputs):
        operator, argument = line.split()
        if operator == JUMP:
            all_jmp_indexes.append(index)

    return all_jmp_indexes


def find_incorrect_jmp_value_and_compute_total_acc(
    inputs: list, jump_index
) -> tuple:
    """There's a bug in the code, e.g. one jmp value must be updated to nop.

    The terminating condition is that is should reach the end of file.

    :returns: e.g. (is_found (bool), total_accumulated_value (int))
    """

    total_acc = 0
    current_line_index = 0
    visited_indexes = []

    while True:

        # Terminating conditions
        if len(inputs) == current_line_index:
            print("DONE. Got last line")
            return True, total_acc

        if current_line_index in visited_indexes:
            print("DONE. INCORRECT guess.")
            return False, total_acc
        else:
            visited_indexes.append(current_line_index)

        line = inputs[current_line_index]  # e.g. `jmp -105`
        operator, argument = line.split()
        argument = int(argument)  # e.g. from `"-1"` to `-1`

        if current_line_index == jump_index:
            operator = NO_OPERATION

        if operator == ACCUMULATE:
            total_acc += argument

        if operator == JUMP:
            current_line_index += argument
        else:
            current_line_index += 1

        print(f"{line} | {total_acc}")


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()

        jump_indexes = find_all_jmp_indexes(inputs=_inputs)
        for _index in jump_indexes:
            is_found, total = find_incorrect_jmp_value_and_compute_total_acc(
                inputs=_inputs, jump_index=_index
            )
            if is_found is True:
                print(f"Found: {total}")
                break
