import  sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import urllib.request as request

""" Importamos todas nuetras Ventana y funciones utiles"""
from view.home import  *
from view.listado import  *
from view.recipes import  *
from view.form import *
from tool.tool import  *


class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)


        # Instaciamos nuestra ventanas widget home
        self.home = Ui_home()

        # Instaciamos nuestro widget listado
        self.listado = Ui_listado()
        self.recipes = ""

        #Agregamos nuestro wigget a la ventana
        self.home.setupUi(self)

        # Cargamos la data
        self.init_rec()

        # Eventos o Señales
        self.home.bt_list_rec.clicked.connect(self.ev_lista)

    def init_rec (self):
        """ Cargamos recetas  a  la pantalla home"""
        # Generamos un ramdom de nuestra informacion
        self.data = Random_recipes(load())
        fila = 0
        for x,dt in enumerate(self.data):
            print(x, " dta: ", dt)
            # Creamos un layout para contenido de las recetas
            ly = QVBoxLayout()
            # Asiganmos la imagen de la Receta
            img = self.add_img(dt['img_local'])
            # Asignamos el nombre de la Receta
            name = QLabel(dt['name'])
            # Asiganamos la fecha de publicacion
            publi = fecha(dt['created_at']['$date'])
            # Asiganamos el author
            pub = QLabel('<b>Publicado: ' + publi + '</b>')
            # agregamos los widget a nuestro layout
            ly.addWidget(img)
            ly.addWidget(name)
            ly.addWidget(pub)

            # Creamos un Widget Receta
            w =""
            w = QWidget()

            # Agreagamos el  Layout  a  widget
            w.setLayout(ly)

            # Asiganmos las columna y fila de cara receta
            if fila < 2:
                self.home.panel.addWidget(w, 0, fila)
            elif fila < 4:
                self.home.panel.addWidget(w, 1, fila-2)
            else:
                break
            # elif fila < 9:
            #     self.home.cont.addWidget(w, 2, fila - 6)
            # elif fila < 12:
            #     self.home.cont.addWidget(w, 3, fila - 9)
            fila += 1

    def add_img(self, url):
        """
        Encargada de Traer una imagen desde una  url  y la retorna como un label
        :param url:
        :return label:
        """
        try:
            # Buscamos nuestra imagenes
            # img = request.urlopen(url).read()
            #  img = '/home/maryito/_.Proyectos/Python/QT/app/img/1.jpg'
            #/home/maryito/_.Proyectos/Python/QT/RecipesPyQt
            img = '/home/maryito/_.Proyectos/Python/QT/RecipesPyQt/img/local/' + url
            # componente de imagen
            pixmap = QPixmap()
            # cargamos la imagen a qpixmap
            # pixmap.loadFromData(img)
            pixmap.load(img)
            # Creamos un label
            label = QLabel()
            # agregamos la imagen y le asignamos el tamaño a label
            label.setPixmap(pixmap.scaled(200, 150))

        except Exception as e:
            print("error ", str(e))

        return label

    def ev_lista (self):
        """ Evento encargado de cargar la ventana de lista de recetas"""
        # Creamos una nueva ventana
        self.home.statusbar.showMessage ("Por favor Espere Cargando lista de recetas...", 2000)
        self.ventana = QMainWindow()

        # Agregamos el widget a la ventana
        self.listado.setupUi(self.ventana)
        # traemos nuestra tableView y la asignamos
        table = self.listado.tb_list
        #Asiganmos el tamaño de la tabla
        size = len( self.data)
        table.setRowCount(size)

        # Recorremos nuestras recetas
        for ind,info in enumerate(self.data):

            # Agregamos la imagen a l row de la table
            table.setCellWidget(ind, 0,self.add_img(info['img_local']))
            # Agregamos el nombre
            table.setItem(ind, 1, QTableWidgetItem(info['name']))
            # Calculo de total del tiempo de preparacion de la receta
            time = int( info['preparation_time'] + info['cook_time'] )
            # convertidmo nuestra fecha en modo normal
            pub = fecha( info['created_at']['$date'] )
            # Agregamos el tiempo de la recepa
            table.setItem(ind, 2, QTableWidgetItem(hora(time)+ " h"))
            # table.setItem(ind, 2, QTableWidgetItem(str(time)+ " Minutos"))
            # Agregamos el author
            table.setItem(ind, 3, QTableWidgetItem(info['author']))
            # Agregamos la fecha de publicacion
            table.setItem(ind, 4, QTableWidgetItem(pub))

            # Asignamos el ancho de el row
            table.setRowHeight(ind, 200)

        # adaptamos el contenido de la recetas a la columna de nuestra tabla
        table.resizeColumnsToContents()

        # CREAMOS EL EVENTO O SEÑAL
        table.itemSelectionChanged.connect(self.ev_table)

        # Mostramos la ventana
        self.ventana.show()

    def ev_table (self):
        """
        Evento encargado de renderizar el item de  UI listado a la ventana de vista de receta
        :return:
        """

       # self.recipes = Ui_Form()
        items = self.listado.tb_list.selectedItems()
        nombre = items[0].text()

        self.show_recipes(nombre)

    def show_recipes (self, nombre):
        """
        Esta en cargado de cargar la informacion detallada de nuestra receta selecionada
        :param nombre:
        :return:
        """
        # Instacionmos nuestro UI recipes
        self.recipes = Ui_MainWindow()
        #Creamos una nueva ventana
        self.w = QMainWindow()

        #Buscamos el id de la receta con sus nombre
        id = find_id(nombre)
        # Buscamos la informacion de nuestra receta selecionada
        datos = find_id(nombre, id)
        # Configuramos nuestra UI con la ventana nueva
        self.recipes.setupUi(self.w)
        #Agregamos los iconos a nuestra UI
        icon = "/home/maryito/_.Proyectos/Python/QT/RecipesPyQt/img/clock2.png"
        icon2 = "/home/maryito/_.Proyectos/Python/QT/RecipesPyQt/img/pre.png"
        #Buscamos la imagen de nuestra receta
        img = "/home/maryito/_.Proyectos/Python/QT/RecipesPyQt/img/local/"+datos['img_local']

        pix = QPixmap()
        #Cargamos nuestras imagenes
        pix.load(icon)
        #Asignamos las imagenes
        self.recipes.icon1.setPixmap(pix)
        pix.load(icon2)
        self.recipes.icon2.setPixmap(pix)
        # damos formato al tiempo
        time =int(datos['preparation_time']+datos['cook_time'])
        # la cantidad de porciones
        prop = int(datos["servings"])

        #API
        # img = request.urlopen(datos['img']).read()
        # pix.loadFromData(img)
        # Cargamos y damos tamaño a la imagen
        pix.load(img)
        self.recipes.list_img.setPixmap(pix.scaled(400,200))
        # Asignamos el nombre de la receta
        self.recipes.titulo.setText(datos['name'])
        #Asignamos el tiempo total de la receta
        self.recipes.time.setText(hora(time)+ " h")
        #Asignamos la porporcion
        self.recipes.time_p.setText(str(prop)+ " Proporciones")

        #Recorremos todos los ingrdientes de la receta y lo agregando a nuestra lista
        for ind, data in enumerate(datos['ingredients']):
            info = str(ind+1)+") "+data['qty']+" "+data['name']
            item = QTreeWidgetItem([info])
            #Agragamos el item a la lista
            self.recipes.list_recteas.addTopLevelItem(item)
            #Nos permite que lista se adapte a la informacion del item
            self.recipes.list_recteas.resizeColumnToContents(ind)

        #verificacion si hay recetas sin instruciones
        if len(datos['instructions']) is 0:
            item = QTreeWidgetItem(["No hay Instruciones Disponible.."])
            self.recipes.list_instruc.addTopLevelItem(item)
        else:
            #Recorremos todos lo pasos para la preparacion de la receta
            for ind, data in enumerate(datos['instructions']):
                paso = "Paso #"+ str ( int ( data['id']))
                info = data['detail']

                item = QTreeWidgetItem([paso])
                item2 = QTreeWidgetItem([info])

                self.recipes.list_instruc.addTopLevelItem(item)
                self.recipes.list_instruc.addTopLevelItem(item2)

                self.recipes.list_instruc.resizeColumnToContents(ind)
        #Mostramos nuestra receta con toda la informacion
        self.w.show()

def iniciar():
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)

    # Instaciomos nuestro ventana
    ventana = Main()
    # Mostramos nuestra app
    ventana.show()

    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
