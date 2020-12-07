"""Created by Jhesed Tacadena Dec 07, 2020.

Advent of Code Day 7: https://adventofcode.com/2020/day/7

Output:
    Total Shiny Objects: 144
"""
from day7.common import DONE_FLAG, ITEM_TO_FIND, generate_rules


def count_bags_with_shiny_gold(
    rules: dict, item_to_find: str = ITEM_TO_FIND
) -> int:
    """Recursively counts bag colors that can eventually contain atleast one
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
    for rule in rules.keys():
        for colored_bag in rules[rule]:
            if item_to_find in colored_bag and not any(
                DONE_FLAG in colored_bag for colored_bag in rules[rule]
            ):
                # Add flag to identify processed rule to avoid duplicates
                rules[rule].append(DONE_FLAG)

                count += 1 + count_bags_with_shiny_gold(rules, rule)
    return count


if __name__ == "__main__":
    with open("data.txt", "r") as _file:
        _inputs = _file.read().splitlines()
        consolidate_rules = generate_rules(inputs=_inputs)
        total_count = count_bags_with_shiny_gold(consolidate_rules)
        print(f"Total Shiny Objects: {total_count}")
