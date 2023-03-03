"""Created by Jhesed Tacadena Dec 14, 2020.

Advent of Code Day 14: https://adventofcode.com/2020/day/14

Output:
    Answer: 3505392154485
    Elapsed time (seconds): 2.605086326599121
"""
import time
from collections import OrderedDict

from day14.common import (
    BINARY_LENGTH,
    BITS,
    DELIMITER,
    FLOATING,
    MASK,
    MEM_NAME_END_INDEX,
    MEM_NAME_START_INDEX,
    ZERO,
    convert_binary_to_decimal,
    convert_decimal_to_binary,
    uniq_comb,
)


def bit_and_string(binary_string: str, mask: str) -> str:
    """A custom bitwise operator and for string.

    TODO: Read on a more standard way of doing this.
    """
    new_string = ""
    for index, char in enumerate(binary_string):

        if mask[index] == ZERO:
            new_string += char
        else:
            new_string += mask[index]

    return new_string


def generate_bit_combinations(masked_binary_value_mem_name: str) -> list:
    """Given a bit with floating values, e.g.
    000000000000000000000000000000X1101X, This function generates possible
    combinations for x. e.g.

    - 000000000000000000000000000000011010  (decimal 26)
    - 000000000000000000000000000000011011  (decimal 27)
    - 000000000000000000000000000000111010  (decimal 58)
    - 000000000000000000000000000000111011  (decimal 59)
    """
    list_value = list(masked_binary_value_mem_name)
    floating_indexes = [i for i, x in enumerate(list_value) if x == FLOATING]
    floating_count = len(floating_indexes)
    combination_count = 2**floating_count

    comb = uniq_comb(BITS * combination_count, r=floating_count)

    answers = []
    for values in comb:
        list_value = list(masked_binary_value_mem_name)
        for i, index in enumerate(floating_indexes):
            list_value[index] = values[i]
        answers.append("".join(list_value))
    return answers


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

            # Apply first mem_value to bitmask
            binary_value_mem_name = str(
                convert_decimal_to_binary(mem_name)
            ).rjust(BINARY_LENGTH, ZERO)

            # Perform masking against mem_value
            masked_binary_value_mem_name = bit_and_string(
                binary_value_mem_name, current_mask_value
            )

            # Generate combinations
            combinations = generate_bit_combinations(
                masked_binary_value_mem_name
            )

            # Convert to decimal
            decimal_values = []
            for comb in sorted(combinations):
                d_value = convert_binary_to_decimal(comb)
                decimal_values.append(d_value)
                formatted_inputs[d_value] = mem_value

    return sum(formatted_inputs.values())


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        answer = compute_sum_of_values(inputs=_file.read().splitlines())
        print(f"Answer: {answer}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
