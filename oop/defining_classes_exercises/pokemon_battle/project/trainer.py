from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in map(lambda x: x.name, self.pokemon):
            return 'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if not pokemons:
            return f'Pokemon is not caught'
        self.pokemon.remove(pokemons[0])
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- '
        for pokemon in self.pokemon:
            result += pokemon.pokemon_details() + '\n'
        return result
