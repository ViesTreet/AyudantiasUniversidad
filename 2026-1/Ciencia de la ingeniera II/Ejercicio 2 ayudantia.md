# 🏛️ El Linaje de los Guardianes: Desafío de Herencia
**Curso:** Ciencia de la Ingeniería II  
**Tema:** Herencia y Polimorfismo en Python

---

### 📜 Historia del Reino
En el antiguo Reino de los Objetos, todos los defensores descienden de la clase ancestral **Guardian**. Aunque todos comparten una base, los Guerreros y Magos han evolucionado sus propias técnicas. Tu misión es codificar este linaje.

### 🛠️ El ADN Base (Clase Padre)
Define la estructura fundamental en tu script de Python:

```python
class Guardian:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def presentarse(self):
        return f"Soy {self.nombre}, Guardian de nivel {self.nivel}."

    def accion_principal(self):
        return "El guardian se mantiene en guardia."
```

---

### ⚔️ Las 5 Pruebas de Linaje

#### Prueba 1: El Heredero del Acero

Crea una clase llamada **Guerrero** que herede de **Guardian**.

- **Misión:** Debe tener un atributo adicional llamado **fuerza**. Usa **super().__init__** para inicializar el nombre y nivel.

#### Prueba 2: El Heredero de los Arcanos

Crea una clase llamada **Mago** que herede de **Guardian**.

- **Misión:** Debe tener un atributo llamado **mana**. Al igual que el Guerrero, usa **super()** para los datos base.

#### Prueba 3: Especialización de Habilidades (Overriding)

El Guerrero no solo "se mantiene en guardia".

- **Misión:** Redefine (override) el método **accion_principal** en la clase **Guerrero** para que devuelva: **"El guerrero ataca con su espada!"**.

#### Prueba 4: El Grito del Mago

El Mago tiene una forma distinta de presentarse.

- **Misión:** Redefine el método **presentarse** en la clase **Mago** para que incluya su nivel de mana. Ejemplo: **"Soy [nombre], un mago de nivel [nivel] con [mana] de poder mágico"**.

#### Prueba 5: El Ejército del Rey (Polimorfismo)

- **Misión:** Crea una lista llamada **ejercito** que contenga un **Guerrero** y un **Mago**. Luego, usa un ciclo **for** para que ambos ejecuten su **accion_principal()**. Observa cómo cada uno responde de forma distinta a pesar de estar en la misma lista.