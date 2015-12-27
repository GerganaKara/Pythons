class DungeonGameException(Exception):
    pass


class GameLogic(object):

    hero = 0
    enemy = 0
    """docstring for GameLogic"""
    def __init__(self, *args, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        try:
            self.mana_regeneration_rate = kwargs['mana_regeneration_rate']
        except KeyError:
            pass
        self.maximum_mana = kwargs['mana']
        self.maximum_health = kwargs['health']
        self.dmg = 0

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

    def regenerate(self):
        if isinstance(self, Hero):
            self.mana = min(self.mana + self.mana_regeneration_rate, self.maximum_mana)

    def take_mana(self, mana_potion, *args):
        try:
            self.mana = min(self.mana + len(args) *
                            self.mana_regeneration_rate, self.maximum_mana)
        except NameError:
            pass
        self.mana = min(self.mana + mana_potion, 100)

    def attack(self, by='weapon'):
        pass
        # return weapon.dmg

    def take_damage(self, dmg_points):
        self.health -= dmg_points if self.health > dmg_points else 0

    def exp_formula(self):
        pass


class Hero(GameLogic):

    """docstring for Hero"""

    def __init__(self, **kwargs):
        super(Hero, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.weapon = {'weapon': '', 'spell': ''}
        self.experience = 0
        self.dmg = 0
        self.lvl = 1
        GameLogic.hero += 1

    def __str__(self):
        return "The mighty {} aslo known as the {}".format(self.name, self.title)

    def __repr__(self):
        return "The mighty {} aslo known as the {}".format(self.name, self.title)

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def equip(self, weapon):
        # equip, работи като суич, в 1 променлива self.weapon = {weapon:'', spell:''},
        # като weapon идва от списък с оръжия и съответно списък с магии
        pass

    def learn(self, spell):
        pass


class Enemy(GameLogic):

    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.experience = 0
        self.lvl = 1
        with open('maps/monsters.txt', 'r') as f:
            f.readlines()

    def __str__(self):
        return "The mighty {} aslo known as the {}".format(self.name, self.title)

    def __repr__(self):
        return "The mighty {} aslo known as the {}".format(self.name, self.title)

    def __init(self):



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

    # def mana_cost(self):
    # return True if self.mana_cost >= mana_points else
    # DungeonGameException("Not enought mana for {}".format(self.name))

    # def mana_cost(self):
    #     if self.mana -= self.mana_cost < 1:
    #         return DungeonGameException("Error mana_cost line 73")
    #     return self.mana -= self.mana_cost

    def cast_range(self):
        pass


class Weapon:

    """docstring for Weapon"""
    equipment = {}

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.dmg = kwargs['damage']
        #equipment[self.name] = self.dmg

    def __str__(self):
        return "Current chosen weapon is {}".format(self.name)

    def __repr__(self):
        return "Current chosen weapon is {}".format(self.name)

    def __int__(self):
        return self.dmg


class Treasure:

    def __init__(self):
        pass


class Fight(object):

    """docstring for Fight"""

    def __init__(self, arg):
        super(Fight, self).__init__()
        self.arg = arg


class Experience(object):
    """docstring for Experience"""
    def __init__(self, arg):
        super(Experience, self).__init__()
        self.experience = 0
        self.exp_to_next_lvl = 0
        self.lvl = 0

    def __add__(self, other):
        return self.experience + other.experience

    def __eq__(self, other):
        return self.experience == other.experience

    def __hash__(self):
        return hash(self.experience)

    def __str__(self):
        return "{} - current lvl {} \n Experience: {} / {}".format(self.name, self.lvl, self.experience, self.exp_to_next_lvl)

    def __repr__(self):
        return "{} - current lvl {} \n Experience: {} / {}".format(self.name, self.lvl, self.experience, self.exp_to_next_lvl)

    def exp_model(self):
        with open(os.path.join(os.path.abspath('maps'), 'experience.txt'), 'r') as f:
            return f.readlines()

    def lvl_up(self):
        self.exp_to_next_lvl = exp_model()[self.lvl].split(',')[1].replace('\n', '')
        if self.experience >= self.exp_to_next_lvl:
            self.lvl += 1
            self.exp_to_next_lvl = exp_model()[self.lvl].split(',')[1].replace('\n', '')
            return True
        return False

    def f(self):
        pass
