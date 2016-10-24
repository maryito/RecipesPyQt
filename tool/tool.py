""" FUNCIONES  UTILES """
import  json
import  sys
from datetime import timedelta

import  dateutil.parser as parser
import  random

global data
def load():
    """
    Esta funcion nos permite traer nuestra data en formato json y nos la da ya serializamos
    :return data:
    """
    with open('/home/maryito/_.Proyectos/Python/QT/RecipesPyQt/tool/Data_Recipes.json')  as data_file:
        global data
        data =  json.load(data_file)

        # print(
        #     "Receta: ",data['name'],
        #     "author: ",data['author'],
        #     "cantidad de ing: ", len(data['ingredients'])
        # )
        # for i, d in enumerate(data['ingredients']):
        #     print(i+1, " ", d['qty']+" "+d['name'])

        # for i,datos in enumerate(data):
        #     print(i,datos)
        return  data

def hora (min):
    """
    Esta funcion nos permite convertir los minutos en horas en un formato HH:MM:SS
    :param min:
    :return:
    """
    return str(timedelta(minutes=min))

def Random_recipes(lista):
    """
    Esta Funcion nos permite Generar un rando de nuestra lista de receta
    :param lista:
    :return:
    """
    random.shuffle(lista)
    return lista
def fecha (fecha):
   """
   Esta funcion nos permite convertir la fecha de formato ISO a fecha normal
   :param fecha:
   :return:
   """
   fecha = (parser.parse(fecha))
   fh = fecha.strftime("%d/%m/%Y %I:%M%p")
   return fh

def find_id(nombre, id =None):
    """
    Esta funcion se encarga de buscar tanto id con los datos del una receta
    :param nombre:
    :param id:
    :return:
    """
    global data

    if id:
        for datos in data:
            if nombre in datos['name']:
                return datos
    else:
        for datos in data:
            if nombre in datos['name']:
                return datos['_id']['$oid']
