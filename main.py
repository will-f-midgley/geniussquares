# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
completed = 0


def create_grid(o):
    g = []
    for i in range(0, 6):
        g.append([])
        for j in range(0, 6):
            if [i, j] in o:
                g[i].append(1)
            else:
                g[i].append(0)
    return g


def get_blocks():
    blue = [[[0, 0]]]
    green = [[[0, 0], [0, 1], [1, 1], [1, 0]]]
    brown = [[[0, 0], [0, 1]], [[0, 0], [1, 0]]]
    orange = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]]]
    cyan = [[[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]], [[1, 0], [1, 1], [1, 2], [0, 2]],
            [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]], [[0, 0], [1, 0], [2, 0], [0, 1]],
            [[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [1, 2], [0, 2]]]
    grey = [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
    yellow = [[[0, 0], [0, 1], [1, 1], [0, 2]], [[1, 0], [1, 1], [0, 1], [1, 2]], [[0, 0], [1, 0], [1, 1], [2, 0]],
              [[0, 1], [1, 1], [1, 0], [1, 2]]]
    purple = [[[0, 0], [0, 1], [1, 1]], [[0, 0], [0, 1], [1, 0]], [[1, 0], [1, 1], [0, 1]], [[0, 0], [1, 0], [1, 1]]]
    red = [[[0, 0], [0, 1], [1, 1], [1, 2]], [[1, 0], [1, 1], [0, 1], [0, 2]], [[0, 0], [1, 0], [1, 1], [2, 1]],
           [[0, 1], [1, 0], [1, 1], [2, 0]]]

    return [red, green, brown, orange, cyan, grey, yellow, purple, blue]


def print_grid(g):
    print('\n', g[0], '\n', g[1], '\n', g[2], '\n', g[3], '\n', g[4], '\n', g[5])


def place_blocks(bs, g, n, g3, c):
    if n == 9:
        # printGrid(g3)
        c = c + 1
        return c
    r = bs[n]

    for b in r:
        for i in range(0, 6):
            for j in range(0, 6):
                failed = False
                g2 = [row[:] for row in g]
                g4 = [row[:] for row in g3]

                for x in range(0, len(b)):
                    if i + int(b[x][0]) > 5 or j + int(b[x][1]) > 5:
                        failed = True
                    if not failed:
                        if g2[i + b[x][0]][j + b[x][1]] == 1:
                            failed = True
                        g2[i + b[x][0]][j + b[x][1]] = 1
                        g4[i + b[x][0]][j + b[x][1]] = n + 2
                if not failed:
                    c = place_blocks(bs, g2, n + 1, g4, c)

    return c


if __name__ == '__main__':
    obstacles = [[0, 0], [1, 2], [3, 1], [5, 3], [3, 4], [4, 5], [1, 4]]
    grid = create_grid(obstacles)
    blocks = get_blocks()
    print_grid(grid)
    g6 = [row[:] for row in grid]
    total = 0
    total = place_blocks(blocks, grid, 0, g6, total)
    print(total)
