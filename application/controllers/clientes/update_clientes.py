import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        cliente = config.model_clientes.select_cliente(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update_clientes(cliente) # Envia el registro y renderiza update.html
    
    def POST(self, email):
        formulario = web.input() # almacena los datos del formulario web
        nombre = formulario['nombre'] # alamcena el nombre escrito en el input
        edad = formulario['edad']
        email = formulario['email'] # almacena el email escrito en el input
        telefono = formulario['telefono']
        tipo = formulario['tipo']
        config.model_clientes.update_cliente(nombre, edad, email, telefono, tipo) # actuliza los valores
        raise web.seeother('/clientes') # redirecciona al index
