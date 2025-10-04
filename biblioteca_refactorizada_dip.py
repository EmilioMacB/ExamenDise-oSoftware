from EXAMEN_SOLID_POO.ejercicio02.biblioteca_refactorizada_srp import SistemaBibliotecaSRP
from EXAMEN_SOLID_POO.ejercicio03.ejercicio03_intrerfaces import IRepositorio
from EXAMEN_SOLID_POO.ejercicio02.ejercicio2_srp import ValidadorBiblioteca, ServicioNotificaciones


class SistemaBibliotecaDIP(SistemaBibliotecaSRP):
    
    def __init__(
        self, 
        validador: ValidadorBiblioteca, 
        repositorio: IRepositorio, # el cambio importane
        notificador: ServicioNotificaciones
    ):
    
        super().__init__(validador, repositorio, notificador)