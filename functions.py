# Make use of functions in python
numbers = [11, 12, 16, 18, 21, -1, 41]
hello_list = ["ciao", "mondo", "ciao", "ciao", "mondo"]
# print(type(result_tuple))

# given an input list return a list of tuple of elements, index of the input list
def list_of_tuple(input_list=[1, 2]):
    result_list= []
    for element in input_list:
        result_list.append((element, input_list.index(element)))
    return result_list
print(list_of_tuple(numbers))

# given an input list return a dictionary with key:value of list_element:how_many_time_element_in_list
def count_dict(input_list = ["test", "default"]):
    result_dict= {}
    for element in input_list:
        result_dict.update({ element : input_list.count(element)})
    return result_dict

# given an input list of integers return how many even numbers there are
def how_many_even(input_list):
    counter = 0
    for element in input_list:
        if element % 2 == 0:
            counter += 1
    return counter

# count how many times a target character is in the input string
def character_count(input_string, target_char):
    return input_string.count(target_char)

# given an input list of integers, return a list of integers divisible by three
def list_div_by_three(input_list):
    result_list = []
    for element in input_list:
        if element % 3 == 0:
            result_list.append(element)
    return result_list

print(list_div_by_three(numbers))

# print(character_count("ciao", "a"))
# print(how_many_even(numbers))


# print(count_dict(hello_list))


# print(list_of_tuple(numbers))
