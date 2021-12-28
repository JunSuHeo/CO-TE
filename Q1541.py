import sys

calc = input().split("-")

num = []

for i in range(len(calc)):
    tmp = calc[i].split("+")

    a = 0
    for j in tmp:
        a += int(j)
    
    num.append(a)

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]

print(answer)