
from Conexion.conexion import DAO
from Conexion.conexion import API
import opciones
from mysql.connector.errors import Error

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
            print("5. Crear BBDD")
            print("6. Consultas SQL")
            print("7. Cargar Peliculas API")
            print("8. Salir")
            
            opcion= int(input("Elige una opción:  "))
            
            if opcion <1 or opcion >8:
                 print("La opción introducida no esta disponible")
            
            elif opcion ==8:
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
                print ("No se encontraron peliculas")      
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
        nombre= input("Introduce el nombre de la base de datos a crear:  ")
        dao.crear_BBDD(nombre)
    
    elif opcion==6:
       
        print("CONSULTAS SQL")
        print("")
        print('1. ¿Qué géneros han recibido más premios Óscar?')
        print('2. ¿Qué género es el mejor valorado en IMDB?')
        print('3. ¿En que año se estrenaron más películas?')
        print('4. ¿En que año se estrenaron mas cortos?')
        print('5. ¿Cuál es la mejor serie valorada en IMDB?')
        print('6. ¿Cuál es la película mejor valorada en IMDB?')
        print('7. ¿Qué actor/actriz ha recibido más premios?')
        print('8. ¿Hay algun actor/actriz que haya recibido más de un premio Óscar?')
        print('9. Volver al menú')
        print("")
       
        
        consulta= input("Elige una consulta a realizar:")
            
        if consulta ==1:
            pass
            
        elif consulta==2:
            pass
        elif consulta==3:
            pass
        elif consulta==4:
            pass
        elif consulta==5:
            pass
        elif consulta==6:
            pass
        elif consulta==7:
            pass
        elif consulta==8:
            pass
            
        else:
            menuPrincipal()
       
   
    elif opcion ==7:
       
       continuar =True
       while continuar:
           
        url = "https://moviesdatabase.p.rapidapi.com/titles"
       
        try:
           
            titleType= input("¿Que fichero quieres generar [movie/short]?  ")
            genere = input ("¿Que género listamos? [Drama,Action,Comedy]?  ")
           
            dic_API_Pelis= API.llamar_API(url,titleType,genere)
            
            # Llamar a funcion para que lo pase a csv
            
            
            #llamar a funcion que lo meta en la base de datos
        
        except Error as err:
            
            print ("Ocurrio un error al intentar ejcutar la API".format(err))
        
        respuesta= input("¿Quieres cargar más peliculas s/n?")
        if respuesta == 'n':
            continuar =False
    
    elif opcion ==8:
        quit
    else:
        pass

menuPrincipal()

