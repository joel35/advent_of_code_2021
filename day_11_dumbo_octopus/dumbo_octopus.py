import numpy as np


def main():
    solve(load('input'))


def solve(grid, p1=100, max=1000):
    flash_count = 0
    steps = 0

    while grid.any() and steps < max:
        steps += 1
        flash_count += step(grid)
        if steps == p1:
            print(f'Part 1: {flash_count}')

    print(f'Part 2: {steps}')


def load(file):
    return np.genfromtxt(file, delimiter=1, dtype=int)


def step(grid):
    grid += 1
    flash_count = 0
    flash = grid == 10

    while flash.any():
        flash_count += flash.sum()
        for flasher_xy in zip(*np.where(flash)):
            grid[flasher_xy] = 0
            for neigh_xy in get_neighbours(*flasher_xy, grid):
                grid[neigh_xy] += 1
        flash = grid == 10
    return flash_count


def get_neighbours(x, y, grid):
    return [xy for xy in [(x - 1, y - 1),
                          (x - 1, y),
                          (x - 1, y + 1),
                          (x, y - 1),
                          (x, y + 1),
                          (x + 1, y - 1),
                          (x + 1, y),
                          (x + 1, y + 1)]
            if valid(*xy, grid)]


def valid(x, y, grid):
    max_x, max_y = grid.shape
    return all([max_x > x >= 0, max_y > y >= 0]) and 10 > grid[x, y] > 0


if __name__ == '__main__':
    main()
