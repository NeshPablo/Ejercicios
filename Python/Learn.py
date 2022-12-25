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
# from functools import reduce

# numeros = (3, 2, 6, 7)

# def suma(x, y):
#     return x + y

# sumar = reduce(suma, numeros)
# print(f'Resultado: {sumar}')

""" Patrones de busqueda en python
    con la libreria re
    que nos facilita la busqueda de caracteres en nustro programa
"""
# import re
#1
# print(re.search(r'\d\d\d', 'askas566skals'))

#2
# patron = re.compile('\d\d\d')
# print(patron.search('jols462saas').group())

#3
# if(re.search('\Aa[0-9].*(end|fin)$', 'a4 es una marca de fin')):
#     print('Se encontro el patron')

#4 Esta funcion es con la funcion sub que sustituye el valor por un caracter especificado
# print(re.sub(r'\d', '*', 'mpang8uera990',2))

#5 modificadores en python nos facilita ya que lo detecta sin importar que sea mayuscula o minuscula el caracter
# regex = re.compile(r'ab', re.IGNORECASE)
# print(regex.search('jutnkmilajAbui'))

""" Leer archivos XML en python 

from xml.dom.minidom import parse, Node 
xmltree = parse('')

for nodo in xmltree.getElementsByTagName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print(nodo_hijo.data)
"""
# import xml.sax
# from xml.etree.cElementTree import parse

# xml_doc = parse('')
# for ele in xml_doc.findall('pro')
#     print(ele.text)

""" Abrir datos de tipo json en python
    Con el fin de aprender a abrir diferentes tipos de archivos

"""
# import json

# with open('') as file:
#     data = json.load(file)

# print(data)
""" Enviar un correo electronico con python el cual es necesario tener una cuenta 
    este solo es un ejemplo ya que si necesitamos que funcione es necesario agregar una cuenta 
    y ns pida permisos para poder enviar un mensaje 
"""

# import smtplib

# from email.mime.text import MIMEText
# smg = MIMEText('Contenido de correo')

# smg['subject'] = 'Asunto del correo'
# smg['From'] = 'Desdedonde@sjssk.com'
# smg['To'] = 'Haciadonde@ajsjs.com'
 
# mailServer = smtplib.SMTP('smt.gmail.com', 587)
# mailServer.ehlo()
# mailServer.starttls()
# mailServer.ehlo()
# mailServer.login('neshss008222@mail.com', 'xxxzxaaxxxxx')
# mailServer.sendmail('sasasas@mail.com', 'sjjjjsjsjsjs@mail.com', msf_as_string())
# mailServer.close

"""Calcular area de un cuadrado con una clase
    o def
"""
# def CalcularPerimetro(lado):
#     area = lado * lado
#     return area

# area_c = CalcularPerimetro(5)
# print(area_c)

""" Recibir varios tipos de datos para poder calcular varios datos 
    utilizando *args ya que nos permite recibir varios tipos de datos
    sin tener que poner varios datos en la funcion
"""

# def calcularPerimetro(*args):
#     perimetro = 0
#     for lado in args:
#         perimetro += lado
#     return perimetro

# permetro = calcularPerimetro(1,2,3,4)
# print(permetro)

""" En este ejercicio utilizaremos en parametro **kwargs
    en donde nos acepta poner datos sin poner el nombre del 
    parametro y nos lo acepta dando un valor como un diccionario
"""
def funcionKwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f'llave: {llave}, valor: {valor}')
    print(kwargs['nombre'], kwargs['apellido'])

funcionKwargs(nombre='Nesho', apellido='Pablo')

llave = 'a' 




















































