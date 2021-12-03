"""Created by Jhesed Tacadena Dec 11, 2020.

Advent of Code Day 11: https://adventofcode.com/2020/day/11

# TODO: Optimize. Lots of room for improvement

Output:
    Occupied Seats: 1865
    Elapsed time (seconds): 14.418888092041016
"""
import time

from numpy import array, count_nonzero, empty

DIRECTION_LENGTH = 8
UP = "UP"
DOWN = "DOWN"
RIGHT = "RIGHT"
LEFT = "LEFT"
DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"
DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"
DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"

FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
UNOCCUPIED_SEATS = (FLOOR, EMPTY_SEAT)
EXCLUDE_CHAR = "J"
THRESHOLD = 5


def build_matrix(string_content: str) -> array:
    """Builds xd matrix from given content."""
    content = string_content.splitlines()
    tmp = []
    for row in content:
        tmp.append([char for char in row])
    return array(tmp)


def get_adjacent_seat_coordinates(
    row_index: int, col_index: int, matrix_height: int, matrix_width: int, distance: int=1
) -> dict:
    """
    Ordering: up, down, left, right, diagonal up left, diagonal up right,
            diagonal down left, diagonal down right
    """
    U = row_index-distance if row_index-distance >= 0 else None
    D = row_index+distance if row_index+distance < matrix_height else None
    L = col_index-distance if col_index-distance >=0 else None
    R = col_index + distance if col_index + distance < matrix_width else None

    adjacents = {
        UP: (U, col_index),
        DOWN: (D, col_index),
        LEFT: (row_index, L),
        RIGHT: (row_index, R),

        # Diagonals
        DIAGONAL_UP_LEFT: (U, L),
        DIAGONAL_UP_RIGHT: (U, R),
        DIAGONAL_DOWN_LEFT: (D, L),
        DIAGONAL_DOWN_RIGHT: (D, R)
    }
    return adjacents


def get_seat_values(matrix: array, adjacent_coordinates: dict, seat_values) -> dict:
    """
    None = no seat at all in adjacent
    L = Empty seat
    # = Occupied seat
    """
    for direction, coordinate in adjacent_coordinates.items():
        if not seat_values.get(direction):
            if None in coordinate:
                # seat_values[direction] = None
                pass
            elif (seat:=matrix[coordinate[0]][coordinate[1]]) in (OCCUPIED_SEAT, EMPTY_SEAT):
                seat_values[direction] = seat

    return seat_values

def rearrange_seats(matrix: array):
    """TODO."""

    height, width = matrix.shape
    updated_matrix = array(empty((height, width), dtype=str))

    # print(f"height: {height}, width: {width}")

    for row_index, row in enumerate(matrix):
        for col_index, col_scalar in enumerate(row):
            seat_values = {}
            distance = 1
            while len(seat_values.keys()) < DIRECTION_LENGTH and distance < height:
                adjacents = get_adjacent_seat_coordinates(row_index, col_index, height, width, distance=distance)
                seat_values = get_seat_values(matrix, adjacents, seat_values)
                distance += 1

            # Rearrange seats
            if col_scalar == EMPTY_SEAT and all(v != OCCUPIED_SEAT for v in seat_values.values()):
                updated_matrix[row_index][col_index] = OCCUPIED_SEAT
            elif col_scalar == OCCUPIED_SEAT and sum(v == OCCUPIED_SEAT for v in seat_values.values()) >= THRESHOLD:
                updated_matrix[row_index][col_index] = EMPTY_SEAT
            elif col_scalar == FLOOR:
                updated_matrix[row_index][col_index] = FLOOR
            else:
                updated_matrix[row_index][col_index] = col_scalar

    # print(updated_matrix)
    return updated_matrix


def count_occupied_seats(matrix: array) -> int:
    """Count occupied seats in matrix."""
    return count_nonzero(matrix == OCCUPIED_SEAT)


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:

        _matrix = build_matrix(string_content=_file.read())
        prev_matrix = rearrange_seats(matrix=_matrix)
        next_matrix = rearrange_seats(matrix=prev_matrix)

        while not ((next_matrix == prev_matrix).all()):
            prev_matrix = next_matrix
            next_matrix = rearrange_seats(matrix=prev_matrix)

        print(f"Occupied Seats: {count_occupied_seats(matrix=next_matrix)}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
