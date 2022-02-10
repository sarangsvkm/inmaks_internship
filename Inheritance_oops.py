class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter a your name")
        self.mark=int(input("entar your mark"))
    def output(self):
        print(self.name,self.mark)
class teacher(student):
    def display(self):
        print("student details")

obj=teacher(" "," ")
obj.getdetails()
obj.output()
obj.display()