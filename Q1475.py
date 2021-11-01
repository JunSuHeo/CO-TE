def addCard(arr, cnt):
    cnt += 1

    for i in range(len(arr)):
        arr[i] += 1
    
    return arr, cnt

arr = [0 for _ in range(10)]
cnt = 0

str = input()

arr, cnt = addCard(arr, cnt)

for i in str:
    if i == '9' or i == '6':
        if arr[6] == 0 and arr[9] == 0:
            arr, cnt = addCard(arr, cnt)
            if arr[6] != 0:
                arr[6] -= 1
            else:
                arr[9] -= 1
        else:
            if arr[6] != 0:
                arr[6] -= 1
            else:
                arr[9] -= 1
    else :
        if arr[int(i)] == 0:
            arr, cnt = addCard(arr, cnt)
            arr[int(i)] -= 1
        else:
            arr[int(i)] -= 1


print(cnt)