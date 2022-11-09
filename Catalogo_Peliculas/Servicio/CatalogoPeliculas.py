import os


class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, Pelicula):
        with open(cls.rutaArchivo, 'a', encoding='UTF8') as archivo:
            archivo.write(f'{Pelicula.nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.rutaArchivo, 'r', encoding='UTF8') as archivo:
            print('Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminarPelicula(cls):
        os.remove(cls.rutaArchivo)
        print(f'Archivo eliminado: {cls.rutaArchivo}')
