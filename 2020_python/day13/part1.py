"""Created by Jhesed Tacadena Dec 13, 2020.

Advent of Code Day 13: https://adventofcode.com/2020/day/13

Output:
    Answer: 153
    Elapsed time (seconds): 0.2634127140045166
"""
import time
from collections import OrderedDict

from day13.common import EXCLUDE


def find_bus_value(inputs: list) -> int:
    """Finds the ID of the earliest bus you can take to the airport multiplied
    by the number of minutes you'll need to wait for that bus."""
    target_time = int(inputs[0])
    bus_times = [int(i) for i in inputs[1].split(",") if i != EXCLUDE]
    all_bus_times = OrderedDict({t: [] for t in bus_times})

    iteration = 1
    while True:

        for i, bus_time in enumerate(bus_times):
            t = bus_time * iteration
            try:
                if t > target_time >= all_bus_times[bus_times[i]][-1]:
                    all_bus_times[bus_times[i]].append(t)
            except IndexError:
                # First item in list
                all_bus_times[bus_times[i]].append(t)

        iteration += 1

        found = [False] * len(bus_times)
        for bus_n, bus_time in all_bus_times.items():
            try:
                # print(v[-1], v[-1] >= target_time)
                if bus_time[-1] >= target_time:
                    found[bus_times.index(bus_n)] = True
            except IndexError:
                # Empty time
                pass

        # print(found, all_bus_times)
        if all(found):
            break
    return compute_bus_time(
        all_bus_times=all_bus_times, target_time=target_time
    )


def compute_bus_time(all_bus_times: OrderedDict, target_time: int) -> int:
    """Calculates difference of target subtracted with minimum time multipled
    to bus_number."""
    min_bus_time = min(all_bus_times.values())[0]
    bus_number = None
    for bus_n, bus_time in all_bus_times.items():
        if bus_time[-1] == min_bus_time:
            bus_number = bus_n

    return abs((target_time - min_bus_time) * bus_number)


if __name__ == "__main__":
    start_time = time.time()
    with open("data.txt", "r") as _file:
        answer = find_bus_value(inputs=_file.read().splitlines())
        print(f"Answer: {answer}")
    end_time = time.time()
    print(f"Elapsed time (seconds): {end_time-start_time}")
