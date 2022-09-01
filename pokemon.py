class PokemonClass():
    def __init__(
            self,
            nombre: str,
            tipo: str,
            defensa: int,
            ataques: dict) -> None:

        self._nombre = nombre
        self._tipo = tipo
        self._defensa = defensa
        self._ataques = ataques
        self._vida = 100

    def atacar(self, ataque) -> int:
        return self._ataques[ataque]

    def revivir(self):
        self._vida = 100

    def restarvida(self, danio):
        self._vida -= danio

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre) -> None:
        self._nombre = nombre


    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo : str) -> None:
        self._tipo = tipo

    @property
    def defensa(self) -> str:
        return self._defensa
    
    @defensa.setter
    def defensa(self, defensa) -> None:
        self._defensa = defensa

    @property
    def ataques(self) -> dict:
        return self.ataques
    
    @ataques.setter
    def ataques(self, ataques : dict) -> None:
        self._ataques = ataques

    @property
    def vida(self) -> int:
        return self._vida
