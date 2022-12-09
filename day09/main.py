"""
Day 9: Rope Bridge
"""

import math

DIRECTIONS = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}


def get_data(filename):
    with open(filename) as f:
        return [line.split(" ") for line in f.read().split("\n")]


def move(leader, follower, move_leader=None):
    follower_has_moved = False
    if move_leader:
        leader[0] += move_leader[0]
        leader[1] += move_leader[1]

    difference = [leader[0] - follower[0], leader[1] - follower[1]]
    if abs(difference[0]) > 1 or abs(difference[1]) > 1:
        move_follower = [
            math.floor(difference[0] / 2)
            if difference[0] < 0
            else math.ceil(difference[0] / 2),
            math.floor(difference[1] / 2)
            if difference[1] < 0
            else math.ceil(difference[1] / 2),
        ]
        follower[0] += move_follower[0]
        follower[1] += move_follower[1]
        follower_has_moved = True

    return leader, follower, follower_has_moved


def all_moves(data, num_of_tails):
    head = [0, 0]
    tails = [[0, 0] for _ in range(num_of_tails)]
    visited = [[*tails[-1]]]

    for line in data:
        for _ in range(int(line[1])):
            head, tails[0], follower_has_moved = move(head, tails[0], DIRECTIONS[line[0]])

            for i in range(len(tails) - 1):
                if follower_has_moved:
                    tails[i], tails[i + 1], follower_has_moved = move(tails[i], tails[i + 1])

            if tails[-1] not in visited:
                visited.append([*tails[-1]])

    return len(visited)


def main(filename):
    data = get_data(filename)
    return all_moves(data, 1), all_moves(data, 9)


if __name__ == "__main__":
    print(main("day09/test-data.txt"))  # 13, 1
    print(main("day09/test-data2.txt"))  # 88, 36
    print(main("day09/data.txt"))  # 5878, 2405
