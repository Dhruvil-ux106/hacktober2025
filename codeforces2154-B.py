def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cost = 0
        for i in range(n - 1):
            if i % 2 == 0:  # i+1 is odd
                if a[i] >= a[i + 1]:
                    diff = a[i] - a[i + 1] + 1
                    cost += diff
                    a[i] -= diff
            else:  # i+1 is even
                if a[i] <= a[i + 1]:
                    diff = a[i + 1] - a[i] + 1
                    cost += diff
                    a[i + 1] -= diff
        print(cost)
