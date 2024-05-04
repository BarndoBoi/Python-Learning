import json, os

#We're going to write a user input loop that asks for an item to add or update
#Whether its in the dictionary or not we'll ask what the new value is and then update the dictionary
#We'll have a print option that shows the dictionary using Lexi's pretty print
gymventory = {
    "Disinfectant": 0,
    "Window Cleaner": 0,
    "Toilet Paper": 0,
    "Paper Towel" : 0,
    "Duster" : 0
}

def print_dict(the_dict):
    print(json.dumps(the_dict, sort_keys=True, indent=4))

#function to print all the keys in the dictionary
def pretty_keys(the_dict):
    pretty_keys = ""
    for key in the_dict.keys():
        pretty_keys += key + '/' #Insert the key at the end of the string followed by a space
    pretty_keys = pretty_keys[0:-1] #Slice the pretty_keys up to everything but the last character
    return pretty_keys

def add_or_remove(response):
    response = response.lower() # set the input to lowercase
    if response == "add":
        item = input("Enter item to add: ")
        amount = input("Enter value to add: ")
        if item in gymventory:
            gymventory[item] = gymventory[item] + int(amount)
            #gymventory[item] += amount
        else:
            gymventory[item] = int(amount) #This adds a new key with the name and sets the amount to what they typed
    if response == "remove":
        item = input("Enter item to remove: ")
        amount = input("Enter value to remove: ")
        if item in gymventory:
            gymventory[item] = gymventory[item] - int(amount)
        else:
            gymventory[item] = 0
            gymventory[item] -= int(amount)

def export_json():
    #Get the filename from the user
    filename = input("Name the file: ")

    #Serialize the dictionary into a JSON string for easy storage
    json_text = json.dumps(gymventory, indent=4)

    with open(filename + ".json", "w") as outfile:
        outfile.write(json_text)

def import_json():
    #Get the filename from the user
    filename = input("Enter file name: ")
    #Ask the os library where our python file is running
    path = os.getcwd()
    fullpath = path + filename + ".json"

    exists = os.path.isfile(fullpath)

    if exists:
        with open(filename + ".json", "r") as cum:
            gymventory = json.load(cum)
    else:
        print("Filename does not exist!")
            


commands = {
    "add": add_or_remove,
    "remove": add_or_remove,
    "print": print_dict,
    "help": pretty_keys,
    "export": export_json,
    "import": import_json
}

try:
    while True:
        #Do forever, or until we break from the loop
        print("Enter a command for the simply inventory program (Ctrl+C to exit)")
        response = input("Command: ")
        response = response.lower()
        if response in commands:
            if response == "print":
                commands[response](gymventory)
            elif response == "help":
                print("Commands: " + commands[response](commands))
            elif response == "export" or response == "import":
                commands[response]()
            else:
                commands[response](response)
        else:
            print("Not a recognized command, try again.")
except KeyboardInterrupt: # this is just here to exit the loop
    print("\nBye nerd")
