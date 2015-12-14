Class Enemy:

    def __init __(self, health, max_health, name, mana, max_mana, damage):

        self.name = names
        self.health = healths
        self.mana = mana
        self.damage = damage

    def __str__(self):
        return "Enemy".format(self.name)

    def __repr__(self):
        return str(self)

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return "{} has {} health".format(self.name, self.health)

    def get_mana(self):
        return "{} has mana {}".format(self.name, self.mana)

    def take_healing(self, healing_points):
        is_healed = False
        try:
            if self.health == 0:
                raise DeadException

            if self.health + healing_points > max_health:
                self.health = max_health

            else:
                self.health = sel.health + healing_points
                is_healded = True

        except DeadException:

            print("too late for you, sorry :( ")

    def take_mana(self, mana_points, is_moved=False):
        # if is_moved == True:

        if self.mana + mana_points > max_mana:
            self.mana = max_mana
        else:
            self.mana += mana_points

# go and check equipment if there is spell, take damage points
    def attack(self, **kwargs):
        attack_points = 0

        if kwargs[by] == "spell" and is_equiped == True:
            self.damage += attack_points 

    def move_hero(self,direction):
        is_moved = False
        pass

    def is_equiped(self, damage):
        pass

