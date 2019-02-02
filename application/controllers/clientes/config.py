import web # importa la libreria web.py
import application.models.model_clientes as model_clientes # importa el modelo_personas 


render = web.template.render('application/views/clientes/','application/views/', base='master') # configura la ubicacion de las vistas