import sys

T = int(input())

for _ in range(T):
    N, M = sys.stdin.readline().split()
    cnt = 0
    for i in range(int(N), int(M) + 1):
        str_i = str(i)
        for j in range(len(str_i)):
            if str_i[j] == '0':
                cnt += 1
    
    print(cnt)
