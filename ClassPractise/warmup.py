A = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]


def print_flat(inputlist):

    list_A = [item for sublist in inputlist for item in sublist]
    for item in list_A:
        print(item, end=" ")


print_flat(A)

print(f"\n=================")


def print_flatt(input):
    for i in range(len(input)):
        for j in range(len(input)):
            print(input[i][j], end=" ")


print_flatt(A)

print(f"\n=================")

# Write a function that takes a matrix A and returns True if the matrix is square and
# False otherwise.
matrix_A = [
    [1, 4, 5],
    [-5, 8, 9]
]
matrix_B = [
    [3, 2, 1],
    [1, 0, 1],
    [10, 2, 0]
]


def isSquareMatrix(input) -> bool:
    # length of 2D-Array gives number of rows
    rows = len(input)
    columns = 0
    # count of length of item of array  gives number of columns
    for item in input:
        columns = len(item)
        break

    if (rows == columns):
        return True
    else:
        return False


print(isSquareMatrix(matrix_A))
print(isSquareMatrix(matrix_B))
