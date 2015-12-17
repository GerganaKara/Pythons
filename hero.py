class DungeonGameException(Exception):
    pass


class Hero(GameLogic):

    """docstring for Hero"""

    def __init__(self, **kwargs):
        GameLogic.__init__(self, **kwargs)
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.weapon = {'weapon': '', 'spell': ''}

    def __int__(self):
        return self.health

    def __add__(self, other):
        return self.health + self.take_healing(other)

    def __iadd__(self, other):
        return self.health - other.attack()

    def __eq__(self, other):
        pass

    def __hash__(self):
        return hash(self.health)

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def equip(self, weapon):
        # equip, работи като суич, в 1 променлива self.weapon = {weapon:'', spell:''},
        # като weapon идва от списък с оръжия и съответно списък с магии
        pass

    def learn(self, spell):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass


class Enemy():

    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.dmg = damage


class Spell:

    """docstring for weapon"""
    spells = {}

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.damage = kwargs['damage']
        self.mana_cost = kwargs['mana_cost']
        self.cast_range = kwargs['cast_range']
        self.spells[self.name] = self.damage

    def __str__(self):
        return "Default spell: {}".format(self.name)

    def __repr__(self):
        return "Default spell: {}".format(self.name)

    def mana_cost(self):
        return True if self.mana_cost >= mana_points else DungeonGameException("Not enought mana for {}".format(self.name))

    def mana_cost(self):
        if self.mana -= self.mana_cost <= 0:
            return DungeonGameException("Error mana_cost line 73")
        return self.mana -= self.mana_cost

    def cast_range(self):
        if cast_range == 1:
            attack


class Weapon:

    """docstring for Weapon"""
    equipment = {}

    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg
        equipment[self.name] = self.dmg

    def __str__(self):
        return "Current chosen weapon is {}".format(self.name)

    def __repr__(self):
        return "Current chosen weapon is {}".format(self.name)

    def __int__(self):
        return self.dmg


class GameLogic:

    """docstring for GameLogic"""

    def __init__(health=100, mana=100, mana_regeneration_rate=2):
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.maximum_mana = mana
        self.maximum_health = health
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.dmg = 0

    def is_alive(self):
        return True if self.health > 0 else False

    def can_cast(self):
        return True if self.mana > 0 else False

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        self.health = min(self.health + healing_points, self.maximum_health)
        return self.health

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_mana(self, mana_potion, *args):
        try:
            self.mana = min(self.mana + len(args) *
                            self.mana_regeneration_rate, self.maximum_mana)
        except NameError:
        self.mana = min(self.mana + mana_potion, 100)

    def attack(self, by='weapon'):
        return weapon.dmg

    def take_damage(self, dmg_points):
        self.health -= dmg_points if self.health > dmg_points else 0




class Treasure():

    def __init__(self):
        pass