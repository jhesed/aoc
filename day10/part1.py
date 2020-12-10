"""Created by Jhesed Tacadena Dec 10, 2020.

Advent of Code Day 10: https://adventofcode.com/2020/day/10

Output:
    Answer: 2812
"""
from day10.common import ACCEPTABLE_DIFF, BUILT_IN_ADAPTER_MARGIN, START_POINT


def compute_product_of_joltages(inputs: list) -> int:
    """TODO."""
    built_in_adapter_joltage = (
        get_max_joltage(inputs=inputs) + BUILT_IN_ADAPTER_MARGIN
    )
    answers = {}  # Key: diff
    inputs.append(built_in_adapter_joltage)

    previous_joltage = START_POINT
    for joltage in inputs:
        diff = joltage - previous_joltage
        if diff <= ACCEPTABLE_DIFF:

            if diff not in answers:
                answers[diff] = []

            answers[diff].append(joltage)
            previous_joltage = joltage

    print(answers)
    product = 1
    for diff, values in answers.items():
        print(f"[{diff}] {len(values)}")
        product *= len(values)
    # print(built_in_adapter_joltage)
    print(f"answer: {product} ")


def get_max_joltage(inputs: list) -> int:
    return max([int(i) for i in inputs])


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = sorted([int(i) for i in _file.read().splitlines()])
        print(_inputs)
        answer = compute_product_of_joltages(_inputs)
        print(f"Answer: {answer}")
