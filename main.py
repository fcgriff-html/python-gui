#this is based on an object oriented python course on freecodecamp.orgs' youtube
#channel


class Item:
    def __init__(self, name: str, price: float, quantity = 0):
        
        #assertions assure that there will not be the problem of negative price or quantity
        #f:string statements post the asertions allow for error handling,
        #in this case it allows us to print directly to the sceen what the issue is
        #(f in this case is just a "format" indicator to allow us to concatonate string values)

        assert price >= 0, f"price {price} is less than zero, there is no such thing as a negative price"
        assert quantity >=0, f"quantity {quantity} is less than zero, why the hell are you trying to sell something that you dont have?"
        
        #this acts as a consturctor to init objects with the given parameters
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("phone", 100, 5)
print(item1.calculate_total_price())

item2 = Item("laptop", 1000, 3)
print(item2.calculate_total_price())
