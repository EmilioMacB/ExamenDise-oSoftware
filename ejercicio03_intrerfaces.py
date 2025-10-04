from abc import ABC, abstractmethod

class IRepositorio(ABC): #contrato a seguir
    @abstractmethod
    def guardar(self, libros: list, prestamos: list): 
        pass


    @abstractmethod
    def cargar(Self):
        pass