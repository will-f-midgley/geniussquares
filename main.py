# Function to create initial grid and place appropriate obstacles
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
    blue = [[0, 0]]
    green = [[0, 0], [0, 1], [1, 1], [1, 0]]
    brown = [[0, 0], [1, 0]]
    orange = [[0, 0], [1, 0], [2, 0]]
    cyan = [[0, 0], [0, 1], [0, 2], [1, 0]]
    grey = [[0, 0], [0, 1], [0, 2], [0, 3]]
    yellow = [[0, 0], [0, 1], [1, 1], [0, 2]]
    purple = [[0, 0], [0, 1], [1, 1]]
    red = [[0, 0], [0, 1], [1, 1], [1, 2]]

    all_blocks = [red, green, brown, orange, cyan, grey, yellow, purple, blue]
    for i in range(0, len(all_blocks)):
        all_blocks[i] = transform_block(all_blocks[i])
    return all_blocks


# Helper function for individual blocks
def transform_block(block):
    # List of all possible transformations in matrix form: Rotations through 90, 180 and 270 degrees as well as
    # reflections in the line y = 0 on top of these.
    matrices = [[0, -1, 1, 0], [-1, 0, 0, -1], [0, 1, -1, 0], [0, 1, 1, 0], [-1, 0, 0, 1], [0, -1, -1, 0],
                [1, 0, 0, -1]]
    transformations = [block]
    for i in matrices:
        temp = apply_transformation(block, i)
        if temp not in transformations:
            transformations.append(temp)
    print(transformations)
    return transformations


# Applies matrix onto block and transitions onto positive axis
def apply_transformation(b, m):
    new_b = []
    x_low = 0
    y_low = 0
    for i in range(0, len(b)):
        new_b.append([b[i][0] * m[0] + b[i][1] * m[1], b[i][0] * m[2] + b[i][1] * m[3]])
        x_low = min(new_b[i][0], x_low)
        y_low = min(new_b[i][1], y_low)
    for i in range(0, len(b)):
        new_b[i] = [new_b[i][0] - x_low, new_b[i][1] - y_low]
    return sorted(new_b)


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
                new_grid = [row[:] for row in g]
                new_temp_grid = [row[:] for row in g3]

                for x in range(0, len(b)):
                    if i + int(b[x][0]) > 5 or j + int(b[x][1]) > 5:
                        failed = True
                    if not failed:
                        if new_grid[i + b[x][0]][j + b[x][1]] == 1:
                            failed = True
                        new_grid[i + b[x][0]][j + b[x][1]] = 1
                        new_temp_grid[i + b[x][0]][j + b[x][1]] = n + 2
                if not failed:
                    c = place_blocks(bs, new_grid, n + 1, new_temp_grid, c)

    return c


if __name__ == '__main__':
    obstacles = [[0, 0], [1, 2], [3, 1], [5, 3], [3, 4], [4, 5], [1, 4]]
    grid = create_grid(obstacles)
    blocks = get_blocks()
    print_grid(grid)
    temp_grid = [row[:] for row in grid]
    total = place_blocks(blocks, grid, 0, temp_grid, 0)
    print(total)
