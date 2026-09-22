n = [1,2,3,4,5]
large = n[0]
for i in range(len(n)):
    if n[i] > large:
        large = n[i]
print(large)

