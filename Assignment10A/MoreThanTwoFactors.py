n=int(input())
factor = 0
for i in range(1,n+1):
    if n % i == 0:
        factor = factor + 1
if factor > 2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")