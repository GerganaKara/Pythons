class Dungeon:
    """docstring for Dungeon"""
    def __init__(self, file_name):
        self.file_name = file_name
    
    def __map(self, file_name):
        with open(file_name, 'r') as map_file:
            return map_file

    def print_map(self):
        print(self.__map(self.file_name))
