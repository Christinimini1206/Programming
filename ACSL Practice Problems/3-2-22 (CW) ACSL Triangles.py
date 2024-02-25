import math
"""
5, 5, 2, 2, 6, 8, 8, 12, 7, 10, 1
4, 2, 0, 2, 2, 0, 2, 0, 0
5, 1, 1, 1, 4, 3, 5, 5, 4, 4, 0

4, 1, 2, 2, 4, 4, 3, 3, 1
4, 0, 0, 0, 4, 6, 4, 6, 0
4, 0, 0, 1, 5, 2, 8, 6, 6
5, 0, 0, 1, 5, 2, 8, 6, 6, 8, 4
6, 0, 0, 1, 5, 2, 8, 6, 6, 8, 4, 5, 2
"""


def calcDistance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])
for run in range(0, len(lines)):
    line = lines[run]
    # Divide the numbers into pts
    pts = []
    for divPts in range(1, len(line)):
        if divPts % 2 == 0:
            pts.append([])
            pts[-1].append(line[divPts - 1])
            pts[-1].append(line[divPts])

    # Find the pts that can be used to draw diagonal lines
    ptsD = []
    for diag in range(2, len(pts) - 1):
        ptsD.append(pts[diag])

    # Divide the points used for each triangle
    ptsTriangle = []
    for ptsT in range(1, len(pts) - 1):
        ptsTriangle.append([pts[0]])
        ptsTriangle[-1].append(pts[ptsT])
        ptsTriangle[-1].append(pts[ptsT + 1])

    # Get the side length of each sides of triangle
    lengths = []
    for ptsL in range(0, len(ptsTriangle)):
        lengths.append([])
        lengths[-1].append(calcDistance(ptsTriangle[ptsL][0], ptsTriangle[ptsL][1]))
        lengths[-1].append(calcDistance(ptsTriangle[ptsL][1], ptsTriangle[ptsL][2]))
        lengths[-1].append(calcDistance(ptsTriangle[ptsL][0], ptsTriangle[ptsL][2]))
    # Calculate the areas
    areas = []
    for calcA in range(0, len(lengths)):
        A, B, C = lengths[calcA][0], lengths[calcA][1], lengths[calcA][2]
        S = (A + B + C)/2
        areas.append(math.sqrt(S * (S - A) * (S - B) * (S - C)))
    finalStr = str(round(max(areas), 2))
    print(finalStr + '0')




