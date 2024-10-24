n = int(input())
i = 0
for _ in range(n):
    d = int(input())
    if d % 6 == 0:
        i += 1
print(i)
