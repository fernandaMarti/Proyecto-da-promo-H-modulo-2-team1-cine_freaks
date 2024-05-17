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
    if opcion ==1:
        
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
                print(pelicula)
                if len(pelicula) >0:
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
                print(codigoPeliEliminar)
             
                if codigoPeliEliminar != "":
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
  
    
    elif opcion ==6:
        
        nombre= input("Introduce el nombre de la base de datos donde quieres crear las tablas:  ")
     
        dao.crear_Tablas(nombre)
    
    
    elif opcion == 7:
    
      nombre= input("Introduce el nombre de la base de datos donde quieres cargar los datos:  ")  
        
      api.cargar_datos_BBDD(nombre)
      
      
    
    
    elif opcion==8:
       
        print("CONSULTAS SQL")
        print("")
        print('1. ¿Que mujer ha ganado mas premios Óscar a major actriz?')
        print('2. ¿Qué género es el mejor valorado en IMDB?')
        print('3. ¿Qué género es el mejor valorado en Tomatometro?')
        print('4. ¿En que año se estrenaron más películas?')
        print('5. ¿En que año se estrenaron mas cortos?')
        print('6. ¿Cuál es el corto mejor valorado en IMDB?')
        print('7. ¿Cuál es la película mejor valorada en IMDB?')
        print('8. ¿Qué palabra es la más utilizada en los títulos?')
        print('9. ¿Qué director ha dirigido más peliculas?')
        print('10. ¿Qué actor ha actuado en más peliculas?')
        print('11. ¿Quién es el actor más joven?')
        print('12. ¿Número de peliculas estrenadas por año?')
        print('13. Volver al menú')
        print("")
       
        
        consulta= input("Elige una consulta a realizar:")
            
        if consulta ==1:
            
            
            ''' Que actriz/actor ha ganado más premios
            SELECT nombre_actor AS 'actriz/actor', SUM(premios) AS 'num premios'
            FROM actores
            GROUP BY nombre_actor
            ORDER BY SUM(premios) DESC
            LIMIT 1;'''
            
        elif consulta==2:
            
            ''' 2. ¿Qué género es el mejor valorado en IMDB?
            SELECT genero_pelicula AS genero, SUM(puntuacion_imdb) AS puntuacion
            FROM MoviesDataset
            INNER JOIN detalles_peliculas ON MoviesDataset.id_pelicula = detalles_peliculas.id_pelicula
            GROUP BY genero_pelicula
            ORDER BY puntuacion DESC
            LIMIT 1;'''
         
        elif consulta==3:
            
            ''' '3. ¿Qué género es el mejor valorado en Tomatometro?'
            SELECT genero_pelicula AS genero, SUM(puntuacion_rotten) AS puntuacion
            FROM MoviesDataset
            INNER JOIN detalles_peliculas ON MoviesDataset.id_pelicula = detalles_peliculas.id_pelicula
            GROUP BY genero_pelicula
            ORDER BY puntuacion DESC
            LIMIT 1;'''
            
            
        elif consulta==4:
            
            '''-- '4. ¿En que año se estrenaron más películas?'
            SELECT anno_estreno AS 'año estreno', COUNT(id_pelicula) AS 'total estrenos'
            FROM MoviesDataset
            WHERE tipo_pelicula = 'movie'
            GROUP BY anno_estreno
            ORDER BY COUNT(id_pelicula) DESC
            LIMIT 1;'''
            
          
        elif consulta==5:
            
            ''' '5. ¿En que año se estrenaron mas cortos?'
            SELECT anno_estreno AS 'año estreno', COUNT(id_pelicula) AS 'total estrenos'
            FROM MoviesDataset
            WHERE tipo_pelicula = 'short'
            GROUP BY anno_estreno
            ORDER BY COUNT(id_pelicula) DESC
            LIMIT 1; '''
            
            pass
        elif consulta==6:
            
            ''' 6. ¿Cuál es el corto mejor valorado en IMDB?
            SELECT nombre_pelicula AS corto, SUM(puntuacion_imdb) AS puntuacion
            FROM detalles_peliculas
            WHERE id_pelicula IN (
					SELECT id_pelicula
                    FROM MoviesDataset
                    WHERE tipo_pelicula = 'short'
                    )
            GROUP BY corto
            ORDER BY puntuacion DESC
            LIMIT 1;'''

            
            
        elif consulta==7:
            
            ''' SELECT nombre_pelicula AS corto, SUM(puntuacion_imdb) AS puntuacion
            FROM detalles_peliculas
            WHERE id_pelicula IN (
					SELECT id_pelicula
                    FROM MoviesDataset
                    WHERE tipo_pelicula = 'movie'
                    )
            GROUP BY corto
            ORDER BY puntuacion DESC
            LIMIT 1; '''
            
        elif consulta==8:
            
            ''' 11. ¿Quién es el actor más joven?
            SELECT nombre_actor, anno_nacimiento AS año
            FROM actores
            ORDER BY año DESC
            LIMIT 1;'''

            
        else:
            menuPrincipal()
       
    elif opcion ==9:
        quit
    else:
        pass

menuPrincipal()

