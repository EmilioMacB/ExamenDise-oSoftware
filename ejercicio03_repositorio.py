
from EXAMEN_SOLID_POO.ejercicio03_intrerfaces import IRepositorio

class RepositorioArchivo(IRepositorio):
   
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo

    def guardar(self, libros: list, prestamos: list):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")
        print(f"[Archivo] Datos guardados exitosamente en '{self.archivo}'.")

    def cargar(self):
        try:
            with open(self._archivo, 'r') as f:
                data = f.read()
            return True
        except:
            return False

# --- BONUS ---
class RepositorioMemoria(IRepositorio): #simula guardar en memoria (no hay persistencia)
   
    def guardar(self, libros: list, prestamos: list):
        print(f"[Memoria] {len(libros)} libros y {len(prestamos)} préstamos 'guardados' en memoria.")