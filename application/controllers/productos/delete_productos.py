import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, codigo): 
        producto = config.model_productos.select_producto(codigo)# Selecciona el registro que coincida con nombre
        return config.render.delete_productos(producto) # Envia el registro y renderiza delete.html
    
    def POST(self, codigo):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        codigo = formulario['codigo'] # Obtine el nombre almacenado en el formulario
        config.model_productos.delete_producto(codigo) # Borra el registro del nombre seleccionado
        raise web.seeother('/productos') # Redirecciona a raiz
