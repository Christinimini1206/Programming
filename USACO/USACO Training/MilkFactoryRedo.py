"""
Input:
4
3 1
3 2
4 1
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

# print(direct)

# Note all the possible vertices
vertices = []
for v in range(N):
    vertices.append(0)

# Check which vertices have the most count of possibilities
for p in range(len(direct)):
    vertices[direct[p][1] - 1] += 1

# Check for -1 case
case = 0
for c in range(len(vertices)):
    if vertices[c] == 0:
        case += 1
if case == N:
    print(-1)
else:
    print(vertices.index(max(vertices)) + 1)