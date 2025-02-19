from typing import Optional
from computer import Computer
class ResaleShop:

    # What attributes will it need?
    inventory: list
    item_id: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        """Initialize the attributes to run a ResaleShop"""
        self.inventory = []
        self.item_id = 0

    # What methods will you need?
    # buy(computer: Computer) -> int
    # sell(item_id: int)
    # refurbish(item_id: int, new_os: Optional[str] = None)
    # print_inventory()
    def buy(self, computer: Computer):
        """Adds a new computer to inventory and returns its ID"""
        print("Buying", computer.description)
        print("Adding to inventory...")
        self.inventory[self.item_id] = computer 
        print("Added computer with ID:", self.item_id)
        assigned_id = self.item_id
        self.item_id += 1
        print("Done.\n")
        return assigned_id
    
    def sell(self, item_id: int):
        """Removes a computer from the inventory,
        print error message if not found"""
        if item_id in self.inventory: 
            self.inventory.pop(item_id) 
            print("Selling computer with ID:", item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Select another item to sell.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """Refurbish a computer,assign a new price based on year,
        optionally update OS, print error message if not found"""
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            if computer.year_made < 2000:
                computer.price = 0 
            elif computer.year_made < 2012:
                computer.price = 250 
            elif computer.year_made < 2018:
                computer.price = 550 
            else:
                computer.price = 1000

            if new_os is not None:
                computer.operating_system = new_os
                print(f"Updated OS to {new_os}.")
        
            print(f"Computer with ID {item_id} refurbished. New price: {computer.price}")
        else:
            print("Item", item_id, "not found. Select another item to refurbish.")

    def print_inventory(self):
        """Print inventory, show error message when it's empty"""
        if not self.inventory: 
            print("No inventory to display.")
        else:
            for item_id, computer in self.inventory.items(): 
                print(f"Item ID: {item_id} : {computer.description}, Price: {computer.price}, OS: {computer.operating_system}")

# test
# my_computer = Computer("MacBook Pro 2015", "Intel i7", 512, 16, "macOS Mojave", 2015, 1200)
# shop = ResaleShop()
# computer_id = shop.buy(my_computer)
# shop.print_inventory()
# shop.refurbish(computer_id, new_os="macOS Catalina")
# shop.print_inventory()
# shop.sell(0)
# shop.print_inventory()
# shop.sell(999)
# shop.refurbish(999)


