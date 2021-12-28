import sys

input = sys.stdin.readline

target = int(input())

N = int(input())

enable = {str(i) for i in range(10)}
if N != 0:
    enable -= set(map(str, input().split()))

min_cnt = abs(100 - target)

for i in range(1000001):
    numStr = str(i)
    for j in range(len(numStr)):
        if numStr[j] not in enable:
            break
        elif j == len(numStr) - 1:
            min_cnt = min(min_cnt, abs(target - int(numStr)) + len(numStr))

print(min_cnt)