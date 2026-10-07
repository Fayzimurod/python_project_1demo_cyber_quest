class Player:
    def __init__(self, name="Кибер-Странник"):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.credits = 50
        self.attack = 15
        self.inventory = ["Энергоячейка"]

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "credits": self.credits,
            "attack": self.attack,
            "inventory": self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        p = cls(data["name"])
        p.hp = data["hp"]
        p.max_hp = data["max_hp"]
        p.credits = data["credits"]
        p.attack = data["attack"]
        p.inventory = data["inventory"]
        return p
