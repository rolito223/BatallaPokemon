# CONSIGNA:
```
    /*
    * Enunciado: Crea un programa que calcule el daño de un ataque durante
    * una batalla Pokémon.
    * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    *   (buscar su efectivisdad)
    * - El programa recibe los siguientes parámetro:
    *  - Tipo del Pokémon atacante.
    *  - Tipo del Pokémon defensor.
    *  - Ataque: Entre 1 y 100.
    *  - Defensa: Entre 1 y 100.
    */
```



## NOTAS:

 | Tipo | Efectiva | Neutral | No es efectivo |
 | :----: | :----: | :----: | :----: |
 | Agua | Fuego | Electrico | Planta |
 | Fuego | Planta | Electrico | Agua |
 | Planta | Electrico | Agua | Fuego |
 | Electrico | Agua | Fuego | Planta |
