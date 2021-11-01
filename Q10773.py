import sys

N = int(input())

arr = []

for _ in range(N):
    val = int(sys.stdin.readline().rstrip())

    if val != 0:
        arr.append(val)
    else :
        arr.pop(-1)

sum = 0
for i in arr:
    sum += int(i)

print(sum)