class hospital:
    def __init__(self, adnname,drname,sistername,dept):
        self.adnname=adnname
        self.drname=drname
        self.sistername=sistername
        self.dept=dept
    def getdetails(self):
        self.adnname=input("enter a your admin name")
        self.drname = input("enter a your dr name")
        self.sistername=input("enter your sister name")
        self.dept=input("enter your department")

class department(hospital):
    def display(self):
        print(adnname,drname,sistername,dept)
class patientward(department,hospital):
    def __init__(self,patientname,age,Mbno,place):
        self.patientname=patientname
        self.age=age
        self.Mbn0=Mbno
        self.place=place
    def getpatientdetails(self):
        self.patientname = input("enter a your patient name")
        self.age = int(input("enter a your age "))
        self.Mbno= int(input("enter your number "))
        self.place = input("enter your place")
    def output2(self):
        print(self.patientname,self.age,self.Mbno,self.place)


obj1=hospital('','','','')
obj1.getdetails()
obj2=patientward('','','','')
obj2.getpatientdetails()
