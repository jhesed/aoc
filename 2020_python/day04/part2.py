"""Created by Jhesed Tacadena Dec 04, 2020.

Advent of Code Day 4: https://adventofcode.com/2020/day/4

Output:
    Answer: 127
"""
import re

from day04.validators import (
    REQUIRED_FIELDS,
    is_birth_year_valid,
    is_expiration_year_valid,
    is_eye_color_valid,
    is_field_existing,
    is_hair_color_valid,
    is_height_valid,
    is_issue_year_valid,
    is_passport_id_valid,
)

VALIDATION_FACTORY = {
    "byr": is_birth_year_valid,
    "iyr": is_issue_year_valid,
    "eyr": is_expiration_year_valid,
    "hgt": is_height_valid,
    "hcl": is_hair_color_valid,
    "ecl": is_eye_color_valid,
    "pid": is_passport_id_valid,
}


def count_valid_passports(inputs: list) -> int:
    """Counts number of valid passports."""
    counter = 0

    for line in inputs:
        valid = True

        for required_field in REQUIRED_FIELDS:

            valid = is_field_existing(
                required_field, line
            ) and VALIDATION_FACTORY[required_field](
                field=required_field, value=line
            )
            if not valid:
                break

        if valid:
            counter += 1

    return counter


if __name__ == "__main__":

    with open("data.txt", "r") as _file:
        blank_line_regex = r"(?:\r?\n){2,}"
        _inputs = re.split(blank_line_regex, _file.read().strip())
        answer = count_valid_passports(inputs=_inputs)

    print(f"Answer: {answer}")
