# Defining some classes, properties and methods

class Persona:
    
    # constructor
    def __init__(self, name="John", age=20):
        self.name = name
        self.age = age
    
    # methods
    def greetings(self):
        print("Hello I'm {}, I am {} years old".format(self.name, self.age))
        
# persona_carl = Persona("Carl", 32)
# persona_carl.greetings()


class Pet:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        sound = "None"
        if self.species == "cat":
            sound = "Miao!"
        elif self.species == "dog":
            sound = "Bau!"
        elif self.species == "bird":
            sound = "Cip!"
        else:
            sound = "No sound"
        print("{}: \"{}\"".format(self.name,sound))


class Car:
    
    def __init__(self, manifacturer, model):
        self.manifacturer = manifacturer
        self.model = model
    
    def car_description(self):
        print(f"This car is a {self.manifacturer} {self.model}")
        
class Employee:
    
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    
    def raise_salary(self):
        self.salary += int(0.1 * self.salary)
    
    def details(self):
        print(f"Emplyee {self.name}, ID:{self.ID} earns {self.salary} euros")

class Item:
    

    def __init__(self, name, price, quantity):
        # Validate variable values passed to the constructor
        assert price >= 0, f"Negative value: {price} < 0"
        assert quantity >= 0, f"Negative value: {quantity} < 0"

        # Defining values for the self object
        self.name = name
        self.price = price
        self.quantity = quantity

class StoreManager:
    
    def __init__(self, monthly_store_cost):
        self.products = {}
        self.monthly_store_cost = monthly_store_cost
    
    def add_product(self, item):
        self.products[item.name] = item
    
    def del_product(self, name):
        self.products.pop(name)

    def calculate_costs(self):
        costs = 0
        for product in self.products.values():
            costs += product.quantity * self.monthly_store_cost
        return costs

    def total_items(self):
        number_of_items = 0
        for product in self.products.values():
            number_of_items += product.quantity
        return number_of_items


p1 = Item("Phone", 500, 20)
p2 = Item("Desktop", 1500, 8)
p3 = Item("Laptop", 900, 12)
SM = StoreManager(15)
SM.add_product(p1)
SM.add_product(p2)
SM.add_product(p3)
print(f"Cost of {SM.calculate_costs()} for {SM.total_items()} items")
SM.del_product("Laptop")
print(f"Cost of {SM.calculate_costs()} for {SM.total_items()} items")
# employee1 = Employee("Mario Rossi", 12345, 1500)
# employee1.details()
# employee1.raise_salary()
# employee1.details()
        
# car1 = Car("Fiat", "Punto")
# car2 = Car("Ferrari", "Testarossa")
# car1.car_description()
# car2.car_description()
# pet1 = Pet("Zelda", "cat")
# pet2 = Pet("Brezza", "dog")
# pet1.make_sound()
# pet2.make_sound()



# Inheritance
# class Teacher(Persona):
    # overloading constructor defining a new specific "init" which inherit part of the Persona one
    # and define more specific attributes for the child class
    # def __init__(self, name, surname, matter="None"):
    #     # could be Persona.__init__(name, surname)
    #     super().__init__(name, surname)
    #     self.matter = matter
    # def introduce(self):
    #     print("Good morning, my name is {} {}, i theach {}".format(self.name,self.surname,self.matter))

# class Friend(Persona):
    # pass # this will inherit all the Persona constructor

# teacher1 = Teacher("Anna", "Neri")
# teacher1.greetings()
# teacher1.matter = "Algebra"
# teacher1.introduce()
# gamer1 = Friend("Dorel", "Petreanu")
# gamer1.greetings()
