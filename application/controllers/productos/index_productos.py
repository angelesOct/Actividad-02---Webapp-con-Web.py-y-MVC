import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        producto = config.model_productos.select_productos().list() # Selecciona todos los registros de personas
        return config.render.index_productos(producto) # Envia todos los registros y renderiza index.html
   