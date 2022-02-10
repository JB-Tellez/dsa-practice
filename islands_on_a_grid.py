def count_islands(grid):

    island_counter = 0

    visited = set()

    for row, row_list in enumerate(grid):

        for col, _ in enumerate(row_list):

            if is_unvisited_land(row, col, grid, visited):

                island_counter += 1

                explore(row, col, grid, visited)

    return island_counter


def explore(row, col, grid, visited):

    if is_unvisited_land(row, col, grid, visited):

        visited.add((row, col))

        explore(row - 1, col, grid, visited)  # up
        explore(row, col + 1, grid, visited)  # right
        explore(row + 1, col, grid, visited)  # down
        explore(row, col - 1, grid, visited)  # left


def is_unvisited_land(row, col, grid, known):
    if not in_bounds(row, col, grid):
        return False

    if (row, col) in known:
        return False

    if grid[row][col] == 0:
        return False

    return True


def in_bounds(row, col, grid):
    if not 0 <= row < len(grid):
        return False

    if not 0 <= col < len(grid[row]):
        return False

    return True
