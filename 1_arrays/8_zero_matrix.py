"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def zero_matrix(matrix: list[list[int]]):
    rows = set()
    cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        target_row = matrix[row]
        for i in range(len(target_row)):
            target_row[i] = 0

    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix
            