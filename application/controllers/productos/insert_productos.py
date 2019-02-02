import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert_productos() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        codigo = formulario['codigo'] # alamcena el nombre escrito en el input
        nombre = formulario['nombre']
        marca = formulario['marca'] # almacena el email escrito en el input
        contenido = formulario['contenido']
        precio = formulario['precio']
        config.model_productos.insert_producto(codigo, nombre, marca, contenido, precio) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/productos') # redirecciona al index.html
