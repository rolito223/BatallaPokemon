from batalla import BatallaPokemon
from pokemon import PokemonClass

charmander = PokemonClass(
    'Charmander',
    'fuego',
    70,
    {
        'Embestir': 30,
        'Brasas': 50,
        'Remolino de Fuego': 70,
        'Rasguñar': 50
    }
)

squirtle = PokemonClass(
    'Squirtle',
    'agua',
    80,
    {
        'Embestir': 30,
        'Chorro de Agua' : 50,
        'Remolino' : 75,
        'Cabezaso' : 60
    }
)

bulbasaur = PokemonClass(
    'Bulbasaur',
    'planta',
    90,
    {
        'Embestir': 30,
        'Latigo Selva' : 50,
        'Rayo Solar' : 80,
        'Cortar' : 70
    }
)

pikachu = PokemonClass(
    'Pikachu',
    'electrico',
    85,
    {
        'Embestir' : 30,
        'Relampago' : 50,
        'Trueno' : 75,
        'Cola de latigo' : 50
    }
)

batalla = BatallaPokemon()

print(batalla.ataque(charmander, 'Embestir', squirtle))

print(batalla.ataque(pikachu, 'Trueno', bulbasaur))
