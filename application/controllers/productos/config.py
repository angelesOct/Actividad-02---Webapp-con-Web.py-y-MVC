import web # importa la libreria web.py
import application.models.model_productos as model_productos # importa el modelo_personas 


render = web.template.render('application/views/productos/','application/views/', base='master') # configura la ubicacion de las vistas