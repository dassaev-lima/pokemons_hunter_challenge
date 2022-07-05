import time as time
from models.ash import Ash

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
