from item import Item
from phone import Phone
from laptop import Laptop

laptop1 = Laptop("Laptop", 800, 5)
# item1.name = "Desktop"
phone1 = Phone("Samsung", 600, 3)
phone2 = Phone("Motorola", 600, 3)
print(Item.all)
print(Phone.all)
print(Laptop.all)
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
