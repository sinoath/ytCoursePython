from item import Item

class Peripheral(Item):
    all = []
    # defining the super() function referring to __init__ of the parent class
    def __init__(self, name: str, price: float, quantity=0, wireless=0):
        # the super function make all the parent class methods/attributes available for the child class
        super().__init__(name, price, quantity)
        
        # specific child class assert
        assert wireless >=0, f"Negative value: {wireless} has to be not negative"

        # specific child class variable definition
        self.__wireless = wireless
        # creating an only phones list
        Peripheral.all.append(self)

    def __repr__(self):
        if self.__wireless == 1:
            return f"{self.__class__.__name__}(\"{self.name}\", {self.price}, {self.quantity}, wireless)"
        elif self.__wireless > 1:
            return f"{self.__class__.__name__}(\"{self.name}\", {self.price}, {self.quantity}, wireless++)"
        else:
            return Item.__repr__(self)

    @property
    def wireless(self):
        return self.__wireless



