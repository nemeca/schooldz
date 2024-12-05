import math

x = int(input())
e = float(input())
z = 1
s = 0
sl = x
i = 1
while sl >= e:
    s += sl * z
    i += 2
    z *= -1
    sl = pow(x, i) / i
print(math.atan(x), s)
