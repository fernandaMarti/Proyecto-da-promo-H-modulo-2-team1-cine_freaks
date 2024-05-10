
![BBDD (1)](https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/e306731c-ed44-4e7b-8592-93a6639e89f1)


<img width="158" alt="Titulo1tablas" src="https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/ce910868-b8d8-473b-9edb-6ecaf1b0331f"></br>
</br>

### MoviesDataset

  id_pelicula VARCHAR(15) PK </br>
  titulo_pelicula VARCHAR (100) </br>
  tipo_pelicula VARCHAR (45) </br>
  genero_pelicula VARCHAR (45) </br>
  anno_estreno VARCHAR(45) </br>
  mes_estreno VARCHAR (45) </br>

### Oscars

  id_oscar INT PK </br>
  genero_pelicula VARCHAR (45) </br>
  fecha_ceremonia INT </br>
  mejor_pelicula VARCHAR (255) </br>
  mejor_director VARCHAR (100) </br>
  mejor_actor VARCHAR (100) </br>
  mejor_actriz VARCHAR (100) </br>

### Actores

  id_actor INT PK </br>
  nombre_actor VARCHAR (100) </br>
  anno_nacimiento INT </br>
  conocido VARCHAR (45) </br>
  que_hace VARCHAR (45) </br>
  premios INT </br>

## Detalles Pelicula

  id_detalle INT PK </br>
  id_pelicula VARCHAR(15) FK </br>
  nombre_pelicula VARCHAR (100) </br>
  argumento VARCHAR (2000) </br>
  duracion VARCHAR (45) </br>
  guionistas VARCHAR(255) </br>
  directores VARCHAR (255) </br>
  puntuacion_imdb VARCHAR (45) </br>
  puntuacion_rotten VARCHAR (45) </br>




</br>
</br>
<img width="141" alt="tituloesquema" src="https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/62805399-ecaf-4d19-a50f-7bbb4c8814b9">
</br>
</br>

<img width="499" alt="tablas_esquema" src="https://github.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/assets/99440874/6c1ed3a3-8959-44c7-a3e9-3bde585332c9">




