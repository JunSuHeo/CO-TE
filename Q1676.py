N = int(input())

num = 1
for i in range(1, N+1):
    num *= i

num = ''.join(reversed(str(num)))

answer = 0
for i in range(len(num)):
    if num[i] == "0":
        answer += 1
    else:
        break

print(answer)