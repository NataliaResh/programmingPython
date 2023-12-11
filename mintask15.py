import matplotlib.pyplot as plt
import numpy as np
from random import choice
from time import time

PLOT = True


def generate_field(size):
    generate_list = [False, True]
    if NUMPY:
        new_field = np.random.choice(generate_list, size=(size, size))
    else:
        new_field = [[choice(generate_list) for _ in range(size)] for _ in range(size)]
    return new_field


def neighbour_count(field, x, y):
    size = len(field)
    return sum(field[(x + i + size) % size][(y + j + size) % size] for i in range(-1, 2) for j in range(-1, 2) if
               i != 0 or j != 0)


def iter_life(field):
    size = len(field)
    if NUMPY:
        new_field = np.zeros((size, size), dtype=int)
    else:
        new_field = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            count = neighbour_count(field, i, j)
            if field[i][j]:
                new_field[i][j] = 2 <= count <= 3
            elif count == 3:
                new_field[i][j] = True
    return new_field


def main():
    n = 512
    start = time()
    main_field = generate_field(n)
    if PLOT:
        plt.ion()
        fig, ax = plt.subplots(figsize=(6, 6), sharex="col")
        for _ in range(128):
            if PLOT:
                ax_x = [i for i in range(n) for j in range(n) if main_field[i][j]]
                ax_y = [j for i in range(n) for j in range(n) if main_field[i][j]]
                ax.clear()
                ax.scatter(ax_x, ax_y, s=1, marker='s')
                plt.pause(10 ** -5)
            main_field = iter_life(main_field)
    else:
        for _ in range(128):
            main_field = iter_life(main_field)
    end = time()
    if PLOT:
        plt.close()
    return end - start


NUMPY = True
with_np = main()
NUMPY = False
without_np = main()
print(with_np, without_np)
plt.ion()
fig, ax = plt.subplots(figsize=(6, 6), sharex="col")
ax.clear()
ax.bar(["with np", "without np"], [with_np, without_np])
plt.pause(10)
plt.close()
