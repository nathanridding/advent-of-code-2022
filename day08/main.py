"""
Day 8: Treetop Tree House
"""

import itertools


def get_data(filename):
    """
    Reads the data from a given filename and formats it as a matrix of integers
    """
    with open(filename) as f:
        return [[int(tree) for tree in line] for line in f.read().split("\n")]


def check_tree(data, row, col, direction, limit):
    """
    For a given direction, returns a tuple of whether the tree is visible from the outside (bool) and
    how many trees can be seen from the tree (int)
    """
    tree = data[row][col]
    view_distance = 0
    while True:
        if direction[0] != 0 and row == limit or direction[1] != 0 and col == limit:
            return True, view_distance
        row += direction[0]
        col += direction[1]
        if tree <= data[row][col]:
            return False, view_distance + 1
        view_distance += 1


def main(filename):
    """
    Counts the number of trees that are visible from outside of the forest, and finds the value of
    the highest scenic score out of all trees
    """
    data = get_data(filename)

    height = len(data)
    width = len(data[0])
    visible_count = 0
    max_scenic_score = 0

    for row, col in itertools.product(range(height), range(width)):
        visible = False

        # up
        result = check_tree(data, row, col, (-1, 0), 0)
        visible = result[0] or visible
        scenic_score = result[1]
        # down
        result = check_tree(data, row, col, (1, 0), height - 1)
        visible = result[0] or visible
        scenic_score *= result[1]
        # left
        result = check_tree(data, row, col, (0, -1), 0)
        visible = result[0] or visible
        scenic_score *= result[1]
        # right
        result = check_tree(data, row, col, (0, 1), width - 1)
        visible = result[0] or visible
        scenic_score *= result[1]

        # part 1
        if visible:
            visible_count += 1
        # part 2
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

    return visible_count, max_scenic_score


if __name__ == "__main__":
    print(main("day08/test-data.txt"))  # 21, 8
    print(main("day08/data.txt"))  # 1809, 479400
