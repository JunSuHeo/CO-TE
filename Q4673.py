def seperate(n):
    answer = n
    while n > 0 :
        answer += n%10
        n //= 10
    
    return answer

num = 1

arr = [0 for i in range(10001)]

for i in range(10000):
    target = seperate(i)

    if target <= 10000:
        arr[target] += 1

for idx, val in enumerate(arr):
    if idx != 0 and val == 0:
        print(idx)