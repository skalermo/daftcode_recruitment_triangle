# (1+n)/2 * n - sum of 1..n
# 0
# 1 2
# 3 4 5
# 6 7 8 9
# 10 11 12 13
from Triangle import Triangle


def extract_tree_from(filename):
    tree = []
    levels = 0
    with open(filename, 'r') as fh:
        for line in fh:
            tree.extend(map(lambda x: int(x), line.split()))
            levels += 1
    return tree, levels


def main():
    tasks = [
        'very_easy.txt',
        'easy.txt',
        'medium.txt'
    ]
    tree, levels = extract_tree_from(tasks[2])
    print(tree)
    moves, cost = Triangle(tree, levels).find_best_route()
    print(cost)
    print(moves)


if __name__ == "__main__":
    main()
