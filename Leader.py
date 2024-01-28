

def solve():
    n, cow_type, EN = initialize()
    pairs = find_pairs(cow_type, EN, n)


def initialize():
    N = int(input())
    types = str(input())
    Ei = list(map(int, input().split()))
    return N, types, Ei


# For loop 2 -> For loop 1
def find_pairs(cType, EI, N):
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            lst1, lst2 = [], []
            print(a, b)


if __name__ == "__main__":
    solve()

