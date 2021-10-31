import sys

N = int(input())

arr = []

for _ in range(N):
    val = sys.stdin.readline().rstrip()
    arr.append(int(val))

arr.sort()

for i in arr:
    print(i)