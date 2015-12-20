# test_dungeon.py
from dungeon import Dungeon
from hero import Hero
import unittest


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon('test_level1.txt')
        self.level = ['..##.....T\n',
                      '#S##..###.\n',
                      '#.###E###E\n',
                      '#.E...###.\n',
                      '###T#####G\n']

    def test_Dungeon_spawn(self):
        self.dungeon._Dungeon__map_write(self.level)
        h = Hero(name="Bron", title="Dragonslayer", health=100,
                 mana=100, mana_regeneration_rate=2)
        self.assertEqual(self.dungeon.spawn(h), True)
        self.assertEqual(self.dungeon.spawn(h), False)
        self.dungeon._Dungeon__map_write(self.level)

    def test_Dungeon_current_position(self):
        self.dungeon._Dungeon__map_read()
        self.assertTrue(self.dungeon.current_position('S'), list)
        self.assertEqual(self.dungeon.current_position('S'), [1, 1])
        self.assertEqual(self.dungeon.current_position('V'), None)

    def test_Dungeon___path(self):
        self.assertEqual(self.dungeon._Dungeon__path(1, 1), 'S')
        self.assertNotEqual(self.dungeon._Dungeon__path(0, 0), 'S')
        self.assertTrue(self.dungeon._Dungeon__path(3, 0), str)

    def test_Dungeon__move_hero(self):
        pass

    def test_Dungeon__up(self):
        pass

    def test_Dungeon__down(self):
        pass

    def test_Dungeon__left(self):
        pass

    def test_Dungeon__right(self):
        pass


if __name__ == '__main__':
    unittest.main()
