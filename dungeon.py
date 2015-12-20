import os
import re


class Dungeon:

    """docstring for Dungeon"""
    level = 0
    spawn = 0
    treasures_taken = 0

    def __init__(self, file_name):
        self.file_name = os.path.join(os.path.realpath('maps'), file_name)
        self.directions = {'up': self.up,
                           'down': self.down,
                           'left': self.left,
                           'right': self.right}
        self.hero = ''
        self.hero_pos = [0, 0]
        self.next_pos = []

    def __map_read(self):
        with open(self.file_name, 'r') as f:
            return f.readlines()

    def __map_write(self, upd_map):
        with open(self.file_name, 'w') as f:
            f.write("".join(upd_map))

    def __path(self, x, y):
        m = self.__map_read()
        return m[x][y]

    # replace position of hero in map+
    def __move(self, x, y, char='.'):
        m = self.__map_read()
        print(m[x])
        repl = list(m[x])
        repl[y] = char
        m[x] = "".join(repl)
        self.__map_write(m)

    # find start position/current position of start/hero
    def current_position(self, point='H'):
        map_file = self.__map_read()
        for i in range(len(map_file)):
            try:
                self.hero_pos = [i, map_file[i].index(point)]
                return [i, map_file[i].index(point)]  # return [0,0]
            except ValueError:
                continue

    def print_map(self):
        for elem in self.__map_read():
            print(elem)

    def spawn(self, hero):
        if Dungeon.spawn == 0:
            self.hero = hero
            p = self.current_position('S')
            self.__move(p[0], p[1], 'H')
            Dungeon.spawn += 1
            return True

    def move_hero(self, direction):
        if direction in self.directions and self.directions[direction]():
            p = self.fasda(direction)
            return self.obsticle(self.__path(p[0], p[1]))
        return False

    def up(self):
        if self.current_position()[0] - 1 >= 0:
            self.next_pos = [self.current_position()[0] - 1, self.current_position()[1]]
            return True
        return False

    def down(self):
        print()
        if self.current_position()[0] + 1 <= len(self.__map_read()):
            self.next_pos = [self.current_position()[0] + 1, self.current_position()[1]]
            return True
        return False

    def left(self):
        if self.current_position()[1] - 1 > 0:
            self.next_pos = [self.current_position()[0], self.current_position()[1] - 1]
            return True
        return False

    def right(self):
        if self.current_position()[1] + 1 <= len(list(self.__map_read()[0])):
            self.next_pos = [self.current_position()[0], self.current_position()[1] + 1]
            return True
        return False

    def obsticle(self, pos):
        if pos == "#":
            return False
        if pos == ".":
            self.__move(self.next_pos[0], self.next_pos[1], 'H')
            self.__move(self.hero_pos[0], self.hero_pos[1])
            return True
        if pos == "G":
            return self.next_level()
        if pos == "T":
            self.__move(self.next_pos[0], self.next_pos[1], 'H')
            self.__move(self.hero_pos[0], self.hero_pos[1])
            # return self.pick_treasure()
        if pos == "E":
            if self.hero_attack(self.hero):
                self.__move(self.hero_pos[0], self.hero_pos[1])
                self.__move(self.next_pos[0], self.next_pos[1], 'H')
            return "DEAD"

    def fasda(self, direction):
        pos = self.current_position('H')
        print(pos)
        if direction == "up":
            pos[0] -= 1
            self.next_pos = pos
            return pos

        if direction == "down":
            pos[0] += 1
            self.next_pos = pos
            return pos

        if direction == "left":
            pos[1] -= 1
            self.next_pos = pos
            return pos

        if direction == "right":
            pos[1] += 1
            self.next_pos = pos
            return pos

    def pick_treasure(self):
        pass

    def next_level(self):
        return "Congrats you finish {} are you ready for {}".format()

    def hero_attack(self, by):
        pass


class Fight(Dungeon):
    """docstring for Fight"""
    def __init__(self, arg):
        super(Fight, self).__init__()
        self.arg = arg

    #return range
    def auto_fight(self):
        m = self.__map_read()
        h_pos = self.hero_pos
        vertical = "".join([x[h_pos[1]] for x in m])
        if "E" or "T" in m[h_pos[0]]:
            if "#" not in m[h_pos[0]][h_pos[1]: self.current_position('E')[1]]:
                return len(m[h_pos[0]][h_pos[1]: self.current_position('E')[1]])
        if "E" or "T" in vertical:
            if "#" not in vertical[h_pos[1]: self.current_position()[1]]:
                return len(vertical[h_pos[1]: self.current_position()[1]])
        return False
