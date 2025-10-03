from biblioteca_examen import SistemaBiblioteca
from ejercicio01_OCP import EstrategiaBusqueda # se importa la clase abstracta

class SistemaBibliotecaOCP(SistemaBiblioteca):
    def buscar_libro(self, estrategia: EstrategiaBusqueda, valor):
        
        resultados = []
        for libro in self.libros:
            if estrategia.es_coincidencia(libro, valor):
                resultados.append(libro)
        return resultados
    
    # en vez de el if y elif se usa la estrategia que implementa la interfaz EstrategiaBusqueda

