from hero import Hero, Enemy, GameLogic, Spell, Weapon, Treasure
from dungeon import Dungeon

class CLI(object):
    """docstring for CLI"""
    def __init__(self):
        self.main()

    def main(self):
        while True:
            self.make_hero()

    def make_hero(self):
        name,title,health,mana,mana_regeneration_rate = ''
        asd = {name: input("Please enter name for your Hero: "),
               title: input("Please enter title for {}: "),
               health: 100,
               mana: 100,
               mana_regeneration_rate: 2}
        Hero(asd)
        print(Hero)


if __name__ == '__main__':
    CLI()