class Computer:

    # What attributes will it need?
    # description (str)
    # processor_type (str)
    # hard_drive_capacity (int)
    # memory (int)
    # operating_system (str)
    # year_made (int)
    # price (int)

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                description: str, 
                processor_type: str, 
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        """Initialize the attributes to describe a computer"""
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    # update_price(new_price: int)
    # update_os(new_os: str)
    def update_price(self, new_price: int):
        """update the price of a computer"""
        print(f"Updating price to {new_price}.")
        self.price = new_price
        print("Done.\n")

    def update_os(self, new_os: str):
        """update the OS of a computer"""
        print(f"Updating os to {new_os}.")
        self.operating_system = new_os
        print("Done.\n")

# testing
# my_computer = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
# my_computer.update_price(1000)
# my_computer.update_os('MacOS Monterey')