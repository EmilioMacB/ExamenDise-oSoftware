from biblioteca_examen import Libro

class ValidadorBiblioteca: #solo valida los datos de entrada

    def validar_libro(self, titulo, autor, isbn):
        if not titulo or len(titulo) < 2:
            return "Error: Título inválido"
        if not autor or len(autor) < 3:
            return "Error: Autor inválido"
        if not isbn or len(isbn) < 10:
            return "Error: ISBN inválido"
        return None
    
    def validar_usuario(self, usuario):
        if not usuario or len(usuario) < 3:
            return "Error: Nombre de usuario inválido"
        return None
    
class RepositorioBiblioteca: #solo maneja la persistencia de datos (guardar y cargar)
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo

    def guardar(self, libros, prestamos):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")
        print("Datos guardados en el archivo.")


class ServicioNotificaciones: #solo maneja las notificaciones
    def enviar_notificacion(self, usuario, libro):
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")