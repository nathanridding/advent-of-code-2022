"""
Day 4: Camp Cleanup
"""


def get_data(filename):
    with open(filename) as f:
        return [
            [[int(n) for n in elf.split("-")] for elf in line.split(",")]
            for line in f.read().split("\n")
        ]


def part_one(line):
    return (
        line[0][0] <= line[1][0]
        and line[0][1] >= line[1][1]
        or line[0][0] >= line[1][0]
        and line[0][1] <= line[1][1]
    )


def part_two(line):
    return (
        line[0][0] <= line[1][0] <= line[0][1]
        or line[0][0] <= line[1][1] <= line[0][1]
        or line[1][0] <= line[0][0] <= line[1][1]
        or line[1][0] <= line[0][1] <= line[1][1]
    )


def main(filename):
    data = get_data(filename)
    return sum(1 for line in data if part_one(line)), sum(
        1 for line in data if part_two(line)
    )


if __name__ == "__main__":
    print(main("day04/test-data.txt"))  # 2, 4
    print(main("day04/data.txt"))  # 599, 928
