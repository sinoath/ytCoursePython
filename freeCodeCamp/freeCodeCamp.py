from peripheral import Peripheral
from item import Item
from phone import Phone
from laptop import Laptop

Item.instantiate_from_csv("./csv/items.csv")
# Item.all[2].price = 12.5
for item in Item.all:
    print(item)
# laptop1 = Laptop("Asus", 800, 5, 1)
# laptop2 = aptop("HP", 800, 5, 0)
# item1.name = "Desktop"
# phone1 = Phone("Samsung", 600, 3)
# phone2 = Phone("Motorola", 600, 3)
# peripheral1 = Peripheral("Razor", 50, 8, 2)
# peripheral2 = Peripheral("Logitech", 35, 5, 1)
# peripheral3 = Peripheral("Steelseries", 45, 10, 0)
# print(Item.all)
# print(Peripheral.all)
# print(Phone.all)
# print(Laptop.all)
# print(Item.is_integer(4.0))
# Item.instantiate_from_csv()
# for item in Item.all:
#     print(item)
# print(Item.all[3].name)
# item1 = Item("Phone", 300, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name, "\n\t", instance.price, "\t", instance.quantity)

# print(f"{item1.name} full price is: {item1.price}")
# item1.apply_discount()
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(f"{item1.name} {round((1.0 - item1.pay_rate) * 100)}% discounted price is: {item1.price}")
# print(f"{item2.name} {round((1.0 - item2.pay_rate) * 100)}% discounted price is: {item2.price}")
# print(Item.__dict__) # Print all class attributes as a dictionary
# print(item1.__dict__) # Print all instance attributes as a dictionary
