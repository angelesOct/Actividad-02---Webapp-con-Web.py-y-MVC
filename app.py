import web
        
urls = (
    '/','application.controllers.clientes.home.Home',
    '/clientes', 'application.controllers.clientes.index_clientes.Index',
    '/insert_clientes', 'application.controllers.clientes.insert_clientes.Insert',
    '/update_clientes/(.*)', 'application.controllers.clientes.update_clientes.Update',
    '/delete_clientes/(.*)', 'application.controllers.clientes.delete_clientes.Delete',
    '/view_clientes/(.*)', 'application.controllers.clientes.view_clientes.View',
    '/productos', 'application.controllers.productos.index_productos.Index',
    '/insert_productos', 'application.controllers.productos.insert_productos.Insert',
    '/update_productos/(.*)', 'application.controllers.productos.update_productos.Update',
    '/delete_productos/(.*)', 'application.controllers.productos.delete_productos.Delete',
    '/view_productos/(.*)', 'application.controllers.productos.view_productos.View',
)


if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()