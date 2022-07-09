class Ash:
    def __init__(self):
        self.captured_pokemons = 1
        self.houses_visited = {(0, 0)}
        self.current_position = [0, 0]
        self.list_size_visited_houses = 1
        
    def walk(self,direction):
        """walk a house"""
        if direction in 'NSLO':
            if direction == 'N' or direction == 'S':
                if direction == 'N':
                    self.current_position[1] += 1
                else:
                    self.current_position[1] -= 1
                
                self.houses_visited.add(tuple(self.current_position))
            else:
                if direction == 'L':
                    self.current_position[0] += 1
                else:
                    self.current_position[0] -= 1
                self.houses_visited.add(tuple(self.current_position))
        
        return len(self.houses_visited), self.current_position

    def has_pokemon(self,current_size_list_visited_houses):
        """ Check if it exists in actual position """
        if current_size_list_visited_houses > self.list_size_visited_houses:
            self.capture_pokemon()
            self.list_size_visited_houses = current_size_list_visited_houses
        
        return self.captured_pokemons
    
    def capture_pokemon(self):
        """ Increase one in quantity of captured pokemons """
        self.captured_pokemons += 1
    
    