def student_discount(a):
    discount_price=a-a*(10/100)
    return discount_price
def regular_discount(b):

    discount_price=b-b*5/100
    return discount_price

n=int(input("enter a price"))

print("regular discount price is %d "%(regular_discount(student_discount(n))),"student discount price is %d"%(student_discount(n)))

