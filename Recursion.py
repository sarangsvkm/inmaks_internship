def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
a=int(input("enter a number"))
print(fact(a))