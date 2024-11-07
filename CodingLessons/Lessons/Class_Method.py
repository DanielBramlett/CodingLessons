class Unit:
    def __init__(self, name, health = 10, attack_power=4):
        self.name = name
        self.health=health
        self.attack_power= attack_power

    def get_hit(self, power):
        self.health = self.health - power
        print('I %s, have been hit for %s! I have %s Health left.' %(self.name, power, self.health))
        if self.health <=0:
            print("I died")
    def attack(self, enemy):         
        print('I am attacking %s for %s power' % (enemy.name, self.attack_power))
        enemy.get_hit(self.attack_power)
pirate = Unit("Catalina",5,6)
soldier=Unit("João",4,3)
pirate.attack(soldier)
print(pirate.attack_power)
pirate.get_hit(3)
pirate.get_hit(3)

#End 1
print('')
#Inheritance

class Pirate(Unit):
    def yell(self):
        print(' I %s say to thou villian, prepare to die' %(self.name))

privateer = Pirate('Anne Bonney')
bad_guy = Unit('Otto')
privateer.yell()
#bad_guy.yell() Not a type of Pirate