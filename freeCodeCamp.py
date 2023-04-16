class StoreManager:
    def __init__(self, name):
        self.name = name

class Item:
    # class attibute
    pay_rate = 0.8 # apply a discount of 20%
    def __init__(self, name, price, quantity):
        # Validating data received for price and quantity
        assert price >= 0, f"Negative value: {price} must be a not negative number"
        assert quantity >= 0, f"Negative value: {quantity} must be a not negative number"
        # Data definition for Item objects
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_items_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # using self.pay_rate instead of Item.pay_rate allow to change it on a per item 
        # instance level, otherwise is hard coded as always be the class attribute

item1 = Item("Phone", 300, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)



# print(f"{item1.name} full price is: {item1.price}")
# item1.apply_discount()
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(f"{item1.name} {round((1.0 - item1.pay_rate) * 100)}% discounted price is: {item1.price}")
# print(f"{item2.name} {round((1.0 - item2.pay_rate) * 100)}% discounted price is: {item2.price}")
# print(Item.__dict__) # Print all class attributes as a dictionary
# print(item1.__dict__) # Print all instance attributes as a dictionary
