from hero import *
from dungeon import Dungeon


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)

h.equip(w)

h.attack(by="weapon") == 20


print(str(h))

print(isinstance(h, Hero))

dungeon = Dungeon('level1.txt')
print(dungeon.spawn(h))
dungeon.print_map()
print(dungeon.move_hero('right'))