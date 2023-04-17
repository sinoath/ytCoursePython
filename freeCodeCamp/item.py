import csv

class StoreManager:
    def __init__(self, name):
        self.name = name

class Item:
    # class attibute
    pay_rate = 0.8 # apply a discount of 20%
    all = []
    def __init__(self, name:str, price:float, quantity:int):

        # Validating data received for price and quantity
        assert price >= 0, f"Negative value: {price} must be a not negative number"
        assert quantity >= 0, f"Negative value: {quantity} must be a not negative number"

        # Data definition for Item objects
        # __name make it private and readonly outside the class contructor
        # _name works to but can still be changed using it as am attribute (Item._name)
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions executed upon instance creation
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    def total_items_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # using self.pay_rate instead of Item.pay_rate allow to change it on a per item 
        # instance level, otherwise is hard coded as always be the class attribute
        # if an instance level pay_rate isn't found, the class level one will be used

    @classmethod
    def instantiate_from_csv(cls):
        with open('./items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            # print(f"Added Item: {item.get('name')}")


    # static methods are mostly like regular independent functions
    # they do not automatically accept "self" as the first argument 
    # this functions could be defined outside the classes and will work fine
    # but declaring them as static methods they will be 'part' of the class definition
    # which is a better approach, 'sticking' together all the functions used inside the class
    @staticmethod
    def is_integer(num):
        # if a float is passed we can get rid of the .0s like in the item prices
        if isinstance(num, float):
            return num.is_integer() # False for float num, but return true if num ends in .0
        elif isinstance(num, int):
            return True
        else:
            return False
    
    # magic method to represent an instance with a formatted string
    # this is a best practice according to python documentation
    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.name}\", {self.price}, {self.quantity})"


