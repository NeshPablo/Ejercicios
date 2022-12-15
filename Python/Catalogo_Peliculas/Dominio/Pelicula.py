class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self.nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __enter__(self):
        self.nombre = open(self.nombre, 'r', encoding='UTF8')
        return self.nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.nombre:
            self.nombre.close()
