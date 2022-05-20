#!/usr/bin/env python3

def main(n: int, m: int):
    import random
    import csv

    if not ((500 < n <= 1000) and (10 < m <= 500)):
        print("Error: 500 < N <= 1000, 10 < m <= 500")
        print("Aborted")
        return

    with open("vector.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(n):
            writer.writerow([random.uniform(-1.0, 1.0) for j in range(m)])

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Creates file 'vector.csv' with list of N random vectors of m elements. "
        "Element values are in range [-1.0, 1.0]."
    )
    parser.add_argument(metavar="N", dest="n", type=int, help="Number of vectors, 500 < N <= 1000")
    parser.add_argument(metavar="m", dest="m", type=int, help="Number of elements, 10 < m <= 500")

    args = parser.parse_args()

    main(args.n, args.m)
