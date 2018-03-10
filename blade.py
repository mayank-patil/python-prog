class fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print(f"{self.name} attacks {other_guy.name}")
        print(f"{other_guy.name} loses! {other_guy.damage} points")


    def __str__(self):
        return f"{self.name}: {self.health}"
p1 = fighter("mayank")
p2 = fighter("kinshul")

print(p1.name,p1.health)
print(p2.name,p2.health)

p1.attack(p2)

print(p2.name,p2.health)
# created battack which sucks 20 poits when attacks
class boxer(fighter):
    def battack(self,other_guy):
        other_guy.health = other_guy.health - self.damage * 2

p3 = boxer("akshay")
p3.battack(p2)
#this is my 

print(p1)
