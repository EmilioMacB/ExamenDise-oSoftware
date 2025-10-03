```python
## 📝 PREGUNTAS TEÓRICAS (10 puntos)
### Pregunta 1: LSP (5 pts)
**a) (5 pts)** Explica qué es LSP y cómo se aplica al ejemplo:
```python
class Usuario:
    def calcular_limite_prestamos(self):
        return 3
class Estudiante(Usuario):
    def calcular_limite_prestamos(self):
        return 3
```
**Respuesta:**
```
Dice que los objetos de una subclase deben poder sustituir a los objetos de la superclase o clase base sin que se altere el funcionamiento del programa. ejemplo: si tu codigo funciona con un "Usuario" tambien deberia de funcionar con un "Estudiante".
En el ejemplo funciona porque el 'método calcular_limite_prestamos' se comporta igualito que el de la clase Usuario, ambos devolviendo un entero 3. El tipo de dato de retorno y comportamiento son los mismos.
```
**b) (5 pts)** Da un ejemplo que VIOLE LSP y explica por qué:
```python
class Usuario:
    def calcular_limite_prestamos(self):
        return 3
class EstudianteSuspendido(Usuario):
    def calcular_limite_prestamos(self):
         raise ValueError("El usuario esta suspendido") 
_________________________________________________________________
```
Este código viola LPS porque un estudiante que ya está suspendido no tiene derecho a ningún préstamo.
Si se llama a la función esperando obtener un número para hacer algún cálculo y devuelve esta excepción, entonces no se va a poder usar de la misma forma.

### Pregunta 2: ISP (5 pts)
**a) (5 pts)** ¿Por qué esta interfaz VIOLA ISP?
```python
class IGestionBiblioteca:
    def agregar_libro(self): pass
    def buscar_libro(self): pass
    def realizar_prestamo(self): pass
    def generar_reporte(self): pass
    def hacer_backup(self): pass
```
**Respuesta:**
```
Porque como hemos estado trabajando, es una interfaz monolítica que esta obligando a que cualquier clase que la implemente a tener conocimiento de métodos que quizás no necesita. Quiere hacer todo.
Una biblioteca nomas deberia hacer quiza los primeros 3 metodos pero la parte de generar reporte o  backup no le corresponde
```
**b) (5 pts)** Propón cómo segregar esta interfaz:
```
Interface 1: IGestionarInventario - Métodos: agregar_libro(), buscar_libro()
Interface 2: IGestionPrestamos - Métodos: realizar_prestamo()
Interface 3: IAdmin - Métodos: generar_reporte(), hacer_backup()
```
---
```
