def sum_lowest_path(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            if row == 0 and col == 0:
                tally = 0
            elif row == 0 and col != 0:
                tally = grid[row][col-1]
            elif row != 0 and col == 0:
                tally = grid[row-1][col]
            else:
                left = grid[row][col-1]
                above = grid[row-1][col]
                tally = left if left < above else above
            
            grid[row][col] += tally

    return grid[row][col] 
