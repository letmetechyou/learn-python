# Hero's Inventory 3.0
# Demonstrate Lists

#Create a list with some items and display with a for loop

inventory = ["sword", "armor", "shield", "healing potion"]
print("Your Items:")
for item in inventory:
    print(item)

# Get the length of the list 
print("You have", len(inventory), "items in your possession.")

# Test for membership with in

if "healing potion" in inventory:
    print("You will live to fight another day")

# Display one item through an index

index = int(input("\n Enter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# display a slice

start = int(input("\n Enter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))

print("inventory[", start, ":", finish, "] is ", end=" ")
print(inventory[start:finish])

input("\n Press the enter key to continue")