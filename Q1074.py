import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

res = 0
while N >= 0:
    checkVal = pow(2, N - 1)
    
    if 0 <= r < checkVal and c >= checkVal:
        c -= checkVal
        res += pow(2, N-1) * pow(2, N-1)
    elif r >= checkVal and 0 <= c < checkVal:
        r -= checkVal
        res += pow(2, N-1) * 2 * pow(2, N-1)
    elif r >= checkVal and c >= checkVal:
        r -= checkVal
        c -= checkVal
        res += pow(2, N-1) * 3 * pow(2, N-1)

    N -= 1

print(res)