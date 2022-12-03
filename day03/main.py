"""
Day 3: Rucksack Reorganization
"""

def get_data(filename: str) -> list:
    with open(filename) as f:
        return [list(line) for line in f.read().split("\n")]


def convert_letter(letter: str) -> int:
    return ord(letter) - 96 if letter.lower() == letter else ord(letter) - 38


def find_duplicate_items(group: list) -> list:
    if not group:
        return []
    elif len(group) == 1:
        return group[0]
    duplicate_items = set(filter(lambda item: item in group[1], group[0]))
    return find_duplicate_items([list(duplicate_items), *group[2:]])


def format_data(data: list, type: int) -> list:
    if type == 1:
        return [[line[: len(line) // 2], line[len(line) // 2 :]] for line in data]
    elif type == 2:
        return [data[i : i + 3] for i in range(0, len(data), 3)]


def get_priority_sum(data: list) -> int:
    priority_sum = 0
    for group in data:
        duplicate_items = find_duplicate_items(group)
        priority_sum += sum(convert_letter(item) for item in duplicate_items)
    return priority_sum


def main(filename: str) -> tuple:
    data = get_data(filename)

    data1 = format_data(data, 1)
    data2 = format_data(data, 2)

    return get_priority_sum(data1), get_priority_sum(data2)


if __name__ == "__main__":
    print(main("day03/test-data.txt"))  # (157, 70)
    print(main("day03/data.txt"))       # (7795, 2703)
