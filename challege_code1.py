def si(p,t,r):
    c=(p*t*r)/100

    return c
a=int(input("enter  principal value"))
b=int(input("enter  time period"))
c=int(input("enter rate of interest"))
d=si(a,b,c)
print("The Simple Interest is", d)