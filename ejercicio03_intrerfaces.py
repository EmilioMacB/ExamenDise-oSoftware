from abc import ABC, abstractmethod

class IRepositorio(ABC): #contrato a seguir
    @abstractmethod
    def guardar(self, libros, prestamos): 
        pass


    @abstractmethod
    def cargar(Self):
        pass