import sys
import time

from solver import solve
# from triangle_solver_lib import solve_fast as solve


def main():
    if len(sys.argv) != 2:
        print(f'Usage: solve.py file/to/process')
        return

    filename = sys.argv[1]

    start = time.time()
    cost, path = solve(filename)
    end = time.time()
    print(cost, path)
    print(f'Elapsed: {(end - start):.3}s')


if __name__ == "__main__":
    main()
