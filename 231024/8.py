n = int(input())
i = 0
s = 0
for _ in range(n):
    d = int(input())
    s += d
    if d >= 60:
        i += 1
print(s / n)
if i >= 2:
    print("YES")
else:
    print("NO")
