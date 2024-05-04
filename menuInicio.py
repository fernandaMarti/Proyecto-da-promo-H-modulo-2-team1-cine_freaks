
from Conexion.conexion import DAO
import opciones
from mysql.connector import Error

#Vamos a hacer un Crud con Python

def menuPrincipal():
    
    continuar =True
    while continuar:
        opcionCorrecta =False
        
        while not opcionCorrecta:
            
            print("===========================    Menú    ==============================")
            print("1. Ver peliculas")
            print("2. Alta Pelicula")
            print("3. Editar Pelicula")
            print("4. Eliminar Pelicula")
            print("5. Salir")
            
            opcion= int(input("Elige una opción"))
            
            if opcion <1 or opcion >5:
                 print("La opción introducida no esta disponible")
            
            elif opcion ==5:
                continuar=False
                print ("Muchas gracias por utilizar nuestra aplicacion")
                break
            else:
                opcionCorrecta=True
                llamarOpcionCorrecta(opcion)
                
def llamarOpcionCorrecta(opcion):
    dao = DAO ()
    if opcion ==1:
        try:
            peliculas=dao.listaPeliculas()
            
            if len(peliculas) >0:
                opciones.listarPeliculas(peliculas)
            else:
                print ("No se encontraron cursos")      
        except:
            print ("Ocurrio un error en opcion 1")    
        
    elif opcion ==2:
        pelicula =opciones.pedirDatosPelicula()
        
        try:
            dao.altaPelicula(pelicula)
        except Error as err:
            print ("Ocurrio un error al dar de alta la pelicula {0}".format(err))
        
    elif opcion ==3:
        try:
            peliculas=dao.listaPeliculas()
            if len(peliculas) >0:
                pelicula = opciones.pedirDatosPeliModificar(peliculas)
                if pelicula:
                    dao.actualizarPelicula(pelicula)
                else:
                    print ("Codigo de película no encontrado")            
            else:
                print ("No se encontraron peliculas")     
        except Error as err:
            
            print ("Ocurrio un error al intentar eliminar la pelicula {0}".format(err))
        
        
        
        
    elif opcion ==4:
        try:
            peliculas=dao.listaPeliculas()
            if len(peliculas) >0:
                codigoPeliEliminar = opciones.pedirDatosPeliEliminar(peliculas)
                if not (codigoPeliEliminar == ""):
                    dao.eliminarPelicula(codigoPeliEliminar)
                else:
                    print ("Codigo de película no encontrado")            
            else:
                print ("No se encontraron peliculas")     
        except Error as err:
            
            print ("Ocurrio un error al intentar eliminar la pelicula {0}".format(err))
        
    elif opcion ==5:
        quit
    else:
        pass

menuPrincipal()

