class product:
    #set
    def setid(self,pid):
        self.pid=pid
    def setcategory(self,catg):
        self.catg=catg
    def setsupplier(self,sup):
        self.sup=sup
    def setname(self,name):
        self.name=name
    def setprice(self,price):
        self.price=price
    def setdiscount(self,discount):
        self.discount=discount
    def setdiscounted_price(self,discounted_price):
        self.discounted_price=discounted_price
    def setquantity(self,quantity):
        self.quantity=quantity
    def setstatus(self,status):
        self.status=status
    #get
    def getid(self):
        return self.pid
    def getcategory(self):
        return self.catg
    def getsupplier(self):
        return self.sup
    def getname(self):
        return self.name
    def getprice(self):
        return self.price
    def getdiscount(self):
        return self.discount
    def getdiscounted_price(self):
        return self.discounted_price
    def getquantity(self):
        return self.quantity
    def getstatus(self):
        return self.status
