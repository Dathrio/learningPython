#RPG Inventory System

#current items in bag
bag = {'rope': 1, 'torch': 6, 'gold': 42, 'dagger': 1, 'arrow': 12}

#go through each item in your inventory to display the contents and count total items
def displayInventory(inventory):
    totalNumber = 0
    print("Inventory:")
    #displays the number of each type of item
    for k, v in inventory.items():
        print(str(v) + " " + k)
        #adds the ammount to the total count
        totalNumber += v
    print("Total number of items: " + str(totalNumber))

displayInventory(bag)