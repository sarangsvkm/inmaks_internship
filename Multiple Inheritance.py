class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter a your name")
        self.mark=int(input("entar your mark"))
    def output(self):
        print(self.name,self.mark)
class teacher:
    def display(self):
        print("i am class teacher")
class parents(teacher,student):
    def newfun(self):
        print( "i am parent")


obj=parents(" "," ")
obj.getdetails()
obj.output()
obj.display()
obj.newfun()
