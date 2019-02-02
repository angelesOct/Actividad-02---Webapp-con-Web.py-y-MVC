import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, codigo):  
        producto = config.model_productos.select_producto(codigo) # Selecciona el registro que coincida con nombre
        return config.render.view_productos(producto) # Envia el registro y renderiza view.html
