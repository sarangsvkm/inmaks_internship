list1=[10,12,1,14,15]
list1[1]=200
print(list1)
fruits=["apple","orange","pinapple","blueburry","banana"]
fruits.append("mango")
fruits.insert(1,"grapes")
print(fruits)
print(len(fruits))
print(fruits.index("mango"))
fruits.remove("orange")
print(fruits)
fruits.pop(1)
print(fruits)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)

