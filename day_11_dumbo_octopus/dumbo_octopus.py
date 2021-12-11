import numpy as np


def main():
    solve(load('input'))


def solve(grid, p1=100, timeout=1000):
    flash_count = 0
    steps = 0
    sync = False

    while not sync and steps < timeout:
        steps += 1
        flashes, sync = step(grid)
        flash_count += flashes
        if steps == p1:
            print(f'Part 1: {flash_count}')

    print(f'Part 2: {steps}')


def load(file):
    return np.genfromtxt(file, delimiter=1, dtype=int)


def step(grid):
    grid += 1
    flash_count = 0

    while True:
        flash = grid == 10
        flash_count += flash.sum()

        if not flash.any():
            sync = np.all((grid == 0))
            return flash_count, sync

        for coord in zip(*np.where(flash)):
            neighbours = [n for n in get_neighbours(coord).values() if valid(n, grid) and 10 > grid[n] > 0]

            for r, c in neighbours:
                grid[r][c] += 1

            grid[coord] = 0


def get_neighbours(coord):
    r, c = coord
    return dict(
        nw=(r - 1, c - 1),
        n=(r - 1, c),
        ne=(r - 1, c + 1),
        w=(r, c - 1),
        e=(r, c + 1),
        sw=(r + 1, c - 1),
        s=(r + 1, c),
        se=(r + 1, c + 1),
    )


def valid(coord, grid):
    return all([
        coord[0] >= 0,
        coord[1] >= 0,
        coord[0] < len(grid),
        coord[1] < len(grid[0])
    ])


if __name__ == '__main__':
    main()
