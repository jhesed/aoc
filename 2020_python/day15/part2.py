"""Created by Jhesed Tacadena Dec 15, 2020.

Advent of Code Day 15: https://adventofcode.com/2020/day/15

Output:
    # TODO: LOTS OF ROOM FOR OPTIMIZATION!!!!  TOO SLOW!!!
            DON'T USE DEQUE! It might be causing the slow down!
    Answer: 955
    Elapsed time (seconds): 22.818878889083862
"""
import time
from collections import deque

START_TURN = 1
END_TURN = 30000000
UNSEEN_VALUE = 0
MAX_DEQUE_LEN = 2


def compute_x(inputs: list) -> int:
    """Determine the 30000000th number spoken in the Elves games.

    Sample structure of seen:
        {7: deque([1]), 14: deque([2]), 0: deque([3]), 17: deque([4]), 11:
        deque([5]), 1: deque([6]), 2: deque([7])}
    """

    # Initialize variables
    seen = {}
    current_turn = START_TURN

    # Retrieve initial values from players
    initial_values = [int(i) for i in (inputs[0].split(","))]  # e.g. 0, 3, 6

    # Iterate over initial values:
    for index, number in enumerate(initial_values):
        seen[number] = deque([current_turn], maxlen=MAX_DEQUE_LEN)
        current_turn += 1

    current_value = initial_values[-1]
    while current_turn < (END_TURN + 1):

        # Identify current value
        if not seen.get(current_value):
            current_value = UNSEEN_VALUE
        else:
            try:
                current_value = seen[current_value][1] - seen[current_value][0]
            except IndexError:
                current_value = UNSEEN_VALUE

        # Append indexes to the right coordinate
        if not seen.get(current_value):
            seen[current_value] = deque([current_turn], maxlen=MAX_DEQUE_LEN)
        else:
            seen[current_value].append(current_turn)

        # print(f"Turn {current_turn}; Current Value: {current_value}; Seen: {seen}")

        current_turn += 1

    return current_value


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        answer = compute_x(inputs=_file.read().splitlines())
        print(f"Answer: {answer}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
