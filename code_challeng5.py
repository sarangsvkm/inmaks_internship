file=open("demo.txt",'w')
file.write("hello , i am sarang s")
file.close()

file=open("demo.txt",'r')
c=file.read()
print(c)
file.close()

file=open("demo.txt",'a')
file.write("\nhow are you? ")
file.close()

file=open("demo.txt",'r')
c=file.read()
print(c)
file.close()
