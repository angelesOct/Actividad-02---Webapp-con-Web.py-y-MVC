import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert_clientes() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # alamcena el nombre escrito en el input
        edad = formulario['edad']
        email = formulario['email'] # almacena el email escrito en el input
        telefono = formulario['telefono']
        tipo = formulario['tipo']
        config.model_clientes.insert_cliente(nombre, edad, email, telefono, tipo) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/clientes') # redirecciona al index.html
