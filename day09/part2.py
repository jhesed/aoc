"""Created by Jhesed Tacadena Dec 09, 2020.

Advent of Code Day 9: https://adventofcode.com/2020/day/9

Output:
    Contiguous Numbers: [5636985, 7377933, 5865067, 7221919, 7453812, 7081408,
        6541452, 7091721, 7269511, 7639101, 8951313, 9935100, 10470974,
        7999555, 8416737, 8604840, 9458140]
    Sum of min and max: 16107959
"""
from day09.part1 import find_number


def find_contiguous(inputs: list, target: int) -> list:
    """Finds contiguous set of at least two numbers which is equal to
    `target`"""
    for index, i in enumerate(inputs):
        i = int(i)
        numbers = [i]
        for j in inputs[index + 1 :]:
            j = int(j)
            numbers.append(j)

            if target == sum(numbers):
                return numbers


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        contiguous_numbers = find_contiguous(
            _inputs, target=find_number(inputs=_inputs)
        )

        print(f"Contiguous Numbers: {contiguous_numbers}")
        print(
            f"Sum of min and max: {min(contiguous_numbers) + max(contiguous_numbers)}"
        )
