"""
1. Identify the location of B, R, and L
2. Compare the location of B and L
- If B is at the higher place, go down
- If B is at the lower place, go up
3. Get the distance between B and L
- |y of B - y of L| + ||
"""

"""
Input:
..........
..........
..........
.....L....
..........
..........
.....B....
..........
.....R....
..........
"""

grid = []
for a in range(10):
    grid.append(list(input()))

# Find the location of B, R, and L
b, r, l = 0, 0, 0
for row in range(10):
    for it in range(10):
        if grid[row][it] == "B":
            b = [row, it]
        elif grid[row][it] == "R":
            r = [row, it]
        elif grid[row][it] == "L":
            l = [row, it]

# Get the general distance
distance = abs(b[0] - l[0]) + abs(b[1] - l[1]) - 1
aa, bb = [0, 1], [1, 0]

for x in range(2):
    # Check if all B, R, and L are aligned together horizontally/vertically
    if (b[aa[x]] == r[aa[x]] == l[aa[x]]):
        if ((b[bb[x]] < r[bb[x]] < l[bb[x]]) or (l[bb[x]] < r[bb[x]] < b[bb[x]])): # R is between B and L
            distance += 2

print(distance)
