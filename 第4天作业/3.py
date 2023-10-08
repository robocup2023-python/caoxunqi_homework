print("请输入第一个3x3矩阵:")
matrix1 = []
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"请输入第{i+1}行第{j+1}列的元素: "))
        row.append(element)
    matrix1.append(row)
matrix2 = []
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"请输入第{i+1}行第{j+1}列的元素: "))
        row.append(element)
    matrix2.append(row)
result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
print("相加后的矩阵:")
for row in result_matrix:
    print(row)