import sys

N = int(sys.stdin.readline())

answer = 0

if N < 10:
    for i in range(1, N+1):
        answer += 1
else:
    for i in range(1, 10):
        answer += 1
    
    for i in range(10, N+1):
        num = str(i)
        diff = int(num[1]) - int(num[0])
        flag = True
        for j in range(len(num) - 1):
            if int(num[j+1]) - int(num[j]) != diff:
                flag = False
                break
            else:
                print(num)
        if flag:
            answer += 1

print(answer)
