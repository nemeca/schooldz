sum = 0
i = 0
n = int(input())
while n != 0:
    if (n // 100 == 0) & (n // 10 != 0) or (-n // 100 == 0) & (-n // 10 != 0):
        i += 1
        sum += n
    n = int(input())
if i != 0:
    print(sum / i)
else:
    print("No numbers")
