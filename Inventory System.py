#RPG Inventory System
#current items in bag
bag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#loot dropped by a dragon
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

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

#add loot to current inventory, updating count of existing items and adding new items to dictionary
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if not item in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    print("Invetory Updated")

#display initial inventory
displayInventory(bag)
#add the loot and redisplay inventroy
addToInventory(bag, dragonLoot)
displayInventory(bag)