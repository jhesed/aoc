"""Created by Jhesed Tacadena Dec 07, 2020.

Just a file to share common variables / functions for part 1 and part 2
"""

DONE_FLAG = "DONE"
ITEM_TO_FIND = "shiny gold"


def generate_rules(inputs: list) -> dict:
    """
    Generates rules based from given inputs
    :returns: Example:
        {
            "dark maroon": [
                "2 striped silver",
                "4 mirrored marron",
                # More items
            ],
            # ... More items
        }
    """
    rules = {}
    for line in inputs:
        [parent, rule] = line.strip().split(" contain ")
        parent = parent.replace(" bags", "")
        rule = rule.strip(".").split(", ")
        rules[parent] = [
            item_to_find.replace(" bags", "").replace(" bag", "")
            for item_to_find in rule
        ]
    return rules
