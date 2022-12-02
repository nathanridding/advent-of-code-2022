"""
Day 2: Rock Paper Scissors

A - Rock
B - Paper
C - Scissors

A < B < C < A
"""

VALUES = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}


def get_data(filename):
    with open(filename) as f:
        return [line.split(" ") for line in f.read().split("\n")]


def part_one(player_one, player_two):
    if player_two == (player_one - 1) % 3:  # lose
        score = 0 + player_two + 1
    elif player_two == player_one:  # draw
        score = 3 + player_two + 1
    elif player_two == (player_one + 1) % 3:  # win
        score = 6 + player_two + 1
    return score


def part_two(player_one, outcome):
    player_two = (player_one + outcome - 1) % 3
    return player_two + 1 + 3 * outcome


def main():
    data = get_data("day02/data.txt")

    part_one_score = 0
    part_two_score = 0

    for line in data:
        part_one_score += part_one(VALUES[line[0]], VALUES[line[1]])
        part_two_score += part_two(VALUES[line[0]], VALUES[line[1]])

    return part_one_score, part_two_score


if __name__ == "__main__":
    print(main())
