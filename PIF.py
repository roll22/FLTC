class PIF:
    def __init__(self):
        self.__data = []

    def __setitem__(self, key, pos):
        self.__data[key] = pos

    def add(self, key, pos):
        self.__data.append((key, pos))

    def __str__(self):
        to_return = '---PIF---\n'
        for element in self.__data:
            to_return += str(element[0]) + (" " * (20 - len(str(element[0])))) + "\t\t --- \t\t" + (" " * (10)) + str(
                element[1]) + "\n"
        return to_return
