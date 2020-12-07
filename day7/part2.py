"""Created by Jhesed Tacadena Dec 07, 2020.

Advent of Code Day 7: https://adventofcode.com/2020/day/7

Output:
    Total Shiny Objects: 5956
"""
from tkinter.messagebox import IGNORE

from day7.common import ITEM_TO_FIND, generate_rules


def count_total_bags_required_for_shiny_gold(
    rules: dict, item_to_find: str = ITEM_TO_FIND
) -> int:
    """Recursively counts individual bags that are required inside a single
    shiny gold bag.

    :param rules: e.g. {
            "dark maroon": [
                "2 striped silver",
                "4 mirrored marron",
                # More items
            ],
            # ... More items
        }
    :param item_to_find: e.g. `shiny gold`
    """
    count = 0
    for bag in rules[item_to_find]:
        if bag != IGNORE:
            # Example bag: 5 muted orange
            bag_count = int(bag[0])  # e.g. 5
            next_key = bag[2:]  # e.g. muted orange
            count += bag_count * (
                1
                + count_total_bags_required_for_shiny_gold(
                    rules=rules, item_to_find=next_key
                )
            )
    return count


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        consolidate_rules = generate_rules(inputs=_inputs)
        total_count = count_total_bags_required_for_shiny_gold(
            consolidate_rules
        )
        print(f"Total Shiny Objects: {total_count}")
