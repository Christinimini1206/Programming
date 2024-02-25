"""
8, A, D, D, A, D, D, A, A, 2
4, A, A, A, A, 2
5, A, D, D, A, D, 3
6, A, A, D, D, A, D, 4
8, D, A, A, D, D, A, D, D, 5

8, A, D, D, A, D, D, A, A, 3
9, A, A, D, D, A, D, D, A, A, 4
10, A, A, D, D, A, D, D, A, A, D, 5
1, D, 6
6, A, D, D, D, D, A, 6
"""


def template(num):
    cellsNew = []
    for new in range(0, num):
        cellsNew.append('')
    cellsNew.insert(0, 'Dnon')
    cellsNew.append('Dnon')
    return cellsNew


# Input
lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    lines[a][0], lines[a][-1] = int(lines[a][0]), int(lines[a][-1])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    gridN, cells, generation = line[0], line[1:len(line) - 1], line[-1]
    cells.insert(0, 'Dnon')
    cells.append('Dnon')
    # Make a template with the length of the cells
    cellsNew = template(gridN)
    # Running code for each cell
    for gene in range(0, generation):
        if gene != 0:
            cells = cellsNew
            cellsNew = template(gridN)
        for cell in range(1, gridN + 1):
            # Next alive cell
            if cells[cell - 1] == 'A' and cells[cell + 1] == 'D':  # Left alive, right dead
                cellsNew[cell] = 'A'
            elif cells[cell - 1] == 'A' and cells[cell + 1] == 'Dnon':  # Left alive, right dead non
                cellsNew[cell] = 'A'
            elif cells[cell - 1] == 'D' and cells[cell + 1] == 'A':  # Left dead, right alive
                cellsNew[cell] = 'A'
            elif cells[cell - 1] == 'Dnon' and cells[cell + 1] == 'A':  # Left dead non, right alive
                cellsNew[cell] = 'A'
            # Next dead cell
            if cells[cell - 1] == 'A' and cells[cell + 1] == 'A':  # Left alive, right alive
                cellsNew[cell] = 'D'
            elif cells[cell - 1] == 'D' and cells[cell + 1] == 'D':  # Left dead, right dead
                cellsNew[cell] = 'D'
            elif cells[cell - 1] == 'D' and cells[cell + 1] == 'Dnon':  # Left dead, right dead non
                cellsNew[cell] = 'D'
            elif cells[cell - 1] == 'Dnon' and cells[cell + 1] == 'D':  # Left dead non, right dead
                cellsNew[cell] = 'D'
            elif cells[cell - 1] == 'Dnon' and cells[cell + 1] == 'Dnon':  # Left dead non, right dead non
                cellsNew[cell] = 'D'
    # Print the final string
    final = ''
    for fin in range(1, gridN + 1):
        final += cellsNew[fin]
    print(final)
