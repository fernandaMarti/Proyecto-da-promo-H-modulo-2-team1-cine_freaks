def listarPeliculas(peliculas):
    
    print("Peliculas: ")
    
    
    for peli in peliculas:
      
        datos = "id registro {1} id pelicula: {2} titulo pelicula {3} tipo pelicula {4} genero pelicula {5} año estreno {6} mes estreno: {7}"
        print (datos.format(peli[1],peli[2],peli[3],peli[4],peli[5],peli[6],peli[7]))
       
    print(" ")   
            
