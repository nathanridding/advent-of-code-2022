"""
Day 10: Cathode-Ray Tube
"""


def get_data(filename):
    with open(filename) as f:
        return [line.split(" ") for line in f.read().split("\n")]


def increment_cycle(cycle, x, signal_strengths):
    cycle += 1
    if cycle % 40 == 20:
        signal_strengths.append(cycle * x)
    return cycle, x, signal_strengths


def increment_cycle2(cycle, x, output):
    if cycle % 40 == 0:
        output.append("")
    cycle += 1
    output[-1] += "#" if cycle % 40 - 1 in [x - 1, x, x + 1] else "."
    return cycle, x, output


def run_program(data, increment_cycle):
    cycle = 0
    x = 1
    output = []

    for line in data:
        if line[0] == "noop":
            cycle, x, output = increment_cycle(cycle, x, output)
        elif line[0] == "addx":
            cycle, x, output = increment_cycle(cycle, x, output)
            cycle, x, output = increment_cycle(cycle, x, output)
            x += int(line[1])

    return output


def main(filename):
    data = get_data(filename)

    # part 1
    signal_strengths = run_program(data, increment_cycle)
    print(sum(signal_strengths))

    # part 2
    output = run_program(data, increment_cycle2)
    for row in output:
        print(row)
    print()


if __name__ == "__main__":
    main("day10/test-data.txt")  # 13140
    main("day10/data.txt")  # 14220
