import sys

arr = []

for i in range(45):
    for j in range(i+1):
        arr.append(i+1)

A, B = sys.stdin.readline().split()

sum = 0
for i in arr[int(A) - 1 : int(B)]:
    sum += i

print(sum)