e = float(input())
s = 0
z = 1
sl = 1
i = 1
while sl >= e:
    s += sl * z
    z *= -1
    i += 2
    sl = 1 / i
print(s * 4)
