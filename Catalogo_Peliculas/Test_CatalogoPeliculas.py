from Catalogo_Peliculas.Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp  # renombramos para acortar el nombre con as

opcion = None

while opcion != 4:
    try:
        print('Opciones'.center(50, '-'))
        print('1. Agregar Pelicula')
        print('2. Listar Pelicula')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion: '))

        if opcion == 1:
            nombrePelicula = input('Proporcione el nombre de su pelicula: ')
            pelicula = Pelicula(nombrePelicula)
            cp.agregarPelicula(pelicula)
        elif opcion == 2:
            cp.listarPeliculas()
        elif opcion == 3:
            cp.eliminarPelicula()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del Programa...')
