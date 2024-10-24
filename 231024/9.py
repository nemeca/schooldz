n = int(input())
i = 0
m = 300
M = 0
for _ in range(n):
    d = int(input())
    if d >= 60:
        i += 1
    if d > M:
        M = d
    if d < m:
        m = d
print(M - m)
print(i)
