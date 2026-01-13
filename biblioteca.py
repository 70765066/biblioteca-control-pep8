"""
Módulo que define las clases Biblioteca y Book para la gestión de inventario.
"""

class Biblioteca:
    """
    Representa una biblioteca que almacena una colección de libros.
    """
    def __init__(self, name):
        self.name = name
        self.libros = []

    def addb(self, book):
        """Agrega un objeto Book a la lista de libros de la biblioteca."""
        self.libros.append(book)

    def show(self):
        """Muestra en consola la información básica de todos los libros."""
        for libro in self.libros:
            print(libro.titulo, libro.autor, libro.indice)


class Book:
    """
    Representa un libro individual con atributos de autor, título y estado.
    """
    def __init__(self, titulo, autor, indice):
        self.titulo = titulo
        self.autor = autor
        self.indice = indice
        self.exist = True

    def lend(self):
        """
        Cambia el estado del libro a no disponible si está presente.
        Retorna True si el préstamo fue exitoso, False de lo contrario.
        """
        if self.exist:
            self.exist = False
            return True
        return False

    def back(self):
        """Establece el estado del libro como disponible (exist = True)."""
        self.exist = True