<h1 style="text-align:center">Ejercicio 1 de ayudantia ciencia de  la ingenieria II</h1>
# Gremio de Héroes: La Prueba de los Lambdas

Contexto de la Aventura
¡Bienvenido al Gremio de Aventureros, Programador! El Maestro del Gremio necesita tu ayuda para organizar a los nuevos reclutas. Para probar tu valía, deberás usar tu magia más concisa: **Las funciones Lambda** aplicadas a **Objetos**.

## El Códice Base
Primero, copia este código en tu pergamino (tu editor de Python). Define a nuestros reclutas:

``` python
class Heroe:
    def __init__(self, nombre, clase, fuerza, agilidad):
        self.nombre = nombre
        self.clase = clase
        self.fuerza = fuerza
        self.agilidad = agilidad

    def __repr__(self):
        return f"{self.nombre} ({self.clase}) - F:{self.fuerza} A:{self.agilidad}"

# La lista de reclutas del gremio
reclutas = [
    Heroe("Arthur", "Guerrero", 85, 40),
    Heroe("Merlín", "Mago", 20, 30),
    Heroe("Lira", "Pícara", 45, 95),
    Heroe("Grom", "Orco", 95, 20),
    Heroe("Elora", "Mago", 25, 60)
]
```
## Las 5 Pruebas del Maestro

Resuelve cada uno de los siguientes desafíos en una sola línea de código utilizando funciones `lambda`.

### Prueba 1: El Rango de Fuerza

El Rey ha pedido que los héroes formen una línea desde el más fuerte hasta el más débil para una inspección real.

- [ ] **Misión:** Usa la función `sorted()` y una función `lambda` para ordenar la lista `reclutas` de mayor a menor según su atributo `fuerza`. Guarda el resultado en una variable llamada `formacion_fuerza` e imprímela.
    

### Prueba 2: La Misión Sigilosa

Hay un dragón durmiendo en la cueva y necesitamos robar su tesoro sin despertarlo. Solo aquellos con una agilidad superior a 50 sobrevivirán.

- [ ] **Misión:** Usa la función `filter()` junto con una función `lambda` para obtener solo los héroes con `agilidad > 50`. Guarda el resultado en una lista llamada `equipo_sigilo` e imprímela.
    

### Prueba 3: El Oráculo de Nombres

El Oráculo ciego del gremio no necesita saber las estadísticas, solo quiere una lista con los nombres de los héroes y su clase en formato texto para anotarlos en el registro mágico.

- [ ] **Misión:** Usa la función `map()` y una `lambda` para transformar la lista de objetos `reclutas` en una simple lista de strings con el formato `"Nombre el Clase"` (ej. `"Arthur el Guerrero"`). Guárdalo en `registro_nombres` e imprímelo.
    

### Prueba 4: El Torneo por Categorías

Se va a celebrar un torneo. El organizador necesita que la lista esté ordenada alfabéticamente por la `clase` del héroe (Guerrero, Mago, Orco, etc.). Pero, si hay dos héroes de la misma clase (como los Magos), el más ágil debe ir primero.

- [ ] **Misión:** Usa `sorted()` con una función `lambda` que devuelva una tupla para ordenar primero por `clase` y luego por `agilidad` (de mayor a menor agilidad). Guarda el resultado en `orden_torneo`.
    

### Prueba 5: La Elección del Campeón

¡Un demonio gigante ha atacado el pueblo! No hay tiempo para equipos, necesitamos enviar a nuestro campeón absoluto. El campeón es aquel que tenga la suma más alta de sus atributos (`fuerza` + `agilidad`).

- [ ] **Misión:** Usa la función `max()` y una función `lambda` como su argumento `key` para encontrar al único objeto `Heroe` que tenga el mayor poder total. Imprime el nombre del campeón elegido.
    

---

¡Misión Cumplida! Si lograste resolver los 5 acertijos usando lambdas, ¡has salvado al Gremio y ganado el título de Archimago de Python!

