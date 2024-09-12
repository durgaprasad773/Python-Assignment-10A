n=int(input())
count = 0
for i in range(1,n+1):
    l = len(str(i))
    count = count + l
print(count)