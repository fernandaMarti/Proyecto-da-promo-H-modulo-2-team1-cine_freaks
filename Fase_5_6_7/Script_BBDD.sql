

CREATE SCHEMA CinemExtract;

USE CinemExtract;

--Tupla que viene del CSV (Tipo,Nombre,Anno_estreno,Mes_estreno,Id_peli,Genero)
  
CREATE TABLE MoviesDataset (
tipo_pelicula VARCHAR (45),
titulo_pelicula VARCHAR (100),
anno_estreno INT,
mes_estreno VARCHAR (45),
id_pelicula VARCHAR (20),
genero_pelicula VARCHAR (45),
PRIMARY KEY (id_pelicula)
);

--Tupla que viene del CSV (indice,Ceremonia,Mejor película,Mejor director,Mejor actor,Mejor actriz)

CREATE TABLE oscars (
id_ceremonia INT,
fecha_ceremonia INT,
mejor_pelicula VARCHAR (255),
mejor_director VARCHAR (100),
mejor_actor VARCHAR (100),
mejor_actriz VARCHAR (100),
PRIMARY KEY (id_ceremonia)
);

--Tupla que viene del CSV (indice, nombre_actor,anno_nacimineto, conocido,que_hace,premios)
  
CREATE TABLE actores (
id_actor INT AUTO_INCREMENT,
nombre_actor VARCHAR (100),
anno_nacimiento INT,
conocido VARCHAR (45),
que_hace VARCHAR (45),
premios INT,
PRIMARY KEY (id_actor)
);

--Tupla que viene del CSV (Id_peli,Punt_IMDB,Tomatometer,Direccion,Guionistas,Argumento,Duracion,Nombre)
  
CREATE TABLE detalles_peliculas (
id_detalle_peli INT AUTO_INCREMENT,
id_pelicula VARCHAR(20),
puntuacion_imdb VARCHAR (45),
puntuacion_rotten VARCHAR (45),
directores VARCHAR (255),
guionistas VARCHAR(255),
argumento VARCHAR (2000),
duracion VARCHAR (45),
nombre_pelicula VARCHAR (100),
PRIMARY KEY (id_detalle_peli),
FOREIGN KEY (id_pelicula) REFERENCES MoviesDataset (id_pelicula)
);

--Tabla inermedia para una relación de muchos a muchos.
  
CREATE TABLE int_pelis_actores (
id_actor INT,
id_pelicula VARCHAR(20),
PRIMARY KEY (id_actor,id_pelicula),
FOREIGN KEY (id_actor) REFERENCES actores (id_actor),
FOREIGN KEY (id_pelicula) REFERENCES MoviesDataset (id_pelicula)  
);
