"""Created by Jhesed Tacadena Dec 14, 2020."""


MASK = "mask"
MEM = "mem"
MEM_NAME_START_INDEX = 4
MEM_NAME_END_INDEX = -2
DELIMITER = "="
BINARY_LENGTH = 36
FLOATING = "X"
IGNORE = "X"
ZERO = "0"
ONE = "1"
BITS = ["1", "0"]


def convert_decimal_to_binary(decimal_number: int) -> bin:
    return bin(decimal_number).replace("0b", "")


def convert_binary_to_decimal(binary_number) -> int:
    return int(binary_number, 2)


def uniq_comb(pool, r):
    """
    A more efficient way of returning UNIQUE combinations from
    built in combinations library in python
    Source: https://stackoverflow.com/questions/48602709/fastest-way-to-find-unique-combinations-of-list
    """
    if r:
        seen = set()
        for i, item in enumerate(pool):
            if item not in seen:
                seen.add(item)
                for tail in uniq_comb(pool[i + 1 :], r - 1):
                    yield (item,) + tail
    else:
        yield ()
