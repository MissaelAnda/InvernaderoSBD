CREATE DATABASE invernadero;

USE invernadero;

CREATE TABLE dueno(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellidos VARCHAR (50)
);

CREATE TABLE invernadero(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(50) NOT NULL,
    id_dueno INT,
    FOREIGN KEY(id_dueno)
    REFERENCES dueno(id)
);

CREATE TABLE clasificacion(
    id INT PRIMARY KEY AUTO_INCREMENT,
    clasificacion VARCHAR(30) NOT NULL
);

CREATE TABLE planta(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cultivo VARCHAR(30) NOT NULL,
    fecha DATE NOT NULL,
    id_clasif INT,
    id_inv    INT,
    FOREIGN KEY(id_clasif)
    REFERENCES clasificacion(id),
    FOREIGN KEY(id_inv)
    REFERENCES invernadero(id)
);

CREATE TABLE registro(
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    ph FLOAT,
    luz FLOAT,
    humedad FLOAT,
    co2 FLOAT,
    id_planta INT,
    FOREIGN KEY(id_planta)
    REFERENCES planta(id)
);

CREATE TABLE usuario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(128) NOT NULL,
    password VARCHAR(64) NOT NULL,
    tipo INT NOT NULL
);

CREATE TABLE usuarioinvernadero(
    id_usuario INT,
    id_inv     INT,
    FOREIGN KEY(id_usuario)
    REFERENCES usuario(id),
    FOREIGN KEY(id_inv)
    REFERENCES invernadero(id)
);
