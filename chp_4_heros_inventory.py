# Hero's Inventory
# Demonstrates tuple creation

#create an empty tuple
inventory = ("sword",
             "armor",
             "shield",
             "healing potion"
             )

print("\nThe tuple inventory is:")
print(inventory)

#print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

#treat the tuple as a condition

if not inventory:
    print("You left empty-handed")

input("\nPress the enter key to continue")