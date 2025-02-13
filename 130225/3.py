znam = 3
chisl = 4


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


def add(a, b, c, d):
    global chisl, znam
    x = a * d + b * c
    y = b * d
    z = nod(x, y)
    chisl = x // z
    znam = y // z


n = int(input())
for i in range(n):
    add(chisl, znam, chisl + 3, znam * 3)

print(chisl, " ", znam)
