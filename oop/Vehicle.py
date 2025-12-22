class Vehicle:

    # constructor, self = object using this method
    def __init__(self, make, model, year, color):
        # changes THIS object's make, model, year, color
        self.make = make
        self.model = model
        self.year = year
        self.color = color



    def drive(self):
        print(self.model + " is driving brrrr")