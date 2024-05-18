from conexion import DAO
from conexion import API
import opciones as opciones
from mysql.connector.errors import Error
import os

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
            print("6. Crear las Tablas")
            print("7. Cargar Peliculas API")
            print("8. Consultas SQL")
            print("9. Salir")
            
            opcion= int(input("Elige una opción:  "))
            
            if opcion <1 or opcion >9:
                 print("La opción introducida no esta disponible")
            
            elif opcion ==9:
                continuar=False
                print ("Muchas gracias por utilizar nuestra aplicacion")
                break
            else:
                opcionCorrecta=True
                llamarOpcionCorrecta(opcion)
                
def llamarOpcionCorrecta(opcion):
    dao = DAO ()
    api = API()
    if opcion == 1:
        
        try:
            peliculas=dao.listaPeliculas()
          
            if len(peliculas) >0:
                opciones.listarPeliculas(peliculas)
                input("Pulse Enter para continuar  ")
                os.system("clear")
              
            else:
                print ("No se encontraron peliculas")      
        except:
            print ("Ocurrio un error en opcion 1")    
        
    elif opcion == 2:
        pelicula =opciones.pedirDatosPelicula()
        
        try:
            dao.altaPelicula(pelicula)
        except Error as err:
            print ("Ocurrio un error al dar de alta la pelicula {0}".format(err))
        
    elif opcion == 3:
        try:
            peliculas=dao.listaPeliculas()
            if len(peliculas) >0:
                pelicula = opciones.pedirDatosPeliModificar(peliculas)
                print(pelicula)
                if len(pelicula) >0:
                    dao.actualizarPelicula(pelicula)
                else:
                    print ("Codigo de película no encontrado") 
                             
            else:
                print ("No se encontraron peliculas")     
        except Error as err:
            
            print ("Ocurrio un error al intentar eliminar la pelicula {0}".format(err))
          
  
    elif opcion == 4:
        try:
            peliculas=dao.listaPeliculas()
       
            if len(peliculas) >0:
                codigoPeliEliminar = opciones.pedirDatosPeliEliminar(peliculas)
                print(codigoPeliEliminar)
             
                if codigoPeliEliminar != "":
                    dao.eliminarPelicula(codigoPeliEliminar)
                else:
                    print ("Codigo de película no encontrado")  
                        
            else:
                print ("No se encontraron peliculas")     
        except Error as err:
            
            print ("Ocurrio un error al intentar eliminar la pelicula {0}".format(err))
        
    elif opcion == 5:
        nombre= input("Introduce el nombre de la base de datos a crear:  ")
        dao.crear_BBDD(nombre)
  
    
    elif opcion == 6:
        
        nombre= input("Introduce el nombre de la base de datos donde quieres crear las tablas:  ")
     
        dao.crear_Tablas(nombre)
    
    
    elif opcion == 7:
    
      nombre= input("Introduce el nombre de la base de datos donde quieres cargar los datos:  ")  
        
      api.cargar_datos_BBDD(nombre) 
    
    elif opcion == 8:
       
        # Llamar a la función hacer_consulta con el entero
        seleccion= api.hacer_consulta()
        consulta=api.mi_sql(seleccion)
        respuesta =api.respuesta(consulta)
        print("La solución a tu consulta que has realizado es: ")
        print(respuesta)
      
    elif opcion == 9:
        quit
    else:
        pass

menuPrincipal()

