import sys
import time
import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='main.py',
                                     description='Program to solve triangle problem using chosen solver implementation')

    parser.add_argument('filename', type=str, help='File to solve')
    parser.add_argument('-r', action='store_true', default=False, help='Use solver implemented in Rust')
    return parser.parse_args()


def main():
    args = parse_args()

    if args.r:
        try:
            from triangle_solver_lib import solve_fast as solve
        except ImportError:
            print('Cannot find "triangle_solver_lib.so". Falling back to python solver')
            from solver import solve
    else:
        from solver import solve

    filename = sys.argv[1]

    start = time.time()
    cost, path = solve(filename)
    end = time.time()
    print(cost, path)
    print(f'Elapsed: {(end - start):.3}s')


if __name__ == "__main__":
    main()
