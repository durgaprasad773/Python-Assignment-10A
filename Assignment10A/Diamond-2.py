n=int(input())
for i in range(1,n+1):
    space =" " * (n-i)
    num = (str(i)+" ") * i
    print(space + num)
    
for i in range(1,n):
    space =" " * i
    num = (str(n-i)+" ") * (n-i)
    print(space + num)
    

'''for i in range(n-1,0,-1):
    space =" " * (n-i)
    num = (str(i)+" ") * i
    print(space + num)'''