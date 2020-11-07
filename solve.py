import time
from PathTree import PathTree, Node


def extract_tree_from(filename):
    triangle = []
    with open(filename, 'r') as fh:
        for line in fh:
            triangle.append(list(map(lambda x: int(x), line.split())))
    return triangle


def main():
    problems = [
        'problems/very_easy.txt',
        'problems/easy.txt',
        'problems/medium.txt',
        'problems/hard.txt'
    ]
    triangle = extract_tree_from(problems[0])
    tree = PathTree()
    for nodes in triangle:
        tree.add_leaves([Node(x) for x in nodes])

    start = time.time()
    path, cost = tree.find_best_path()
    end = time.time()
    print(cost, path)
    print(f'Time consumed: {end - start}')


if __name__ == "__main__":
    main()
