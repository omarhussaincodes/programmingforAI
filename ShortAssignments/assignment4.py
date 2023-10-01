# Linear Algebra Functions:-
matrix = [[2, -1, 3],
          [4, 3, 1],
          [9, 1, 2]
          ]

matrix_a = [[1, 2, 3],
            [4, 5, 6],
            ]


def transpose_matrix(matrix):

    # figure out rows and columns
    rows = len(matrix)
    columns = len(matrix[0])

    # create empty matrix with the figured rows and columns
    # here in order to ensure that for a non-square matrix, we need to transpose such that m*n rows*cols will n*m cols*rows for resulting tranpose
    transpose = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transpose[j][i] = matrix[i][j]

    return transpose

# By list comprehension


def create_empty_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

# With nested loops


def create_empty_mat(rows, cols):
    empty_matrix = []

    for _ in range(rows):
        row = [0] * cols
        empty_matrix.append(row)

    return empty_matrix


vec1 = [-4, 5, 10]
vec2 = [1, 2, 3]


def vector_subtraction(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError(
            "Cannot perform vector subtraction for unequal dimensions.")

    result = 0
    for i in range(len(vec1)):
        diff = vec1[i] - vec2[i]
        result += diff

    return result


matrix1 = [[1, -1, 1],
           [2, 1, 1],
           [7, 1, 3]
           ]
matrix2 = [[1, -2, 1],
           [1, 1, 2],
           [3, 0, 6]
           ]


# Hadamard product or square matrix multiplication
def element_wise_matrix_multiply(mat1, mat2):

    if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
        result = [[0 for _ in range(len(mat1))] for _ in range(len(mat1[0]))]
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                result[i][j] = mat1[i][j] * mat2[i][j]

        return result
    else:
        print("Hamdamard product not possible for non-square matrices. Please pass in square matrices.")
        raise ValueError(
            "Matrices must have the same dimensions for element-wise multiplication.")


print(create_empty_mat(3, 2))
print(create_empty_matrix(2, 3))
print("Transpose of Matrix (3*3):", transpose_matrix(matrix))
print("Transpose of Matrix (3*2):", transpose_matrix(matrix_a))
print("Vector Sum:", vector_subtraction(vec1, vec2))
print("Element Wise Matrix:", element_wise_matrix_multiply(matrix1, matrix2))
