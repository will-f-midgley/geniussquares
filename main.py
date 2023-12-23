# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def makeGrid(obstacles):
    grid = []
    for i in range(0, 6):
        grid.append([])
        for j in range(0, 6):
            if [i, j] in obstacles:
                grid[i].append(1)
            else:
                grid[i].append(0)
    return grid


def getBlocks():
    blue = [[[0, 0]]]
    green = [[[0, 0], [0, 1], [1, 1], [1, 0]]]
    brown = [[[0, 0], [0, 1]],[[0,0],[1,0]]]
    orange = [[[0, 0], [0, 1], [0, 2]],[[0,0],[1,0],[2,0]]]
    cyan = [[[0, 0], [0, 1], [0, 2], [1, 0]],[[0, 0], [0, 1], [1, 1], [1, 2]],[[1, 0], [1, 1], [1, 2], [0, 2]],[[0, 0], [1, 0], [2, 0], [2, 1]],[[0, 0], [1, 0], [1, 1], [1, 2]],[[0, 0], [1, 0], [2, 0], [0, 1]],[[0, 0], [0, 1], [0, 2], [1, 2]],[[0, 1], [1, 1], [1, 2], [0, 2]]]
    grey = [[[0, 0], [0, 1], [0, 2], [0, 3]],[[0,0],[1,0],[2,0],[3,0]]]
    yellow = [[[0, 0], [0, 1], [1, 1], [0, 2]],[[1, 0], [1, 1], [0, 1], [1, 2]],[[0, 0], [1, 0], [1, 1], [2, 0]],[[0, 1], [1, 1], [1, 0], [1, 2]]]
    purple = [[[0, 0], [0, 1], [1, 1]],[[0, 0], [0, 1], [1, 0]],[[1, 0], [1, 1], [0, 1]],[[0, 0], [1, 0], [1, 1]]]
    red = [[[0, 0], [0, 1], [1, 1], [1, 2]],[[1, 0], [1, 1], [0, 1], [0, 2]],[[0, 0], [1, 0], [1, 1], [2, 1]],[[0, 1], [1, 0], [1, 1], [2, 0]]]

    return [red, green, brown, orange, cyan, grey, yellow, purple, blue]

def rotateBlock():
    blue = [[0, 0]]
    green = [[0, 0], [0, 1], [1, 1], [1, 0]]
    brown = [[0, 0], [1, 0]]
    orange = [[0, 0], [1, 0], [2, 0]]
    cyan = [[0, 0], [0, 1], [0, 2], [1, 0]]
    grey = [[0, 0], [0, 1], [0, 2], [0, 3]]
    yellow = [[0, 0], [0, 1], [1, 1], [0, 2]]
    purple = [[0, 0], [0, 1], [1, 1]]
    red = [[0, 0], [0, 1], [1, 1], [1, 2]]

def printGrid(g):
    print('\n', g[0], '\n', g[1], '\n', g[2], '\n', g[3], '\n', g[4], '\n', g[5])


def placeBlock(bs, g, n, g3):
    if n == 9:
        print("DONE DONE")
        printGrid(g3)
        return -1
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
                    if failed == False:
                        if g2[i + b[x][0]][j + b[x][1]] == 1:
                            failed = True
                        g2[i + b[x][0]][j + b[x][1]] = 1
                        g4[i + b[x][0]][j + b[x][1]] = n+2
                if failed == False:
                    # print(b, "\n")
                    # printGrid(g2)
                    placeBlock(bs, g2, n + 1,g4)



    return -1


            # def rotateBlock(b,angle):
# if angle =

if __name__ == '__main__':
    obstacles = [[0, 0], [0, 2], [4, 0], [4, 2], [4, 4], [3, 3], [3, 5]]
    grid = makeGrid(obstacles)
    blocks = getBlocks()
    printGrid(grid)
    g6 = [row[:] for row in grid]
    placeBlock(blocks, grid, 0, g6)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
