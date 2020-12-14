"""Created by Jhesed Tacadena Dec 14, 2020.

Advent of Code Day 14: https://adventofcode.com/2020/day/14

Output:
    Answer: 13105044880745
    Elapsed time (seconds): 0.0
"""
import time
from collections import OrderedDict

from day14.common import (
    BINARY_LENGTH,
    DELIMITER,
    IGNORE,
    MASK,
    MEM_NAME_END_INDEX,
    MEM_NAME_START_INDEX,
    ZERO,
    convert_binary_to_decimal,
    convert_decimal_to_binary,
)


def bit_and_string(binary_string: str, mask: str) -> str:
    """A custom bitwise operator and for string.

    TODO: Read on a more standard way of doing this.
    """
    new_string = ""
    for index, char in enumerate(binary_string):

        if mask[index] != IGNORE:
            new_string += mask[index]
        elif mask[index] == IGNORE or mask[index] == char:
            new_string += char
        else:
            new_string += ZERO
    return new_string


def compute_sum_of_values(inputs: list) -> int:
    """Computes sum of all values left in memory after it completes."""
    formatted_inputs = OrderedDict({})
    current_mask_value = None
    for index, line in enumerate(inputs):
        if MASK in line:
            current_mask_value = line.split(DELIMITER)[
                1
            ].strip()  # e.g. XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
        else:

            # Extract mem key and value
            mem_name, mem_value = line.split(DELIMITER)
            mem_name = int(
                mem_name[MEM_NAME_START_INDEX:MEM_NAME_END_INDEX]
            )  # e.g. 8 from mem[8]
            mem_value = int(mem_value.strip())  # e.g. 11 from mem[8] = 11

            # Convert it to binary string
            binary_value = str(convert_decimal_to_binary(mem_value)).rjust(
                BINARY_LENGTH, ZERO
            )

            # Perform masking
            masked_binary_value = bit_and_string(
                binary_value, current_mask_value
            )

            # Convert back to integer
            masked_integer_value = convert_binary_to_decimal(
                masked_binary_value
            )

            formatted_inputs[mem_name] = masked_integer_value

    return sum(formatted_inputs.values())


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        answer = compute_sum_of_values(inputs=_file.read().splitlines())
        print(f"Answer: {answer}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
