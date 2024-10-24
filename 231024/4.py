n = int(input())
i = 0
for _ in range(n):
    d = int(input())
    if d % 10 == 3:
        i += 1
print(i)
