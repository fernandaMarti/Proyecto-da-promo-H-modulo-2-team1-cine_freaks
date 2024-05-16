def listarPeliculas(peliculas):
    
    print("Peliculas: ")
    
    
    for peli in peliculas:
      
        datos = "tipo_pelicula: {0} titulo pelicula: {1} anno_estreno: {2} mes_estreno: {3} id_pelicula: {4} genero_pelicula: {5}"
        print (datos.format(peli[0],peli[1],peli[2],peli[3],peli[4],peli[5]))

    print(" ")   
            

def pedirDatosPelicula ():
    print("Introduzca los siguientes datos de la película")
    
    tipo_pelicula=input("Tipo de película:  ")
    titulo_pelicula=input("Iítulo de la pelicula:  ")
    anno_estreno=input("Año de estreno:  ")
    mes_estreno=input("Mes de estreno:  ")
    id_pelicula=input("Id de la película:  ")
    genero_pelicula=input("Género al que pertence la película:  ")
 
    
    pelicula = (tipo_pelicula, titulo_pelicula,anno_estreno,mes_estreno,id_pelicula,genero_pelicula)
    
    return pelicula



def pedirDatosPeliModificar(peliculas):
    listarPeliculas(peliculas)  

    codigoPeliEditar = input("Por favor, introduzca el id_pelicula de la pelicula a modificar: ")
    
    for peli in peliculas:
        if peli[4] == codigoPeliEditar:
            print("Introduzca los siguientes datos de la película")
            tipo_pelicula = input("Tipo de película: ")
            titulo_pelicula = input("Título de la película: ")
            anno_estreno = input("Año de estreno: ")
            mes_estreno = input("Mes de estreno: ")
            genero_pelicula = input("Género al que pertenece la película: ")
            
            return (tipo_pelicula, titulo_pelicula, anno_estreno, mes_estreno, codigoPeliEditar, genero_pelicula)

    print("La película con el id_pelicula {} no fue encontrada.".format(codigoPeliEditar))
    
    return ""

    

def pedirDatosPeliEliminar(peliculas):
    
    listarPeliculas(peliculas)
    
    existePeli=False

    codigoPeliEliminar = input ("Por favor, introduzca el codigo de la pelicula a eliminar:   ")
    
    for peli in peliculas:
        if peli[4] == codigoPeliEliminar:
            existePeli=True
            break
    if not existePeli:
        codigoPeliEliminar =""
    
    return codigoPeliEliminar        
    