"""
Day 1: Calorie Counting
"""

def get_data(filename):
    with open(filename) as f:
        return [line.split("\n") for line in f.read().split("\n\n")]


def sum_calories(elves):
    return [sum(int(calories) for calories in elf) for elf in elves]


def main():
    data = get_data("day01/data.txt")
    elves = sum_calories(data)
    elves.sort()

    max_calories = elves[-1]     # part one
    top_three = sum(elves[-3:])  # part two

    return max_calories, top_three


if __name__ == "__main__":
    print(main())
