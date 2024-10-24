n = int(input())
i = 0
for _ in range(n):
    d = int(input())
    if (d % 10 == 4) & (d % 6 == 0):
        i += d
print(i)
