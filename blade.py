class fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
p1 = fighter("mayank")
p2 = fighter("kinshul")

print(p1.name)
print(p2.name)
