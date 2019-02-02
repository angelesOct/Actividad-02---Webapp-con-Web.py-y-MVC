import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre): 
        cliente = config.model_clientes.select_cliente(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete_clientes(cliente) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre = formulario['nombre'] # Obtine el nombre almacenado en el formulario
        config.model_clientes.delete_cliente(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/clientes') # Redirecciona a raiz