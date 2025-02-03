# Kattis Bank Queue: Greedy
# Link: https://open.kattis.com/problems/bank

def bank(m, arr):
    available = [False] * (m + 1)
    arr.sort(key=lambda x: (-x[0], x[1]))

    ans = 0
    for cash, limit in arr:
        for time in range(limit, -1, -1):
            if not available[time]:
                available[time] = True
                ans += cash
                break

    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    print(bank(n, m, arr))