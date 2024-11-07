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

class Motorcycle(Vehicle):
     def __init__(self, category, acceleration=10, top_speed=10, wheels=4, speed=0, position=0):
         super().__init__(category, acceleration, top_speed, wheels, speed, position)

class Sport(Vehicle):
    def __init__(self, category, acceleration, top_speed, wheels=4, speed=0, position=0, turbo=False):
        super().__init__(category, acceleration, top_speed, wheels, speed, position)
        self.turbo = turbo

    def accelerate(self):
        if self.turbo> 0:
            self.speed += 2 * self.acceleration
            self.turbo -= 1
        else:
            self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

sports = Sport('Sports', 10, 30)
motorcycle = Motorcycle('Motorcycle', 10, 10, 2)
van = Vehicle('Van', 2, 10)
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