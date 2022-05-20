#!/usr/bin/env python3

def main():
    import math
    from itertools import combinations

    from typing import TextIO

    vectors: list[list[float]] = []

    # считываем векторы из файла
    with open("vector.csv", 'r') as f:
        while line := f.readline():
            vec = [float(x) for x in line.split(',')]
            vectors.append(vec)
    
    n = len(vectors)

    max_dist: tuple[int, int, float] = None
    min_dist: tuple[int, int, float] = None

    # определяем минмальное и максимальное расстояние
    for i, j in combinations(range(n), 2):
        dist = math.dist(vectors[i], vectors[j])

        if (max_dist is None) or (dist > max_dist[2]):
            max_dist = (i, j, dist)
        
        if (min_dist is None) or (dist < min_dist[2]):
            min_dist = (i, j, dist)

    # считаем гистограмму
    # определяем интервалы с шагом 0.1
    x = math.ceil((max_dist[2] - min_dist[2]) / 0.1)
    histogram = [0.0 for _ in range(x)]

    for i, j in combinations(range(n), 2):
        dist = math.dist(vectors[i], vectors[j])
        # аккумулирем в соответствующем интервале
        histogram[math.floor((dist - min_dist[2]) / 0.1)] += 1

    print(f"min distance: {min_dist}")
    print(f"max distance: {max_dist}")
    
    # рисуем гистограмму
    from matplotlib import pyplot

    pyplot.bar(range(x), histogram)
    pyplot.xticks([])
    
    pyplot.savefig("histogram.png")
    pyplot.show()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Reads file 'vector.csv' with list of vectors, "
        "calculates distances between for all pairs of vectors, "
        "for minimum and maximum distances outputs to console corresponding indices of vectors and distance value, "
        "creates distance distribution histogram."
    )
    parser.parse_args()

    main()
    
