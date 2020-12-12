"""Created by Jhesed Tacadena Dec 12, 2020.

Advent of Code Day 12: https://adventofcode.com/2020/day/12

Output:
    Manhattan Distance: 71586
    Elapsed time (seconds): 0.0
"""
import time
from collections import OrderedDict, deque

from day12.common import (
    DEGREES_PER_TURN,
    EAST,
    FORWARD,
    LEFT,
    NORTH,
    RIGHT,
    SOUTH,
    WEST,
    compute_manhattan_distance,
)


def compute_waypoint(current_waypoints, action, value):
    """Calculates waypoint based on action / direction and value Used
    OrderedDict instead of plain dict to ease rotation in dictionary."""
    waypoint_values = deque(current_waypoints.values())
    new_action_index = (
        value // DEGREES_PER_TURN * (-1 if action == LEFT else 1)
    )

    waypoint_values.rotate(new_action_index)
    return OrderedDict(
        {
            key: value
            for key, value in zip(current_waypoints.keys(), waypoint_values)
        }
    )


def identify_ship_location(inputs: list) -> dict:
    """Used OrderedDict to preserve ordering of directions for later use."""
    waypoints = OrderedDict({NORTH: 1, EAST: 10, SOUTH: 0, WEST: 0})
    location = OrderedDict({NORTH: 0, EAST: 0, SOUTH: 0, WEST: 0})

    for line in inputs:
        action = line[0]  # e.g. N | S | E | W | F
        value = int(line[1:])

        if action == FORWARD:
            for direction, direction_value in location.items():
                location[direction] = direction_value + (
                    waypoints[direction] * value
                )

        elif action in (NORTH, SOUTH, EAST, WEST):
            waypoints[action] += value

        elif action in (LEFT, RIGHT):
            waypoints = compute_waypoint(waypoints, action, value)
        # print(action, value, waypoints, current_direction, location)

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
