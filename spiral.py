# For 3-by-3:

# >>> spiral(3)
# (0, 0)
# (1, 0)
# (2, 0)
# (2, 1)
# (2, 2)
# (1, 2)
# (0, 2)
# (0, 1)
# (1, 1)

# >>> spiral(4)
# (0, 0)
# (1, 0)
# (2, 0)
# (3, 0)
# (3, 1)
# (3, 2)
# (3, 3)
# (2, 3)
# (1, 3)
# (0, 3)
# (0, 2)
# (0, 1)
# (1, 1)
# (2, 1)
# (2, 2)
# (1, 2)

def spiral(matrix_size):

    # add x until 3(matrix_size - 1)
    # add y until 3(matrix_size - 1)
    # subtract x until 0(min_x)
    # subtract y until 1(min_y + 1, new min_y)
    # add one to x, now new min_x
    # repeat

    for box in range(matrix_size // 2):
        top = box
        left = box
        bottom = matrix_size - box - 1
        right = matrix_size - box - 1

        for x in range(left, right):
            print((x, top))

        for y in range(top, bottom):
            print((right, y))
        
        for x in range(right, left, -1):
            print((x, bottom))

        for y in range(bottom, top, -1):
            print((left, y))

    if matrix_size % 2 != 0:
        print((matrix_size//2, matrix_size//2))

  
spiral(3)


