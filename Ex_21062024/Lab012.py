# Dictionary
# key-value pair
# unordered
# mutable
# can store any data type
# cannot have duplicate KEYS
from collections import OrderedDict

my_dict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(len(my_dict))
print(my_dict["name"])
print(my_dict.keys())
print(my_dict["age"])
print(my_dict["city"])

# if we use dict keyword then no need to add "" for keys
my_dict2 = dict(name="Max", age=28, city="New York")

new_dict = {"name" : "John", "age" : 30, "city" : "New York"}
# below line is not index nut its the key name
print(new_dict["city"])
print(new_dict.get("age"))

# cannot have duplicate KEYS
# if we try to add duplicate key then it will overwrite the value
new_dict["age"] = 31
print(new_dict)

# for loop
print("for lopp")

for key in new_dict:
    print(key, new_dict[key])

for k,v in new_dict.items():
    print(k,v)

# ordered dictionary
# from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["name"] = "John"
ordered_dict["age"] = 30
ordered_dict["city"] = "New York"
print(ordered_dict)

# compare dictionaries
# dictionaries are equal if they have the same key-value pairs in the same order
# dictionaries are not equal if they have different key-value pairs or different order

dict1 = {"name": "John", "age": 30, "city": "New York"}