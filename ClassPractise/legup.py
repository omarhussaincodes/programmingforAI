# help(dir)
# help(hasattr)
# help(id)
import inspect


class Animal():

    def __init__(self, name, color, noise):
        self.name = name
        self.color = color
        self.noise = noise

    def make_noise(self):
        return self.noise

    def __str__(self):
        return (f"This is {self.name}'s voice: {self.noise}")

    def __add__(self, other):
        return f"Playing with genes of {self.name} and {other.name}"

    # default behaviour check for same instance - referencing same memory
    def __eq__(self, __o: object):
        if (self.noise == __o.noise):
            return True

        return False


dog = Animal("Dog", "Grey", "Bark Bark!!")
print(dog.make_noise())
cat = Animal("Cat", "Black", "Meoww!")
print(cat.make_noise())
print(cat.__str__())
print(dog.__str__())
print(cat.__add__(dog))
print(cat.__eq__(dog))

# Code/Object Introspection

# print(dir(Animal))
# check if particular class instance i.e obj has a particular property or attribute
# print(hasattr(cat, "name"))
# print(isinstance(dog, Animal))
# print(callable(Animal))

# print(inspect.getmembers(cat))
class Games():

    def __init__(self, name: str, type: str, number_of_players_involved: int):
        self.name = name
        self.type = type
        self.number_of_players_involved = number_of_players_involved

    def play_game(self):
        print(
            f"Game of {self.name} of {self.type} type is played with {self.number_of_players_involved} players involved")

class IndoorGames(Games):
    def __init__(self, location, name, type, number_of_players_involved):
        super().__init__(name, type, number_of_players_involved)
        self.location = location

    # method overriding - Inhertance involved - overriding parent class method i.e play_game()
    def play_game(self):
        print(
            f"Game of {self.name} of {self.type} type is played with {self.number_of_players_involved} players involved in {self.location} ")
        super().play_game()

class OutdoorGames(Games):
    def __init__(self, weather, name, type, number_of_players_involved):
        super().__init__(name, type, number_of_players_involved)
        self.weather = weather

    # method overriding - Inhertance involved
    def play_game(self):
        print(
            f"Game of {self.name} of {self.type} type is played with {self.number_of_players_involved} players involved on a perfect {self.weather} weather ")
        super().play_game()


chess = IndoorGames("living room", "Chess", "Indoor", 2)
football = IndoorGames("Overcast", "Football", "Outdoor", 22)
print(chess.play_game())
print(football.play_game())

print(issubclass(Games, IndoorGames))
