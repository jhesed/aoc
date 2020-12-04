"""Created by Jhesed Tacadena Dec 04, 2020.

Advent of Code Day 4: https://adventofcode.com/2020/day/4

Output:
"""
import re

REQUIRED_FIELDS = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
)


DELIMITER = "\n"

def count(inputs: list) -> int:
    """Counts number of trees (e.g. #) in matrix."""
    counter = 0

    for input in inputs:
        valid = True
        # item = input.split("\r\n")
        # if item:
        if input:
            for required_field in REQUIRED_FIELDS:
                if required_field not in input:
                    valid = False
                    break

                if required_field == "byr":
                    try:
                        byr = int(input.split("byr:")[1].split()[0])
                        if not(1920 <= byr <= 2002):
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break

                if required_field == "iyr":
                    try:
                        byr = int(input.split("iyr:")[1].split()[0])
                        if not(2010 <= byr <= 2020):
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break

                elif required_field == "eyr":
                    try:
                        byr = int(input.split("eyr:")[1].split()[0])
                        if not (2020 <= byr <= 2030):
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break

                elif required_field == "hgt":
                    try:

                        byr = input.split("hgt:")[1].split()[0]
                        regex = r'(\d+)(in.*|cm.*)'
                        value = re.search(regex, byr)
                        height = int(value.group(1))

                        if value.group(2) == "in":
                            print("IN")
                            print(height)
                            if not(59 <= height <= 76):
                                valid = False
                                break

                        if value.group(2) == "cm":
                            print("CM")
                            print(height)
                            if not(150 <= height <= 193):
                                valid = False
                                break

                    except:
                        valid = False
                        break

                if required_field == "hcl":
                    try:

                        byr = input.split("hcl:")[1].split()[0]
                        regex = r'(#)([0-9a-f]{6})$'
                        value = re.search(regex, byr)
                        if not value.group(2):
                            valid = False
                            break
                    except:
                        print("ERROR")
                        valid = False
                        break

                if required_field == "ecl":
                    try:

                        byr = input.split("ecl:")[1].split()[0]
                        if byr not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                            valid = False
                            break
                    except:
                        print("ERROR")
                        valid = False
                        break

                if required_field == "pid":
                    try:

                        byr = input.split("pid:")[1].split()[0]
                        regex = r'^([0-9]{9})$'
                        value = re.search(regex, byr)
                        if not value.group(1):
                            valid = False
                            break
                    except:
                        print("ERROR")
                        valid = False
                        break

            if valid:
                # print(input)
                counter += 1

    return counter


if __name__ == "__main__":

    with open("data.txt", "r") as _file:
        blank_line_regex = r"(?:\r?\n){2,}"
        _inputs = re.split(blank_line_regex, _file.read().strip())

        # _inputs = _file.read().splitlines()
        answer = count(inputs=_inputs)

    print(f"Answer: {answer}")
