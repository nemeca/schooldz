x = int(input())
e = float(input())
z = 1
s = 0
sl = float(x)
i = 0
while sl >= e:
    s += sl * z
    i += 1
    z *= -1
    sl = pow(x, i) / i
print(s)
