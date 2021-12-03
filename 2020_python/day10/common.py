"""Created by Jhesed Tacadena Dec 10, 2020."""

START_POINT = 0
ACCEPTABLE_DIFF = 3
BUILT_IN_ADAPTER_MARGIN = 3  # Add 3 to highest value


def get_max_joltage(inputs: list) -> int:
    """Retrieves max joltage from list of inputs."""
    return max([int(i) for i in inputs])


def generate_unique_key(joltage: int) -> str:
    """Simply generates a string of key to avoid collision with other numbers
    in e.g. the dictionary.

    :param joltage: e.g. 10
    :return: e.g. KEY10
    """
    return f"KEY{joltage}"


def compute_product(joltages: dict) -> int:
    """Computes product of provided joltages."""

    product = 1
    for diff, values in joltages.items():
        product *= len(values)
    return product
