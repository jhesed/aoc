"""Created by Jhesed Tacadena Dec 12, 2020."""

START_DIRECTION = "E"

FORWARD = "F"

NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"

LEFT = "L"
RIGHT = "R"

DEGREES_ORDERING = [NORTH, EAST, SOUTH, WEST]
DEGREES_PER_TURN = 90


def compute_manhattan_distance(ship_location: dict) -> int:
    """
    :param ship_location: e.g. {
            "N": 1,
            "E": 10,
            "S": 11,
            "W": 13
        }
    """

    return abs(ship_location[EAST] - ship_location[WEST]) + abs(
        ship_location[NORTH] - ship_location[SOUTH]
    )
