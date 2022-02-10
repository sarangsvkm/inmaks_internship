def student_discount(a):
    discount=a*(10/100)
    discount_price=a-discount
    return discount_price
def regular_discount(b):
    discount=student_discount(b)*5/100
    discount_price=b-discount
    return discount_price

n=int(input("enter a price"))

print("regular discount price is %d "%(regular_discount(n)),"student discount price is %d"%(student_discount(n)))

