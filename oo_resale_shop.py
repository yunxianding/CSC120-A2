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
        computer.item_id = self.item_id
        self.inventory.append(computer)
        assigned_id = self.item_id 
        print("Added computer with ID:", assigned_id)
        self.item_id += 1
        print("Done.\n")
        return assigned_id
    
    def sell(self, item_id: int):
        """Removes a computer from the inventory,
        print error message if not found"""
        for computer in self.inventory:
            if computer.item_id == item_id:
                self.inventory.remove(computer)
                print("Selling computer with ID:", item_id)
                print("Item", item_id, "sold!")
                return
        print("Item", item_id, "not found. Select another item to sell.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """Refurbish a computer,assign a new price based on year,
        optionally update OS, print error message if not found"""
        for computer in self.inventory:
            if computer.item_id == item_id:
                if computer.year_made < 2000:
                    computer.update_price(0)  # Price is 0 for computers older than 2000
                elif computer.year_made < 2012:
                    computer.update_price(200)  # Price is 200 for computers made between 2000 and 2012
                elif computer.year_made < 2018:
                    computer.update_price(500)  # Price is 500 for computers made between 2012 and 2018
                else:
                    computer.update_price(1000)  # Price is 1000 for computers made after 2018

                if new_os is not None:
                    computer.update_os(new_os)
                    print(f"Updated OS to {new_os}.")
        
                print(f"Computer with ID {item_id} refurbished. New price: {computer.price}")
                return
        print("Item", item_id, "not found. Select another item to refurbish.")

    def print_inventory(self):
        """Print inventory, show error message when it's empty"""
        if not self.inventory: 
            print("No inventory to display.")
        else:
            for computer in self.inventory: 
                print(f"Item ID: {computer.item_id} : {computer.description}, Price: {computer.price}, OS: {computer.operating_system}")

if __name__ == "__main__":
    my_computer = Computer("MacBook Pro 2015", "Intel i7", 512, 16, "macOS Mojave", 2015, 1200)
    shop = ResaleShop()

    # Test buying a computer
    computer_id = shop.buy(my_computer)
    shop.print_inventory()

    # Test refurbishing a valid computer
    shop.refurbish(computer_id, new_os="macOS Catalina")
    shop.print_inventory()

    # Test selling a valid computer
    shop.sell(computer_id)
    shop.print_inventory()

    # Test selling an invalid computer
    shop.sell(999)  # Invalid ID
    shop.sell(-1)   # Negative ID

    # Test refurbishing an invalid computer
    shop.refurbish(999)  # Invalid ID
    shop.refurbish(-1)   # Negative ID

    # Test inventory when empty
    shop.print_inventory()


