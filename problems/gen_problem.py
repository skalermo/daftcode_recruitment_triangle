import sys
from random import randint


def generate(rows: int):
    for i in range(1, rows+1):
        numbers_row = []
        for j in range(i):
            numbers_row.append(str(randint(1, 9)))
        print(' ' * (rows - i), ' '.join(numbers_row), ' ' * (rows - i), sep='')


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} number_of_rows')
        return

    n = int(sys.argv[1])
    generate(n)


if __name__ == '__main__':
    main()
