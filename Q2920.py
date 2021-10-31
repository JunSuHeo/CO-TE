import sys

arr = list(map(int, sys.stdin.readline().split()))

target = arr.pop(0)
target2 = arr.pop(0)

answer = ''

if target > target2:
    answer = 'descending'
else:
    answer = 'ascending'

for i in arr:
    if answer == 'ascending':
        if target2 > i:
            answer = 'mixed'
        target2 = i

    elif answer == 'descending':
        if target2 < i:
            answer = 'mixed'
        target2 = i

print(answer)