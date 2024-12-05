import math

x = int(input())
e = float(input())
s = 0
sl = 1
i = 0
while sl >= e:
    s += sl
    i += 1
    sl *= x / i
print(math.exp(x), s)
