"""
nhoj mooed. farmer taught elsie, bessie and john flew.

9 words
5 nouns
2 intrans
1 trans
1 conjun
2 period
1 comma
"""


T = int(input())
# Each instance
for instance in range(T):
    # Input
    N, C, P = map(int, input().split())
    wordBank = [input().split() for w in range(N)]

    #