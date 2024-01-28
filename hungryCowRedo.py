"""
1 5
1 2

2 5
1 2
5 10

2 5
1 10
5 10
"""

N, T = map(int, input().split())
days = [list(map(int, input().split())) for i in range(N)]

today = days[0][0]
stock = days[0][1]
answer = 0
for i in range(1, N):
    newDate = days[i][0]
    dateGap = newDate - today
    if stock >= dateGap:
        stock -= dateGap
        answer += dateGap
    else:
        answer += stock
        stock = 0
    today = newDate
    stock += days[i][1]

dateGap = T - today + 1
if stock >= dateGap:
    stock -= dateGap
    answer += dateGap
else:
    answer += stock
    stock = 0
print(answer)