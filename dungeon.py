class Dungeon:

    """docstring for Dungeon"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.directions = ['up', 'down', 'left', 'right']
        self.s_point = [0, 0]
        self.h_point = self.s_point

    def __map_read(self):
        with open(self.file_name, 'r') as f:
            content = f.readlines()
            return content

    def __map_write(self, upd_map):
        with open(self.file_name, 'r') as f:
            f.write(upd_map)

    def print_map(self):
        for elem in self.__map_read():
            print(elem)

    def spawn(self, hero):
        m = self.__map_read()
        for i in len(m):
            if 'S' in m[i]:
                m[i].replace('S', 'H')
                with open(self.file_name, 'r') as f:
                    f.write(m)
                return True
        return False

    def move_hero(self, direction):
        return True if self.direction in self.directions and self.obsticle(self.direction) else False

    def obsticle(self, direction):
        pass

    def up(self):
        if self.start_possition['x'] + 1 <= len(self.__map_read()):
            return True
        return False

    def down(self):
        if self.start_possition['x'] - 1 > 0:
            return True
        return False

    def left(self):
        if self.start_possition['y'] - 1 > 0:
            return True
        return False

    def right(self):
        if self.start_possition['y'] + 1 <= len(list(self.__map_read[0])):
            return True
        return False

    # find start position (hero position)
    def start_possition(self, point='S'):
        map_file = self.__map_read()
        for i in len(map_file):
            try:
                return {"x": i, 'y': map_file[i].index('S')}  # return [0,0]
            except ValueError:
                continue
