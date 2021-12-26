import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = set(input().rstrip().split()[1:])

parties = []
res = []

for _ in range(M):
    parties.append(set(input().rstrip().split()[1:]))
    res.append(1)


for _ in range(M):
    for i, party in enumerate(parties):
        if not arr.isdisjoint(party):
            res[i] =  0
            arr.update(party)

print(sum(res))