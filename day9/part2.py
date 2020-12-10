"""Created by Jhesed Tacadena Dec 09, 2020.

Advent of Code Day 9: https://adventofcode.com/2020/day/9

Output:
    Total Shiny Objects:
"""
from day9.part1 import count_values

PREAMBLE = 25


def find_contiguous(inputs, target):
    current_index = 0
    for index, i in enumerate(inputs):
        i = int(i)
        numbers = [i]
        for j in inputs[index + 1 :]:
            j = int(j)
            numbers.append(j)

            if target == sum(numbers):
                print("FOUND: ", numbers)
                return numbers


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        answer = find_contiguous(_inputs, target=count_values(inputs=_inputs))

        print(min(answer) + max(answer))
        print(f"target: {answer}")
