
![BBDD (1)](https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/e306731c-ed44-4e7b-8592-93a6639e89f1)


<img width="158" alt="Titulo1tablas" src="https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/ce910868-b8d8-473b-9edb-6ecaf1b0331f"></br>
</br>

### MoviesDataset

id_pelicula VARCHAR(15) PK
titulo_pelicula VARCHAR (100)
tipo_pelicula VARCHAR (45)
genero_pelicula VARCHAR (45)
anno_estreno VARCHAR(45)
mes_estreno VARCHAR (45)

### Oscars

id_oscar INT PK
genero_pelicula VARCHAR (45)
fecha_ceremonia DATE
mejor_pelicula VARCHAR (255)
mejor_director VARCHAR (100)
mejor_actor VARCHAR (100)
mejor_actriz VARCHAR (100)

### Actores

id_actor INT PK
nombre_actor VARCHAR (100)
anno_nacimiento INT
conocido VARCHAR (45)
que_hace VARCHAR (45)
premios INT

## Detalles Pelicula

id_detalle INT PK
id_pelicula VARCHAR(15) FK
nombre_pelicula VARCHAR (100)
argumento VARCHAR (2000)
duracion VARCHAR (45)
guionistas VARCHAR(255)
directores VARCHAR (255)
puntuacion_imdb VARCHAR (45)
puntuacion_rotten VARCHAR (45)




</br>
</br>
<img width="141" alt="tituloesquema" src="https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/62805399-ecaf-4d19-a50f-7bbb4c8814b9">
