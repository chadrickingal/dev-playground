
phone = {}
laptop = {}
product = []  # this means the container of the all products

phone["IPHONE0013"] = { # this phone["IPHONE"] acts as id of the phone products
    "name" : "Iphone 13",
    "price": "9000",
    "stock": "200"
}

phone["IPHONE0014"] = {
    "name" : "Iphone 14",
    "price": "9000",
    "stock": "20"
}

laptop["MACBOOK"] = {
    "name" : "MacBook Air",
    "price": "90000",
    "stock": "10"
}

product.append(phone)
product.append(laptop)








class Product:

    def __init__(self, name, price, stock): # constructor
        self.name = name
        self.price = price
        self.stock = stock


    def buy(self, quantity):   # buy behavior
        self.stock -= quantity # self.stock = self.stock - quantity

    def checkStock(self):
        print(f"The stock now is: {self.stock}")


macBook = Product("MacBook Air 15", 9999.00, 20) # object and yung argument nya ay sabihin natin na galing yun sa database

macBook.checkStock()
print("---------------")
macBook.buy(10)
print("---------------")
macBook.checkStock()


print(product[0]["IPHONE0013"], "\n", product[0]["IPHONE0014"])

