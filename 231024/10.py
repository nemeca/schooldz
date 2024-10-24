i = 0
t = 0
while (n := int(input())) != 0:
    i += 1
    if (n % 2 != 0) & (n % 3 == 0):
        t += 1
print(i)
print(t)
