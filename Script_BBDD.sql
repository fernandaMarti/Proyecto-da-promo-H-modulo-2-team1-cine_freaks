

CREATE SCHEMA CinemExtract;

USE CinemExtract;

CREATE TABLE MoviesDataset (
id_pelicula INT NOT NULL,
titulo_pelicula VARCHAR (100),
tipo_pelicula VARCHAR (45),
genero_pelicula VARCHAR (45),
anno_estreno INT,
mes_estreno VARCHAR (45),
PRIMARY KEY (id_pelicula)
);

CREATE TABLE oscars (
id_ceremonia INT NOT NULL,
genero_pelicula VARCHAR (45),
fecha_ceremonia INT,
mejor_pelicula VARCHAR (255),
mejor_director VARCHAR (100),
mejor_actor VARCHAR (100),
mejor_actriz VARCHAR (100),
PRIMARY KEY (id_ceremonia)
);

CREATE TABLE actores (
id_actor INT NOT NULL,
nombre_actor VARCHAR (100),
anno_nacimiento INT,
conocido VARCHAR (45),
que_hace VARCHAR (45),
premios INT
PRIMARY KEY (id_actor)
);

CREATE TABLE detalles_peliculas (
id_detalle_peli INT NOT NULL,
id_pelicula VARCHAR(20)
nombre_pelicula VARCHAR (100),
genero_pelicula VARCHAR (45),
argumento VARCHAR (2000),
duracion VARCHAR (45),
guionistas VARCHAR(255),
directores VARCHAR (255),
puntuacion_imdb VARCHAR (45),
puntuacion_rotten VARCHAR (45),
PRIMARY KEY (id_detalle_peli),
FOREIGN KEY (id_pelicula) REFERENCES MoviesDataset (id_pelicula)
);

CREATE TABLE int_pelis_actores (
id_actor INT
id_pelicula VAARCHAR(20)
PRIMARY KEY (id_actor,id_pelicula),
FOREIGN KEY (id_actor) REFERENCES actores (id_actor),
FOREIGN KEY (id_pelicula ) REFERENCES MoviesDataset (id_pelicula)  
);




  
