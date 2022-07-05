import time as time
class Ash:
    def __init__(self):
        self.captured_pokemons = 1
        self.pokemon_houses_visited = set()
        self.actual_position = [0, 0]
        self.list_size_houses_visited = 1
        
    def to_walk(self,direction):
        """walk a house"""
        if direction == 'N' or direction == 'S':
            if direction == 'N':
                self.actual_position[1] += 1
            else:
                self.actual_position[1] -= 1
            
            self.pokemon_houses_visited.add(tuple(self.actual_position))
        else:
            if direction == 'L':
                self.actual_position[0] += 1
            else:
                self.actual_position[0] -= 1
            self.pokemon_houses_visited.add(tuple(self.actual_position))
        
        return len(self.pokemon_houses_visited)

    def has_pokemon(self,actual_size_list_houses_visitadas):
        """ Check if it exists in actual position """
        if actual_size_list_houses_visitadas > self.list_size_houses_visited:
            self.capture_pokemon()
            self.list_size_houses_visited = actual_size_list_houses_visitadas
    
    def capture_pokemon(self):
        """ Increase one in quantity of captured pokemons """
        self.captured_pokemons += 1


if __name__ == "__main__":
    ash = Ash()
    ash.pokemon_houses_visited.add(tuple(ash.actual_position))
    moviments = input("input the moviments made by Ash: \n")

    initial_time = time.time()
    for direction in moviments.upper():
        actual_size_list_houses_visitadas = ash.to_walk(direction)
        ash.has_pokemon(actual_size_list_houses_visitadas)
    
    print(f'The Ash captured {ash.captured_pokemons} pokemons')
    final_time = time.time() - initial_time

    """ For check the time of execution descoment the line bottom """
    """ print(f'Final time {final_time}') """
