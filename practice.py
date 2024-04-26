number = 1
decimals = 1.5
strings = "UwU, what's this?"
list = ["List", "of", "things", 1, 11, ["Another list inside the outer list"]]
dictionary = {"Cuties": ["Feeny", "Lexi", "Vicky", "Linds"], "Caged": "Lexi"}
tuple = ("UwU", 5)
boolean = True

# Sex store time!
#Make a list with everyone's items. Then we'll show a for loop to print all of the items in the shop

VickyToys = ["Lexi's throat", "Lexi's ass", "Lexi's drippy caged clitty", "dildo", ]
FeenyToys = ["Dew", "Vibrating strap-on", "Abby's ass", "Candle wax"]

#Now we'll remove toys or add them
adding = True
while adding == True:
    response = input("Add toys: Y\nPrint toys: P\nRemove toys: R\nExit: Anything else\n")

    if response == "Y":
        #Do add code here
        response = input("Vicky's Toys or Feeny's toys? V/F ")
        if response == "V":
            #Add vicky toys here
            new_toy = input("Enter toy: ")
            VickyToys.append(new_toy)
        if response == "F":
            #Add feeny toys here
            new_toy = input("Enter toy: ")
            FeenyToys.append(new_toy)
    elif response == "P":
        for toy in VickyToys:
            print("Vicky's Toys: " + toy)
        for toy in FeenyToys:
            print("Feeny's Toys: " + toy)
    else:
        adding = False
        