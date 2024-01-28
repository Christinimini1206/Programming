def findNeighbors(pt1, pt2):
    # If the points are next to each other horizontally
    if abs(pt1[0] - pt2[0]) <= 1 and abs(pt1[1] - pt2[1]) <= 1:
        return True
    # If the points are not neighbors
    else:
        return False

# '1,1,2,2,3,2,4,3,4,4,5,5,5,1,0,0'
stringSpl = '1,1,2,2,3,2,4,3,4,4,5,5,5,1,0,0'.split(',')

p = [(i,j) for i in range(1,4) for j in range(1,4)]
p.remove((2,2))
print(p)

for i in p:
    print(f"Are {i} and {(2, 2)} neighbors: " + str(findNeighbors(i, (2, 2))))

point = []
for a in range(0, len(stringSpl), 2):
    pointTup = (int(stringSpl[a]), int(stringSpl[a + 1]))
    point.append(pointTup)
print(point)

point1, point2 = point[1], point[2]
print(f"Are {point1} and {point2} neighbors: " + str(findNeighbors(point1, point2)))