sum = 0
i = 0
n = int(input())
while(n!=0):
    if(n//100 == 0) and (n//10 !=0):
        i+=1
        sum+=n
    n = int(input())
print(sum/i)
