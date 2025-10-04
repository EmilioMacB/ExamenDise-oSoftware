from datetime import datetime
from biblioteca_examen import Libro, Prestamo
from EXAMEN_SOLID_POO.ejercicio02.ejercicio2_srp import ValidadorBiblioteca, RepositorioBiblioteca, ServicioNotificaciones


class SistemaBibliotecaSRP:
    def __init__(self, validador: ValidadorBiblioteca, repositorio: RepositorioBiblioteca, notificador: ServicioNotificaciones):
        
        self.validador = validador
        self.repositorio = repositorio
        self.notificador = notificador        
        
        self.libros = []
        self.prestamos = []
        self.contador_libro = 1
        self.contador_prestamo = 1

    def agregar_libro(self, titulo: str, autor: str, isbn: str):
        self.validador.validar_libro(titulo, autor, isbn)
        libro = Libro(self.contador_libro, titulo, autor, isbn)
        self.libros.append(libro)
        self.contador_libro += 1
        self.repositorio.guardar(self.libros, self.prestamos)
        return f"Libro '{titulo}' agregado exitosamente"
    
    def realizar_prestamo(self, libro_id: int, usuario: str):
        self.validador.validar_usuario(usuario)
        libro = None
        for l in self.libros:
            if l.id == libro_id:
                libro = l
                break
        if not libro:
            return "Error: Libro no encontrado"
        if not libro.disponible:
            return "Error: Libro no disponible"
        
        prestamo = Prestamo(
            self.contador_prestamo,
            libro_id,
            usuario,
            datetime.now().strftime("%Y-%m-%d")
        )

        self.prestamos.append(prestamo)
        self.contador_prestamo += 1
        libro.disponible = False
        

        self.repositorio.guardar(self.libros, self.prestamos)
        self.notificador.enviar_notificacion(usuario, libro)
        return f"Préstamo realizado a {usuario}"

    def devolver_libro(self, prestamo_id: int):
        prestamo = None
        for p in self.prestamos:
            if p.id == prestamo_id:
                prestamo = p
                break
        
        if not prestamo:
            return "Error: Préstamo no encontrado"
        
        if prestamo.devuelto:
            return "Error: Libro ya devuelto"
        
        for libro in self.libros:
            if libro.id == prestamo.libro_id:
                libro.disponible = True
                break
        
        prestamo.devuelto = True
        self._guardar_en_archivo()
        
        return "Libro devuelto exitosamente"
    
    def obtener_todos_libros(self):
        return self.libros

    def obtener_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def obtener_prestamos_activos(self):
        return [p for p in self.prestamos if not p.devuelto]
