"""
Day 1: Calorie Counting
"""

def get_data(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f]


def get_elves(data):
    elves = []
    calories = []
    for line in data:
        if line == '':
            elves.append(calories)
            calories = []
        else:
            calories.append(int(line))
    return elves


def count_calories(elves):
    return [sum(elf) for elf in elves]


def sort_ascending(elves):
    elves.sort()
    return elves


def main():
    data = get_data("data.txt")
    elves = count_calories(get_elves(data))
    sorted_elves = sort_ascending(elves)

    max_calories = sorted_elves[-1] # part one
    top_three = sum(sorted_elves[-3:]) # part two

    return max_calories, top_three


print(main())
