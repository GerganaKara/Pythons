
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
