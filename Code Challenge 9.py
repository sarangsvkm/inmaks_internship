class computer:
    def __init__(self,c_model_no,c_ramsize,c_storage):
        self.c_model_no=c_model_no
        self.c_ramsize=c_ramsize
        self.c_storage=c_storage


    def getspecs(self):
        self.c_model_no=input("enter  model year number")
        self.c_ramsize=input("enter  ram memory size in GB")
        self.c_storage=input("enter  storage size in GB")
    def displayspecs(self):
        print("comuter specs=" + self.c_model_no, self.c_ramsize, self.c_storage)



class Desktop(computer):
    def __init__(self,D_modelno,D_displaysize,D_brand,D_procceser):
        self.D_modalno=D_modelno
        self.D_displaysize=D_displaysize
        self.D_brand=D_brand
        self.D_procceser = D_procceser
    def getspecialspecs(self):
        self.c_model_no=input("enter Desktop seriel no")
        self.D_brand=input("enter Desktop barnd name")
        self.D_displaysize=input("enter Desktop display size")
        self.D_procceser = input("enter Desktop proccesr type")

    def displayspecs1(self):
        print("Desktop specs=" + self.D_displaysize, self.D_brand, self.D_modalno, self.D_procceser)



class laptop(Desktop):
    def __init__(self,L_modelno,L_brand,L_displaysize,L_procceser):
        self.L_modalno = L_modelno
        self.L_displaysize = L_displaysize
        self.L_brand = L_brand
        self.L_procceser = L_procceser
    def getspecialspecs1(self):
        self.L_model_no = input("enter laptop seriel no")
        self.L_brand = input("enter laptop barnd name")
        self.L_displaysize = input("enter laptop display size")
        self.L_procceser = input("enter laptop proccesr type")

    def displayspecs2(self):

        print("laptop specs="+self.L_modalno,self.L_brand,self.L_displaysize,self.L_procceser)




obj1=Desktop('','','','')
obj2=laptop('',' ','','')
obj1.getspecs()
obj1.getspecialspecs()
obj2.getspecialspecs1()

obj1.displayspecs1()
obj2.displayspecs2()




