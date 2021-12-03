"""Created by Jhesed Tacadena Dec 08, 2020.

Advent of Code Day 8: https://adventofcode.com/2020/day/8

Output:
    answer: 1594
"""
from day08.common import ACCUMULATE, JUMP


def compute_total_acc_before_second_execution(inputs: list) -> int:
    """The inputs are machine-code-like which will run in an infinite loop.
    Before executing a command (e.g. line) the second time, return the
    `total_acc` as the answer.

    :param inputs: e.g. ["nop +43", "jmp -65", "..."]
    """

    total_acc = 0
    current_line_index = 0
    visited_indexes = []

    while True:

        # Terminating condition
        if current_line_index in visited_indexes:
            print(
                f"DONE. Already visited {current_line_index} "
                f"from visited indexes: {visited_indexes}"
            )
            return total_acc

        visited_indexes.append(current_line_index)
        line = inputs[current_line_index]  # e.g. `jmp -105`
        operator, argument = line.split()
        argument = int(argument)  # e.g. from `"-1"` to `-1`

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
        answer = compute_total_acc_before_second_execution(inputs=_inputs)
        print(f"answer: {answer}")
