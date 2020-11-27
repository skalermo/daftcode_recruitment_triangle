from PathTree import PathTree, Node


def extract_tree_from(filename):
    triangle = []
    with open(filename, 'r') as fh:
        for line in fh:
            triangle.append(list(map(lambda x: int(x), line.split())))
    return triangle


def solve(filename):
    triangle = extract_tree_from(filename)
    tree = PathTree()
    for nodes in triangle:
        tree.add_leaves([Node(x) for x in nodes])

    path, cost = tree.find_best_path()
    # print(cost, path)
    return cost, path
