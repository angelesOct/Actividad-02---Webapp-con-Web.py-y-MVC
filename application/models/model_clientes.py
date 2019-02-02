import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_cliente(nombre):
    try:
        return db.select('clientes',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_cliente Error {}".format(e.args)
        print "Model select_cliente Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando los datos de las tablas
'''
def insert_cliente(nombre, edad, email, telefono, tipo):
    try:
        return db.insert('clientes', nombre=nombre,edad=edad,email=email,telefono=telefono,tipo=tipo) # inserta un registro en personas
    except Exception as e:
        print "Model insert_cliente Error {}".format(e.args)
        print "Model insert_cliente Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_cliente(nombre):
    try:
        return db.delete('clientes', where='nombre=$nombre',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_cliente Error {}".format(e.args)
        print "Model delete_cliente Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos, del nombre recibido
'''
def update_cliente(nombre, edad, email, telefono, tipo): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('clientes', 
            edad=edad,
            email=email, 
            telefono=telefono,
            tipo=tipo,
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_cliente Error {}".format(e.args)
        print "Model update_cliente Message {}".format(e.message)
        return None
