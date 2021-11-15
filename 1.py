class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

james = Gamer.gamer_from_string('James, 34, 2, 45')
jane = Gamer.gamer_from_string('Jane, 24, 3, 5')
#print(james.get_age())
#print(jane.get_level())
print(james.gamer_from_string())
print(jane.gamer_from_string())