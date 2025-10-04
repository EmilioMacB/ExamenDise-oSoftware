from abc import ABC, abstractmethod
from biblioteca_examen import Libro 

class EstrategiaBusqueda(ABC):
   
    @abstractmethod
    def coincide(self, libro: Libro, valor: str) -> bool:
        pass

# Estrategias

# revisa si el titulo del libro contiene el "valor" que se busca
class BusquedaPorTitulo(EstrategiaBusqueda):  
    def es_coincidencia(self, libro: Libro, valor: str) -> bool:
        return valor.lower() in libro.titulo.lower() #minusculas para que no sea caseSensitive


# revisa si el nombre del autor contiene el "valor" que se busca
class BusquedaPorAutor(EstrategiaBusqueda):
    def es_coincidencia(self, libro: Libro, valor: str) -> bool:
        return valor.lower() in libro.autor.lower() #minusculas para que no sea caseSensitive


# revisa si el ISBN del libro es exactamente igual al "valor" que se busca
class BusquedaPorISBN(EstrategiaBusqueda):
    def es_coincidencia(self, libro: Libro, valor: str) -> bool:
        return libro.isbn == valor


# revisa si la disponibilidad del libro es igual al "valor" que se busca
class BusquedaPorDisponibilidad(EstrategiaBusqueda):
    def es_coincidencia(self, libro: Libro, valor: bool) -> bool:
        return libro.disponible == valor