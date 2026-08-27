"""[LEARNING LOGS] ของขวัญและขโมย"""
N, K, T = map(int, input().split())
NOW = 1
COUNT = 1

if T == 1:
    print(1)
else:
    while True:
        NOW = (NOW + K) % N

        if NOW == 1:
            print(COUNT)
            break

        COUNT += 1

        if NOW == T:
            print(COUNT)
            break
