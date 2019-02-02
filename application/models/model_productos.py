import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el codigo dado
'''
def select_producto(codigo):
    try:
        return db.select('productos',where='codigo=$codigo', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_producto Error {}".format(e.args)
        print "Model select_producto Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando los datos de las tablas
'''
def insert_producto(codigo, nombre, marca, contenido, precio):
    try:
        return db.insert('productos', codigo=codigo,nombre=nombre,marca=marca,contenido=contenido,precio=precio) # inserta un registro en personas
    except Exception as e:
        print "Model insert_producto Error {}".format(e.args)
        print "Model insert_producto Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el codigo recibido
'''
def delete_producto(codigo):
    try:
        return db.delete('productos', where='codigo=$codigo',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_producto Error {}".format(e.args)
        print "Model delete_producto Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos, del codigo recibido
'''
def update_producto(codigo, nombre, marca, contenido, precio): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('productos', 
            nombre=nombre,
            marca=marca,
            contenido=contenido,
            precio=precio,
            where='codigo=$codigo',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}".format(e.args)
        print "Model update_producto Message {}".format(e.message)
        return None
