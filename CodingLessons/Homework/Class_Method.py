class Vehicle:
    def __init__(self, category, acceleration, top_speed, wheels=4, speed=0, position=0):
        self.category = category
        self.wheels = wheels
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.speed = speed
        self.position = position
    
    def move(self):
        self.position += self.speed
    
    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

motorcycle = Vehicle('Motorcycle', 5, 20, 2)
van = Vehicle('Van', 2, 10)
sports = Vehicle('Sports', 10, 30)
minivan = Vehicle('Minivan', 3, 13)
truck = Vehicle('Truck', 4, 17)

Time = 0
while Time <= 20:
    van.accelerate()
    van.move()
    motorcycle.accelerate()
    motorcycle.move()
    sports.accelerate()
    sports.move()
    minivan.accelerate()
    minivan.move()
    truck.accelerate()
    truck.move()
    
    print(f"Van: {van.position}, Motorcycle: {motorcycle.position}, Sports: {sports.position}, Minivan: {minivan.position}, Truck: {truck.position}")
    Time += 1
print()
Time = 0
while Time <= 40:
    van.accelerate()
    van.move()
    motorcycle.accelerate()
    motorcycle.move()
    sports.accelerate()
    sports.move()
    minivan.accelerate()
    minivan.move()
    truck.accelerate()
    truck.move()
    
    print(f"Van: {van.position}, Motorcycle: {motorcycle.position}, Sports: {sports.position}, Minivan: {minivan.position}, Truck: {truck.position}")
    Time += 1
print()
Time = 0
while Time <= 60:
    van.accelerate()
    van.move()
    motorcycle.accelerate()
    motorcycle.move()
    sports.accelerate()
    sports.move()
    minivan.accelerate()
    minivan.move()
    truck.accelerate()
    truck.move()
    
    print(f"Van: {van.position}, Motorcycle: {motorcycle.position}, Sports: {sports.position}, Minivan: {minivan.position}, Truck: {truck.position}")
    Time += 1
