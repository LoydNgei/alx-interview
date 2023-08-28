#!/usr/bin/python3
"""Finding an Island perimeter"""


def island_perimeter(grid):
    L1 = len(grid)  # The row (Height)
    L2 = len(grid[0])  # The column (Width)

    def dfs(row, col):
        # Check the water bound area
        if row < 0 or row >= L1 or col < 0 or col >= L2 or grid[row][col] == 0:
            return 1

        if grid[row][col] == 1:
            grid[row][col] = 2  # Check repetition on a single cell.Return 0
            return dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + \
                dfs(row, col+1)
        return 0

    perimeter = 0
    for row in range(L1):
        for col in range(L2):
            if grid[row][col] == 1:
                perimeter += dfs(row, col)

    return perimeter
