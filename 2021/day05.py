from utils import read_data
import numpy as np


def day05(data, diag=False):
    grid = np.zeros((1000, 1000))
    for line in data:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            grid[x1, range(y1, y2+1)] += 1
        elif y1 == y2:
            x1, x2 = sorted((x1, x2))
            grid[range(x1, x2+1), y1] += 1
        else:
            if diag:
                add = lambda x1, x2: 1 if x1 < x2 else -1
                x_add, y_add = add(x1, x2), add(y1, y2)
                grid[x1, y1] += 1
                while x1 != x2:
                    x1 += x_add
                    y1 += y_add
                    grid[x1, y1] += 1

    return len(grid[np.where(grid > 1)])

def main():
    data = read_data('./data/day05.txt', typ='coords')

    # PART ONE
    print(day05(data))

    # PART TWO
    print(day05(data, diag=True))


if __name__ == '__main__':
    main()
