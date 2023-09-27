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

    if (not isinstance(input, list)):
        return False

    # length of 2D-Array gives number of rows
    rows_len = len(input)
    if rows_len == 0:
        return False

    # count of length of item of array  gives number of columns
    for item in input:
        columns_len = len(item)
        if (not isinstance(item, list) or columns_len != rows_len):
            return False
    return True

print(isSquareMatrix(matrix_A))
print(isSquareMatrix(matrix_B))

# Matrix Addition
A = [
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
]
B = [
    [4, 5, 6],
    [7, 8, 9],
    [-1, 9, 0]
]

def sum_matrix(A, B):
    result = []

    for i in range(len(A)):
        sum_list = []
        for j in range(len(B)):
            print(A[i][j], B[i][j])
            sum = A[i][j] + B[i][j]
            sum_list.append(sum)
        result.append(sum_list)

    return result

print(sum_matrix(A, B))

# dot product of 2 matrices
X = [1, 2, 3]
Y = [4, 5, 6]

def dot_product_vectors(X, Y):

    if (len(X) != len(Y)):
        print("Cannot dot product for unequal sized vectors")
        exit()
    
    result = 0
    for i in range(len(X)):
        product = X[i] * Y[i]
        result += product

    return (result)

print(dot_product_vectors(X, Y))
