def div(a,b):
    try:

        print(a / b)
    except:
        print("there is a division error")

    finally:
        print(" am finally")
x=int(input("enter a first number"))
y=int(input("enter a second number"))
div(x,y)

