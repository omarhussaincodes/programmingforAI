# Linear Algebra Functions:-
matrix = [[2, -1, 3],
          [4, 3, 1],
          [9, 1, 2]
          ]
vec1 = [-4, 5, 10]
vec2 = [1, 2, 3]
matrix1 = [[1, -1, 1],
           [2, 1, 1],
           [7, 1, 3]
           ]
matrix2 = [[1, -2, 1],
           [1, 1, 2],
           [3, 0, 6]
           ]

def transpose_matrix(matrix):
    print(len(matrix),"===")
    for i in range(len(matrix)):
        res = [] 
        for j in range(len(matrix[i])):
            print("i", matrix[i][j]) # row value
            # print("i+1", matrix[i+1][j])
            # print("i+2", matrix[i+2][j])
            res.append(matrix[i][j])
    
    return res

def vector_subtraction(vec1, vec2):
    if len(vec1) != len(vec2):
        return "Cannot perform vector subtraction for unequal dimensions."

    result = 0
    for i in range(len(vec1)):
        diff = vec1[i] - vec2[i]
        result += diff

    return result

def element_wise_matrix_multiply(mat1, mat2):
    pass

print("Transpose Matrix:",transpose_matrix(matrix))
print("Vector Sum:",vector_subtraction(vec1, vec2))
print("Element Wise Matrix:",element_wise_matrix_multiply(matrix1, matrix2))
