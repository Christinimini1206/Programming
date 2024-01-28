"""
Input:
3
1 2
3 2
"""

"""
1. By using N, create an empty 2D list representing matrix
2. Fill out the matrix according to the directions listed
3. Use two for loops to go through all the points (vertices being 
compared).
4. If the two sets of numbers (for loop #'s) matches the set from input,
put 1 in specific point in the matrix. Else, put 0. 
5. By looking vertically (columns), get the minimal vertex possible and
print it.
"""

# Get the input
N = int(input())
direct = []
for a in range(N - 1):
    direct.append(list(map(int, input().split(" "))))

# Create an empty matrix
matrix, secMat = [], []
for row in range(N):
    matrix.append([])
    secMat.append([])
    for item in range(N):
        matrix[row].append(0)
        secMat[row].append(0)

# Fill the matrix out with the input
for check in range(len(direct)):
    way = direct[check]
    matrix[way[0] - 1][way[1] - 1] = 1

# Fill the self loop
for v in range(N):
    matrix[v][v] = 1

# Create the second matrix to compare
for sr in range(N):
    for si in range(N):
        secMat[si][sr] = matrix[sr][si]

for f in range(1, N):
    # Multiply the matrices
    ind = 0
    for mr in range(N):
        for mi in range(N):
            row1 = matrix[mr]
            col1 = secMat[ind]
            addN = 0
            for mult in range(N):
                addN += row1[mult] * col1[mult]
            matrix[mr][mi] = addN

# Find the column with the most number of ways
vertex = 1
for fr in range(N):
    notZero = 0
    for fi in range(N):
        x = matrix[fi][fr]
        if x == 0:
            vertex += 1
            break
        else:
            notZero += 1
    if notZero == N:
        break
'''
print("")
print(matrix)
print(secMat)
print(multMat)
print(vertices)
'''

if vertex > N:
    print(-1)
else:
    print(vertex)
