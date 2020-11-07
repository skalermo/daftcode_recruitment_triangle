from random import randint


def generate(rows: int):
    for i in range(1, rows+1):
        numbers_row = []
        for j in range(i):
            numbers_row.append(str(randint(1, 9)))
        print(''.join([' ' * (rows - i), ' '.join(numbers_row), ' ' * (rows - i)]))


def main():
    n = 500
    generate(n)


if __name__ == '__main__':
    main()
