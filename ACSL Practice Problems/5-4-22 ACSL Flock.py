"""
3,1,3,5,3
3,1,3,5,7
7,1,3,4,6,8,9,10,3

4,4,5,6,7,4
4,1,4,8,10,5
4,2,8,9,10,6
6,3,4,6,7,9,10,5
4,7,8,9,10,7
"""

# Input
lines = []
for a in range(0, 3):
    lines.append(input().split(','))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    birdN, position, stages = line[0], line[1:len(line) - 1], line[-1]
    # Move the birds
    for stage in range(0, stages - 1):  # Number of stages
        moved = 0
        if position[-1] == 10 and position[0] > 1:
            position.insert(0, 1)
            position.pop()
            moved = 1
        for move in range(moved, len(position)):
            # Move right
            if move < len(position) - 1:
                if position[move] + 1 < position[move + 1]:
                    position[move] += 1
            elif move == len(position) - 1:
                if position[-1] < 10:
                    position[-1] += 1
    # Final string
    final = ''
    for fin in range(0, len(position) - 1):
        final += str(position[fin])
        final += ','
    final += str(position[-1])
    print(final)
    '''# Create the grid
    grid = []
    for birds in range(0, 10):
        grid.append('')
    # Put 'B' on the bird positions
    for pos in range(0, len(position)):
        grid[position[pos] - 1] = 'B'
    # Move the birds
    for stage in range(0, stages):  # Number of stages
        for '''