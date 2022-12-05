"""
Day 5: Supply Stacks
"""

import re
from copy import deepcopy


def get_data(filename):
    with open(filename) as f:
        data = f.read().split("\n\n")
        return get_stacks(data), get_instructions(data)


def get_stacks(data):
    lines = data[0].split("\n")
    stacks = {int(num): [] for num in lines[-1].split()}
    for i in range(2, len(lines) + 1):
        for num, stack in stacks.items():
            crate = lines[-i][4 * num - 3]
            if crate != " ":
                stack.append(crate)
    return stacks


def get_instructions(data):
    return [
        [int(n) for n in re.findall(r"\d+", line)]
        for line in data[1].split("\n")
    ]


def move_crates(stacks, line, type):
    amount, from_stack, to_stack = line
    if type == 1:
        for _ in range(amount):
            crate_moved = stacks[from_stack].pop()
            stacks[to_stack].append(crate_moved)
    elif type == 2:
        stacks[to_stack] += stacks[from_stack][-amount:]
        stacks[from_stack] = stacks[from_stack][:-amount]
    return stacks


def get_top_crates(stacks):
    return "".join(stack[-1] for _, stack in stacks.items() if stack)


def main(filename):
    stacks1, instructions = get_data(filename)
    stacks2 = deepcopy(stacks1)

    for line in instructions:
        stacks1 = move_crates(stacks1, line, 1)
        stacks2 = move_crates(stacks2, line, 2)

    return get_top_crates(stacks1), get_top_crates(stacks2)


if __name__ == "__main__":
    print(main("day05/test-data.txt"))  # CMZ, MCD
    print(main("day05/data.txt"))  # HNSNMTLHQ, RNLFDJMCT
