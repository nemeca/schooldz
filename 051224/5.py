import math

x = int(input())
e = float(input())
z = 1
s = 0
sl = math.pi / 2
i = 1
while sl >= e:
    s += sl * z
    i += 2
    z *= -1
    sl = 1 / i * pow(x, i)
print(math.pi / 2 - math.atan(x), s)
