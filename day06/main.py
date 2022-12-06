"""
Day 6: Tuning Trouble
"""


def get_data(filename):
    with open(filename) as f:
        return list(f.read())


def get_marker(data, n):
    window = []
    for i in range(len(data)):
        window.append(data[i])
        if len(window) > n:
            window.pop(0)
            if len(set(window)) == len(window):
                return i + 1

def main(filename):
    data = get_data(filename)
    return get_marker(data, 4), get_marker(data, 14)


if __name__ == "__main__":
    print(main("day06/test-data.txt"))  # 7, 19
    print(main("day06/data.txt"))  # 1640, 3613
