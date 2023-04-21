from item import Item

class Laptop(Item):
    all = []
    # defining the super() function referring to __init__ of the parent class
    def __init__(self, name: str, price: float, quantity=0, has_numpad=0):
        # the super function make all the parent class methods/attributes available for the child class
        super().__init__(name, price, quantity)
        
        # specific child class assert
        assert has_numpad >=0, f"Negative value: {has_numpad} has to be not negative"

        # specific child class variable definition
        self.__has_numpad = has_numpad
        # creating an only phones list
        Laptop.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.name}\", {self.price}, {self.quantity}, {self.has_numpad})"

    @property
    def has_numpad(self):
        return self.__has_numpad


