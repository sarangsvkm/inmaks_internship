class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter a your name")
        self.mark=int(input("enter a your mark"))
    def getoutput(self):
        print(self.name,self.mark)

obj=student(" "," ")
obj.getdetails()
obj.getoutput()
