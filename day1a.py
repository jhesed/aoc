"""
    Created by Jhesed Tacadena Dec 01, 2020

    Advent of Code Day 1: https://adventofcode.com/2020/day/1
"""


def compute_product_of_targets(inputs: list, target: int = 2020) -> int:
    """
    Finds 2 targets in list where sum is 2020 and calculate their product.
    """
    for counter, first_candidate in enumerate(inputs):
        try:
            for second_candidate in inputs[counter + 1 :]:
                if first_candidate + second_candidate == target:
                    print(f"FIRST number: {first_candidate}")
                    print(f"SECONDS number: {second_candidate}")
                    return first_candidate * second_candidate
        except IndexError:
            print("No number in list match the target qualification")
            return -1


if __name__ == "__main__":

    with open("data/day1.txt", "r") as _file:
        day1_inputs = list(map(int, _file.read().splitlines()))
        print(f"ANSWER: {compute_product_of_targets(inputs=day1_inputs)}")
