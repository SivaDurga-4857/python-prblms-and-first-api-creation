l = list(map(int,input().split()))
s = int(input())
for i in l:
    if s in l:
        print("Found")
    else:
        print("Not found")


