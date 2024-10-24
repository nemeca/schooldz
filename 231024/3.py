n = int(input())
i = 0
for _ in range(n):
    d = int(input())
    if d % 4 == 0:
        i += d
print(i)
