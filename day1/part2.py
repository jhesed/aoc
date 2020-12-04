"""Created by Jhesed Tacadena Dec 01, 2020.

Output:
    FIRST number value:  912
    SECOND number value:  977
    THIRD number value:  131
    ANSWER: 116724144
"""


def compute_product_of_targets(inputs: list, target: int = 2020) -> int:
    """Finds 2 targets in list where sum is 2020 and calculate their
    product."""
    try:
        for counter, first_candidate in enumerate(inputs):
            for counter2, second_candidate in enumerate(inputs[counter:]):
                for third_candidate in inputs[counter2:]:
                    if (
                        first_candidate + second_candidate + third_candidate
                        == target
                    ):
                        print("FIRST number value: ", first_candidate)
                        print("SECOND number value: ", second_candidate)
                        print("THIRD number value: ", third_candidate)
                        return (
                            first_candidate
                            * second_candidate
                            * third_candidate
                        )
    except IndexError:
        print("No number in list match the target qualification")
        return -1


if __name__ == "__main__":

    with open("data.txt", "r") as _file:
        day1_inputs = list(map(int, _file.read().splitlines()))
        print(f"ANSWER: {compute_product_of_targets(inputs=day1_inputs)}")
