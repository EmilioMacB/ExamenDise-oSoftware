from biblioteca_refactorizada_srp import SistemaBibliotecaSRP
from ejercicio03_intrerfaces import IRepositorio
from ejercicio2_srp import ValidadorBiblioteca, ServicioNotificaciones


class SistemaBibliotecaDIP(SistemaBibliotecaSRP):
    
    def __init__(
        self, 
        validador: ValidadorBiblioteca, 
        repositorio: IRepositorio, # el cambio importane
        notificador: ServicioNotificaciones
    ):
    
        super().__init__(validador, repositorio, notificador)