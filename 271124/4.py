max = -30000
n = int(input())
while n != 0:
    if n > max:
        max = n
    n = int(input())
print(max)