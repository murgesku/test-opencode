#!/usr/bin/env python3

def main():
    import math
    from itertools import combinations

    from typing import TextIO

    # таблица смещений на вектора в исходном текстовом файле
    vec_offsets = []

    # первый проход: заполняем таблицу смещений
    with open("vector.csv", 'r') as f:
        pos = 0
        while f.readline():
            vec_offsets.append(pos)
            pos = f.tell()
    
    n = len(vec_offsets)


    def get_vec(f: TextIO, i: int) -> list[float]:
        """
        Функция для чтения вектора по индексу из файла
        """
        f.seek(vec_offsets[i])
        line = f.readline()
        vec = [float(x) for x in line.split(',')]
        return vec


    distances: list[float] = []
    max_dist: tuple[int, int, float] = None
    min_dist: tuple[int, int, float] = None

    # второй проход: заполняем таблицу расстояний
    # выбираем попарно векторы, читаем из файла, считаем расстояние
    with open("vector.csv", 'r') as f:
        for index_a, index_b in combinations(range(n), 2):
            vec_a = get_vec(f, index_a)
            vec_b = get_vec(f, index_b)
            
            dist = math.dist(vec_a, vec_b)
            distances.append(dist)

            if (max_dist is None) or (dist > max_dist[2]):
                max_dist = (index_a, index_b, dist)
            
            if (min_dist is None) or (dist < min_dist[2]):
                min_dist = (index_a, index_b, dist)
    
    assert(len(distances) == math.comb(n, 2))
    
    print(f"min distance: {min_dist}")
    print(f"max distance: {max_dist}")

    from matplotlib import pyplot
    import numpy as np

    # рисуем гистограмму с шагом 0.1
    pyplot.hist(distances, bins=np.arange(min_dist[2], max_dist[2], 0.1))
    pyplot.xticks(np.arange(min_dist[2], max_dist[2], 0.5))
    
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