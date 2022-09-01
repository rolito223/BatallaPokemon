class BatallaPokemon():
    def __init__(self):
        self._dict_efectividad = {
            'agua' : {
                'fuego' : 2,
                'electrico' : 1,
                'planta' : 0.5
            },
            'fuego' : {
                'planta' : 2,
                'electrico' : 1,
                'agua' : 0.5
            },
            'planta' : {
                'electrico' : 2,
                'agua' : 1,
                'fuego' : 0.5
            },
            'electrico' : {
                'agua' : 2,
                'fuego' : 1,
                'planta' : 0.5
            }
        }

    def ataque(self, atacante, ataque, defensor):
        efectividad_ataque = self.efectividad(atacante.tipo, defensor.tipo)
        danio = 50*(atacante.atacar(ataque)/defensor.defensa) * efectividad_ataque
        defensor.restarvida(danio)
        if defensor.vida <= 0:
            return f'{defensor.nombre} esta fuera de combate'
        
        if efectividad_ataque == 2:
            return f'{ataque} fue muy efectivo'

        return f'El ataque causo {danio}'

    def efectividad(self, tipo1, tipo2):
        return self._dict_efectividad[tipo1][tipo2]

