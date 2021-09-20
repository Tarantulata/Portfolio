def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()
first = []
second = []
second_i = len(matrix) - 1
for r in range(len(matrix)):
    first.append(matrix[r][r])
    second.append(matrix[r][second_i])
    second_i -= 1

print(f"Primary diagonal: {', '.join(str(x) for x in first)}. Sum: {sum(first)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")
