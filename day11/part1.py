"""Created by Jhesed Tacadena Dec 11, 2020.

Advent of Code Day 11: https://adventofcode.com/2020/day/11

Output:
"""

FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
UNOCCUPIED_SEATS = (FLOOR, EMPTY_SEAT)
EXCLUDE_CHAR = "J"
THRESHOLD = 4

def count_x(inputs: list, out_file: str) -> int:
    """TODO"""

    modified_values = []
    for row_index, row in enumerate(inputs):
        modified_seating_arrangement = ""
        for col_index, col in enumerate(row):

            # ----------------- OCCUPY
            occupy = False
            occupied_counter = 0

            occupy = True

            # Indices
            left_index = col_index -1
            right_index = col_index + 1
            up_index = row_index - 1
            down_index = row_index + 1

            # Seat Values
            left = row[left_index]
            up = inputs[up_index]

            try:
                down = inputs[down_index]
            except IndexError:
                down = EXCLUDE_CHAR

            try:
                right = row[right_index]
            except IndexError:
                right = EXCLUDE_CHAR

            if left_index > 0 and left == OCCUPIED_SEAT:
                if col == EMPTY_SEAT:
                    occupy = False
                occupied_counter += 1

            if right_index > 0 and right == OCCUPIED_SEAT:
                if col == EMPTY_SEAT:
                    occupy = False
                occupied_counter += 1

            if up_index > 0 and up[col_index] == OCCUPIED_SEAT:
                if col == EMPTY_SEAT:
                    occupy = False
                occupied_counter += 1

            try:
                if down_index > 0 and down[col_index] == OCCUPIED_SEAT:
                    if col == EMPTY_SEAT:
                        occupy = False
                    occupied_counter += 1
            except IndexError:
                pass

            # Diagonals Up-left
            if up_index > 0 and left_index > 0 and up[col_index-1] == OCCUPIED_SEAT:
                if col == EMPTY_SEAT:
                    occupy = False
                occupied_counter += 1

            # Diagonals Up-Right
            try:
                if up_index > 0 and right_index > 0 and up[col_index+1] == OCCUPIED_SEAT:
                    if col == EMPTY_SEAT:
                        occupy = False
                    occupied_counter += 1
            except IndexError:
                pass

            # Diagonals Down-left
            try:
                if down_index > 0 and left_index > 0 and down[col_index-1] == OCCUPIED_SEAT:
                    if col == EMPTY_SEAT:
                        occupy = False
                    occupied_counter += 1
            except IndexError:
                pass

            # Diagonals Down-left
            try:
                if down_index > 0 and right_index > 0 and down[col_index +1] == OCCUPIED_SEAT:
                    if col == EMPTY_SEAT:
                        occupy = False
            except IndexError:
                pass

            # TODO: Finalize rules here
            seat = col
            if occupy:
                seat = OCCUPIED_SEAT
            if occupied_counter >= THRESHOLD:
                seat = EMPTY_SEAT
            modified_seating_arrangement += seat

            # print(f"[{col}]: [L {left_index}] {left} [R {right_index}] {right}, [OCC] {occupy}")

        modified_values.append(modified_seating_arrangement)

    with open(out_file, "w") as _file:
        for v in modified_values:
            _file.write(v)
            _file.write("\n")
    return modified_values

def count_occupied_seats(inputs: list):
    counter = 0
    for row_index, row in enumerate(inputs):
        for col_index, col in enumerate(row):
            if col == OCCUPIED_SEAT:
                counter += 1
    return counter


if __name__ == "__main__":
    i = 0
    answers = []
    while True:
        file_name = f"data{i}.txt"
        out_file =  f"data{i+1}.txt"
        with open(file_name, "r") as _file:
            _inputs = _file.read().splitlines()
            answers.append(count_x(inputs=_inputs, out_file=out_file))
            if i!= 0 and answers[i] == answers[i-1]:
                print(i)
                print("DONE.")
                print(answers[i])
                print(f"COUNT: {count_occupied_seats(answers[i])}")
                break
            i += 1

