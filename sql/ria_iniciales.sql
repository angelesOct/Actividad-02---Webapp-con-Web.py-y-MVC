CREATE DATABASE ria_iniciales;

USE ria_iniciales;

CREATE TABLE clientes(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    edad varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    telefono varchar(50) NOT NULL,
    tipo varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos(
    codigo varchar(50) NOT NULL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    marca varchar(50) NOT NULL,
    contenido varchar(50) NOT NULL,
    precio varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


insert into clientes values
    ('Estefania Garcia','20','fanny@gmail','775542305','general'),
    ('Alexis oso','19','alexisOso@email.com','7751200148','preferido'),
    ('Mario','20','mario@alberto.edu.mx','775845392','frecuente');

insert into productos values
    ('745120369810','juguito','boing','500ml','15'),
    ('140257896542','papas','sabritas','60gr','10'),
    ('589423005585','paleta','cupido','2gr','1');

SHOW TABLES;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
