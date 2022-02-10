result=[]
for i in "good morning":
    result.append(i)
print(result)

result1=[i for i in "hai , how are you"]
print(result1)

result2=["python","django","flask","people","power","flash","fact"]
new=[]
for i in result2:
    if 'p' in i:
        new.append(i)
print(new)

new2=[i for i in result2 if 'f' in i]
print(new2)
