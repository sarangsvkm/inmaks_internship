def bmi(a,b):
    d= a/(b**2)
    return d
x=int(input("enter your weight in kg"))
y=int(input("enter your height in m"))
z= bmi(x,y)
print("BMI=",z,"kg/m^2")

