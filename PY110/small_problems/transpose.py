matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(list_of_rows):
    return [list(val) for val in list(zip(*list_of_rows))]

def transpose(matrix):
    transposed_matrix = [[],[],[]]
    for row in matrix:
        for col_no, val in enumerate(row):
            transposed_matrix[col_no].append(val)
    return transposed_matrix

def transpose(matrix):
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])
    
    transposed_matrix = [[],[],[]]
    for row in matrix:
        for col_no, val in enumerate(row):
            transposed_matrix[col_no].append(val)
    return transposed_matrix




new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True