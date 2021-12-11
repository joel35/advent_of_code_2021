import numpy as np


def main():
    solve(load('input'))


def solve(grid, p1=100, timeout=1000):
    flash_count = 0
    steps = 0

    while grid.any() and steps < timeout:
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
        for coord in zip(*np.where(flash)):
            for xy in get_neighbours(*coord, grid):
                if 10 > grid[xy] > 0:
                    grid[xy] += 1
            grid[coord] = 0
        flash = grid == 10
    return flash_count


def get_neighbours(r, c, grid):
    return [x for x in [(r - 1, c - 1),
                        (r - 1, c),
                        (r - 1, c + 1),
                        (r, c - 1),
                        (r, c + 1),
                        (r + 1, c - 1),
                        (r + 1, c),
                        (r + 1, c + 1)]
            if valid(x, grid)]


def valid(coord, grid):
    return all([
        coord[0] >= 0,
        coord[1] >= 0,
        coord[0] < len(grid),
        coord[1] < len(grid[0])
    ])


if __name__ == '__main__':
    main()
