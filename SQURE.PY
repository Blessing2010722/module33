class computer:
    def__init__(self):
        self.__MAX_PRICE=7000
    def sell(self):
        print("sellling price: {}".format(self.__max_price"))


    def setmaxprice(self,price):
        self.__max_price = price
    
c = computer()
c.sell()

c.__max_price = 1000
print("attempting to change price directly.")
c.sell()
print("changing price using the setter function.")
c.setmaxprice(1000)
c.sell()