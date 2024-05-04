def listarPeliculas(peliculas):
    
    print("Peliculas: ")
    
    
    for peli in peliculas:
      
        datos = "id registro: {0} id pelicula: {1} titulo pelicula {2} tipo pelicula {3} genero pelicula {4} año estreno {5} mes estreno: {6}"
        print (datos.format(peli[0],peli[1],peli[2],peli[3],peli[4],peli[5],peli[6]))
       
    print(" ")   
            

def pedirDatosPelicula ():
    print("Introduzca los siguientes datos de la película")
    id_pelicula=int(input("Codigo de película:  "))
    titulo_pelicula=input("Iítulo de la pelicula:  ")
    tipo_pelicula=input("Tipo de película:  ")
    genero_pelicula=input("Género al que pertence la película:  ")
    anno_estreno=input("Año de estreno:  ")
    mes_estreno=input("Mes de estreno:  ")
    
    pelicula = (id_pelicula,titulo_pelicula,tipo_pelicula,genero_pelicula,anno_estreno,mes_estreno)
    
    return pelicula



def pedirDatosPeliModificar(peliculas):
    
    listarPeliculas(peliculas)
    
    codigoPeliEditar = int(input ("Por favor, introduzca el codigo de la peli a modificar   "))
    
    for peli in peliculas:
        if peli[0] == codigoPeliEditar:
            existePeli=True
            break
    if existePeli:
        print("Introduzca los siguientes datos de la película")
        id_pelicula=codigoPeliEditar
        titulo_pelicula=input("Iítulo de la pelicula:  ")
        tipo_pelicula=input("Tipo de película:  ")
        genero_pelicula=input("Género al que pertence la película:  ")
        anno_estreno=input("Año de estreno:  ")
        mes_estreno=input("Mes de estreno:  ")
    
        pelicula = (id_pelicula,titulo_pelicula,tipo_pelicula,genero_pelicula,anno_estreno,mes_estreno)
    else:
        curso = None
        
    return pelicula
    

def pedirDatosPeliEliminar(peliculas):
    
    listarPeliculas(peliculas)

    codigoPeliEliminar = int(input ("Por favor, introduzca el codigo de la peli a eliminar:   "))
    
    for peli in peliculas:
        if peli[0] == codigoPeliEliminar:
            existePeli=True
            break
    if not existePeli:
        codigoPeliEliminar =""
    
    return codigoPeliEliminar        
    