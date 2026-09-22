n,m = list(map(int,input().split()))
sum = 0
for i in range(n,m+1):
    m=i**3
    sum+=m
print(sum)