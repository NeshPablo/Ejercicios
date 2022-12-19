""" Hilos en python que significa un proceso en python esto sirve 
    para poder ver como se trabaja con varios datos a la vez con el 
    fin de ver cuando de ejecuta y cuando empieza a terminar cada dato o funcion
"""

# import threading
# import time

# class MiHilo(threading.Thread):
#     def run(self):
#         print("{} inicio".format(self.getName()))
#         time.sleep(1)
#         print('{} terminado'.format(self.getName()))


# if __name__=='__main__':
#     for x in range(4):
#         hilo = MiHilo(name='Thread - {}'.format(x+1))
#         hilo.start()
#         time.sleep(.1)

""" Programa que pasa las letras mayuscualas a minusculas 
    que se le envian 
"""
# def lower(elementos):
#     return elementos.lower()

# lista = ['Nesh', 'PABlo', 'AgUIrre']

# print(list(map(lower,lista)))
# print([cad.lower() for cad in lista])

""" Funciones de orden superior
    En donde se especifica el idioma y dependiendo de uq eingresemos nos 
    mostrara el saludo en ingles o español
"""
# def saludo(idioma):
#     def saludo_es():
#         print('Hola')

#     def saludo_en():
#         print('HI')

#     idioma_func = {'es':saludo_es, 'en': saludo_en}

#     return idioma_func[idioma]

# saludar = saludo('es')
# saludar()

""" Libreria reduce para hacer funciones 
    esto con el fin de aprender a ver como es la programacion funcional
"""
from functools import reduce

numeros = (3, 2, 6, 7)

def suma(x, y):
    return x + y

sumar = reduce(suma, numeros)
print(f'Resultado: {sumar}')

""" 
"""


















































