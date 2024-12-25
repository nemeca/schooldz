def dsum(a):
    sum = 0
    while a:
        sum += a % 10
        a //= 10
    return sum


x = int(input())
print(dsum(x))
