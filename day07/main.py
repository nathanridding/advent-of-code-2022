"""
Day 7: No Space Left On Device
"""


def get_data(filename):
    with open(filename) as f:
        return f.read().split("\n")


def get_subtree(tree, path):
    subtree = tree
    for level in path[:-1]:
        subtree = subtree[level]
    return subtree


def create_tree(data):
    tree = {"/": {}}
    path = []
    for line in data:
        if line == "$ cd ..":
            path.pop(-1)

        elif line.startswith("$ cd "):
            path.append(line.split("$ cd ")[1])

        elif not line.startswith("$"):
            value, key = line.split()
            subtree = get_subtree(tree, path)
            subtree[path[-1]][key] = {} if value == "dir" else int(value)

    return tree


def sum_file_size(tree):
    if type(tree) == int:
        return tree
    return sum(sum_file_size(v) for v in tree.values())


def get_dir_sizes(tree):
    dir_sizes = []
    for key, value in tree.items():
        if type(value) == dict:
            dir_sizes.append([key, sum_file_size(value)])
            dir_sizes += get_dir_sizes(value)
    return dir_sizes


def main(filename):
    data = get_data(filename)
    file_structure = create_tree(data)
    # file_structure = {
    #     "/": {
    #         "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
    #         "b.txt": 14848514,
    #         "c.dat": 8504156,
    #         "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
    #     }
    # }

    dir_sizes = get_dir_sizes(file_structure)
    # dir_sizes = [["/", 48381165], ["a", 94853], ["e", 584], ["d", 24933642]]

    return (
        sum(dir[1] for dir in dir_sizes if dir[1] <= 100000),
        min(dir[1] for dir in dir_sizes if dir[1] > dir_sizes[0][1] - 40000000),
    )


if __name__ == "__main__":
    print(main("day07/test-data.txt"))  # 95437, 24933642
    print(main("day07/data.txt"))  # 1206825, 9608311
