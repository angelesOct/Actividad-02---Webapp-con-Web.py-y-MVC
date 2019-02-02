import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, codigo): 
        producto = config.model_productos.select_producto(codigo) # Selecciona el registro que coincida con nombre
        return config.render.update_productos(producto) # Envia el registro y renderiza update.html
    
    def POST(self, nombre):
        formulario = web.input() # almacena los datos del formulario web
        codigo = formulario['codigo'] # alamcena el nombre escrito en el input
        nombre = formulario['nombre']
        marca = formulario['marca'] # almacena el email escrito en el input
        contenido = formulario['contenido']
        precio = formulario['precio']
        config.model_productos.update_producto(codigo, nombre, marca, contenido, precio) # actuliza los valores
        raise web.seeother('/productos') # redirecciona al index
