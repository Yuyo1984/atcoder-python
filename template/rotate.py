def rotate(grid, direction):
    if direction == 'R':
        grid = grid[::-1]
        grid = list(map(list, zip(*grid)))
    else:
        grid = list(map(list, zip(*grid)))
        grid = grid[::-1]
    return grid

