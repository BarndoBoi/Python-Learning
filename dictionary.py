import pprint
import json


def print_dict(dict):
    print(json.dumps(dict, sort_keys=True, indent=4))


dictionary = {
    #keys               #ovalues
    1                  : "One",
    "two"              : 2,
    ("Gay", "Lesbian") : "UwU!"
}

dictionary.keys()
dictionary.values()

if "Doesn't Exist" in dictionary:
    print("Key is in dictionary")
else:
    print("No such key in dictionary")

for key in dictionary.keys():
    print(key)

#dictionaries can't have multiple of the same key, so below updates the "two" key instead of adding a new one
dictionary["two"] = "two"

#Lets do something a little more relevant

inventory = { 
    "Cleaner": 0,
    "Gym Mats": 0,
    "Cuties": 3
}
empty_inventory = {} #exmpty dictionary with nothing in it yet
empty_inventory["Item"] = 0 #Now the dictionary isn't empty anymore, it has a new key and value added

def increment_cleaner(inventory_dict):
    if "Cleaner" in inventory_dict:
        inventory_dict["Cleaner"] = inventory_dict["Cleaner"] + 1
    else:
        print("No cleaner in dictionary, doing null operation")

print(inventory.get("Cleaner"))
increment_cleaner(inventory)
print(inventory["Cleaner"])
increment_cleaner(empty_inventory)
print_dict(inventory)