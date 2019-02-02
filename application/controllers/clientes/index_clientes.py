import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        cliente = config.model_clientes.select_clientes().list() # Selecciona todos los registros de personas
        return config.render.index_clientes(cliente) # Envia todos los registros y renderiza index.html
   