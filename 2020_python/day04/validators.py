"""Created by Jhesed Tacadena Dec 04, 2020.

Contains validation rules for a passport
"""
import re

REQUIRED_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def get_value(field: str, value: str) -> str:
    """Helper function for extracting passport requirement."""
    return value.split(f"{field}:")[1].split()[0]


def is_field_existing(field: str, value: str) -> bool:
    if field not in value:
        return False
    return True


def is_yr_valid(field, value, start_year, end_year):
    try:
        value = int(get_value(field=field, value=value))
        if not (start_year <= value <= end_year):
            return False
    except ValueError:
        return False
    else:
        return True


def is_birth_year_valid(field: str, value: str) -> bool:
    return is_yr_valid(field, value, 1920, 2002)


def is_issue_year_valid(field: str, value: str) -> bool:
    return is_yr_valid(field, value, 2010, 2020)


def is_expiration_year_valid(field: str, value: str) -> bool:
    return is_yr_valid(field, value, 2020, 2030)


def is_height_valid(field, value, regex=r"(\d+)(in.*|cm.*)"):
    try:
        value = get_value(field=field, value=value)
        matches = re.search(regex, value)
        height = int(matches.group(1))

        if matches.group(2) == "in" and not (59 <= height <= 76):
            return False

        if matches.group(2) == "cm" and not (150 <= height <= 193):
            return False

    except AttributeError:
        return False
    else:
        return True


def is_hair_color_valid(field, value, regex=r"(#)([0-9a-f]{6})$"):
    try:
        value = get_value(field=field, value=value)
        matches = re.search(regex, value)
        if not matches.group(2):
            return False
    except AttributeError:
        return False
    else:
        return True


def is_eye_color_valid(field: str, value: str) -> bool:
    try:
        value = get_value(field=field, value=value)
        if value not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            return False
    except AttributeError:
        return False
    else:
        return True


def is_passport_id_valid(field, value, regex=r"^([0-9]{9})$"):
    try:
        value = get_value(field=field, value=value)
        matches = re.search(regex, value)
        if not matches.group(1):
            return False
    except AttributeError:
        return False
    else:
        return True
