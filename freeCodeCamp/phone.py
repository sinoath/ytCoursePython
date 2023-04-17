from item import Item

class Phone(Item):
    all = []
    # defining the super() function referring to __init__ of the parent class
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # the super function make all the parent class methods/attributes available for the child class
        super().__init__(name, price, quantity)
        
        # specific child class assert
        assert broken_phone >=0, f"Negative value: {broken_phone} has to be not negative"

        # specific child class variable definition
        self.broken_phone = broken_phone

        # creating an only phones list
        Phone.all.append(self)
