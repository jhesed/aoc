"""Created by Jhesed Tacadena Dec 12, 2020.

Advent of Code Day 12: https://adventofcode.com/2020/day/12

Output:
    Manhattan Distance: 998
    Elapsed time (seconds): 0.0
"""
import time

from day12.common import (
    DEGREES_ORDERING,
    DEGREES_PER_TURN,
    EAST,
    FORWARD,
    LEFT,
    NORTH,
    RIGHT,
    SOUTH,
    START_DIRECTION,
    WEST,
    compute_manhattan_distance,
)


def get_direction(new_action: str, value: int, current_direction: str) -> str:
    """Identifies new direction based on given inputs."""

    current_direction_index = DEGREES_ORDERING.index(current_direction)
    new_action_index = (
        value // DEGREES_PER_TURN * (-1 if new_action == LEFT else 1)
    )

    new_action_index = (current_direction_index + new_action_index) % len(
        DEGREES_ORDERING
    )
    return DEGREES_ORDERING[new_action_index]


def identify_ship_location(inputs: list) -> dict:
    location = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
    current_direction = START_DIRECTION

    for line in inputs:
        action = line[0]  # e.g. N | S | E | W | F
        value = int(line[1:])

        if action == FORWARD:
            location[current_direction] += value

        elif action in (NORTH, SOUTH, EAST, WEST):
            location[action] += value

        elif action in (LEFT, RIGHT):
            current_direction = get_direction(action, value, current_direction)

        # print(action, value, location, current_direction)

    return location


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        ship_location = identify_ship_location(
            inputs=_file.read().splitlines()
        )
        manhattan_distance = compute_manhattan_distance(ship_location)
        print(f"Manhattan Distance: {manhattan_distance}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
