from .ash import Ash

class Game:

    def start(self,route):
        ash = Ash()
        for direction in route.upper():
            current_size_list_visited_houses, current_position = ash.walk(direction)
            ash.has_pokemon(current_size_list_visited_houses)
    
        return ash.captured_pokemons