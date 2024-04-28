CREATE SCHEMA CinemExtract;
USE CinemExtract;

CREATE TABLE MoviesDataset (
id_registro INT AUTO_INCREMENT NOT NULL,
id_pelicula INT,
titulo_pelicula VARCHAR (100),
tipo_pelicula VARCHAR (45),
genero_pelicula VARCHAR (45),
anno_estreno VARCHAR(45),
mes_estreno VARCHAR (45),
PRIMARY KEY (id_registro)
);

CREATE TABLE premios (
id_premio INT AUTO_INCREMENT NOT NULL,
id_registro INT,
fecha_ceremonia DATE,
mejor_pelicula VARCHAR (255),
mejor_director VARCHAR (100),
mejor_actor VARCHAR (100),
mejor_actriz VARCHAR (100),
PRIMARY KEY (id_premio),
FOREIGN KEY (id_registro) REFERENCES MoviesDataset (id_registro)
);

CREATE TABLE actores (
nombre_actor VARCHAR (100),
anno_nacimiento VARCHAR (45),
conocido VARCHAR (45),
que_hace VARCHAR (45),
premios VARCHAR (45),
id_premio INT,
CONSTRAINT FK_premios FOREIGN KEY (id_premio) REFERENCES premios (id_premio)
);

CREATE TABLE detalles_peliculas (
id_detalle INT AUTO_INCREMENT NOT NULL,
id_registro INT,
nombre_pelicula VARCHAR (100),
argumento VARCHAR (2000),
duracion VARCHAR (45),
guionistas VARCHAR(255),
directores VARCHAR (255),
puntuacion_imdb VARCHAR (45),
puntuacion_rotten VARCHAR (45),
PRIMARY KEY (id_detalle),
FOREIGN KEY (id_registro) REFERENCES MoviesDataset (id_registro)
);

