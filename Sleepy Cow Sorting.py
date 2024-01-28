"""
1 - 2 4 3
Check if the largest number is on the rightmost side
Check if the smallest number is on the leftmost side

"""

N = int(input())
lst = list(map(int, input().split()))

ind = N - 1
while True:
    if lst[ind] < lst[ind - 1]:
        break
    else:
        ind -= 1
print(ind)