#importacion de libreria
from flask import Flask,render_template
#creacionde objeto  de tipo  flask
app = Flask(__name__)
#creacion de ruta raiz a la pagina primcipall
@app.route ("/")
#creacion de funcion para llamar al inedex (pagina principal)
def index():

        return render_template("index.html")
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

        print(fHi, [name])
#configuracion de un archivo principal de ejecucion
if __name__ == '__main__':
#configuracion del puerto de escucha del servidor web
        app.run(port=80,debug= True)
