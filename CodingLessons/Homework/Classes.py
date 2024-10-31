class Vehicle:
   def __init__(self, category, wheels=4):
         self.category= category
         self.wheels=wheels

motorcycle = Vehicle('Motorcycle',2)
van = Vehicle('Van')
sports = Vehicle('Sports')
minivan = Vehicle('Minivan')
truck = Vehicle('Truck')