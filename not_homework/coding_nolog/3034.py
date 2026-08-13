"""พอด"""
n_k = input().split()
N = int(n_k[0])
K = int(n_k[1])

count = [0] * (K + 1)

for _ in range(N):
    q = int(input())
    count[q] += 1

min_people = count[1]
for i in range(2, K + 1):
    if count[i] < min_people:
        min_people = count[i]

ans = N - (min_people * K)
print(ans)
