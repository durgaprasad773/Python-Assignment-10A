n=int(input())
for i in range(n):
    if i == 0:
        row = "* " * ((2*n) -1)
        print(row)
    else:
        star="* " * (n-i)
        space=" " * i
        mid_space = "  " * (i-1)
        print(space + star + mid_space + star)