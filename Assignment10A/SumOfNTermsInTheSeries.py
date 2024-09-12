x=int(input())
n =int(input())
sum_of = 0
power = 1
for i in range(n):
    term = x ** power
    if i % 2 == 0:
        sum_of = sum_of + term
    else:
        sum_of = sum_of - term
    power = power + 2
print(sum_of)