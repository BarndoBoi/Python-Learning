number = 1
decimals = 1.5
strings = "UwU, what's this?"
list = ["List", "of", "things", 1, 11, ["Another list inside the outer list"]]
dictionary = {"Cuties": ["Feeny", "Lexi", "Vicky", "Linds"], "Caged": "Lexi"}
tuple = ("UwU", 5)
boolean = True

# Sex store time!
#Make a list with everyone's items. Then we'll show a for loop to print all of the items in the shop

vickys_toys = ["Lexi's throat", "Lexi's ass", "Lexi's drippy caged clitty", "dildo", ]
feeny_toys = ["Dew", "Vibrating strap-on", "Abby's ass", "Candle wax"]

def get_list(identifier):
    if identifier == "V":
        return vickys_toys
    elif identifier == "F":
        return feeny_toys
    else:
        return None
    
def remove_toy(list, item):
    if item in list:
        list.remove(item)
    else:
        print("No such item in list")

"""void function(int parameter)
{
    These curly braces denote where the function starts and ends
    In python whitespace (indentation) denotes what code block something goes in
}
"""

#Now we'll remove toys or add them
#Standard in python is snake_case which is lowercase variables with _ instead of spaces
#In C# it's CamelCase, which is valid in python, but is not the standard UwU

pass #Don't do anything or "do nothing"

adding = True
while adding == True:
    response = input("Add toys: A\nPrint toys: P\nRemove toys: R\nExit: Anything else\n")#
    if response == "A":
        #Do add code here
        response = input("Vicky's Toys or Feeny's toys? V/F ")
        list = get_list(response)
        if list != None:
            new_toy = input("Enter toy: ")
            list.append(new_toy)
        else: #If the list is None then the user entered incorrect input, so let's tell them that
            print("You didn't type V or F, dork")
    elif response == "P":
        response = input("Vicky's Toys or Feeny's toys? V/F ")
        list = get_list(response)
        if list != None:
            for toy in list:
                print(toy)
    elif response == "R":
        response = input("Vicky's Toys or Feeny's toys? V/F ")
        list = get_list(response)
        if list != None :
            toy = input ("Enter toy: ")
            remove_toy(list, toy) #Check if the toy is in the list and remove it, otherwise yell at user
            
    else:
        adding = False

        # Victoria is a fucking slut
        # She wishes she could eat my ass
        # She wants her cock to be as big as mine :3
