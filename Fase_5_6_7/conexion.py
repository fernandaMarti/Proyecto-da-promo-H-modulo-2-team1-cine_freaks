#Importamos las librerias necesarias
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import re
from time import sleep
import os


class DAO:
    def __init__(self):
        try:
         self.conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306')
         
         #print(self.conexion)
        
        except Error as ex:
            print("Error al intentar la conexión con la base de datos {0}".format(ex))
            print("Error al intentar realizar la consulta: {0}".format(ex))
                   
    
    def listaPeliculas(self):
        
        self.conexion.database = 'cinemextract'
        if self.conexion.is_connected():
            try:
                cursor =self.conexion.cursor()
                cursor.execute("SELECT * FROM moviesdataset ORDER BY id_pelicula ASC")
                resultados=cursor.fetchall()
                cursor.close
                #columnas=['Tipo pelicula,'Titulo pelicula',]
                #df = pd.DataFrame(resultados, columns=columnas)
                return resultados
                
            except Error as ex:
                               
                print("Error al intentar realizar la consulta: {0}".format(ex))
                
        self.conexion.close()
                
    def altaPelicula(self, pelicula):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO moviesdataset (tipo_pelicula, titulo_pelicula, anno_estreno, mes_estreno, id_pelicula, genero_pelicula) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, pelicula)
                self.conexion.commit()
                print("Película dada de alta correctamente")
            except Error as ex:
                print("Error al intentar realizar la consulta: {0}".format(ex))

        self.conexion.close()

    def actualizarPelicula (self,pelicula):
        if self.conexion.is_connected():
            try:
                
                cursor =self.conexion.cursor()
                sql = "UPDATE moviesdataset SET tipo_pelicula = %s, titulo_pelicula = %s, anno_estreno = %s, mes_estreno = %s, genero_pelicula = %s WHERE id_pelicula = %s"
                cursor.execute(sql, pelicula)
                self.conexion.commit()
                print ("Película actualizada correctamente")

            except Error as ex:
                           
                print("Error al intentar realizar la consulta: {0}".format(ex))
    
        self.conexion.close()
    
    def eliminarPelicula(self,codigocodigoPeliEliminar):
         
         if self.conexion.is_connected():
             
            try:
                cursor =self.conexion.cursor()
                
                sql = "DELETE FROM moviesdataset WHERE id_pelicula = %s"
                cursor.execute(sql, (codigocodigoPeliEliminar,))
                
                self.conexion.commit()
                
                print ("Película dada de baja correctamente")
                
            except Error as ex:
                
                print("Error al intentar realizar la consulta: {0}".format(ex))
                
         self.conexion.close()
    
    def crear_BBDD(self,nombre_BBDD):
                      
            try:
                cursor =self.conexion.cursor()
                
                sql = "CREATE DATABASE {}".format(nombre_BBDD)
                
                #sql = "CREATE DATABASE %s"
                
                cursor.execute(sql)
                
                self.conexion.commit()
                
                print ("Base de datos creado correctamente")
                          
            except Error as ex:
                
                print("Error al crear la base de datos: {0}".format(ex))
         
     
    # Creamos las tablas
              
    def crear_Tablas(self, nombre_BBDD):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
            
                # Cambiar a la base de datos especificada
                self.conexion.database = nombre_BBDD
                
            
                # Comprobar si la base de datos existe
                cursor.execute("SHOW TABLES")
                tablas = cursor.fetchall()
                print(tablas)
                
                if ('moviesdataset',) in tablas:
                    print("La tabla moviesdataset ya existe en la base de datos.")
                else:
                    # Crear la tabla si no existe
                    sql = "CREATE TABLE moviesdataset (tipo_pelicula VARCHAR(45), titulo_pelicula VARCHAR(100), anno_estreno INT, mes_estreno VARCHAR(45), id_pelicula VARCHAR(20), genero_pelicula VARCHAR(45), PRIMARY KEY (id_pelicula))"
                    cursor.execute(sql)
                    self.conexion.commit()
                    print("Tabla moviesdataset creada correctamente")
                
                if ('actores',) in tablas:
                    print("La tabla actores ya existe en la base de datos.")
                else:
                    # Crear la tabla si no existe
                    sql = "CREATE TABLE actores (id_actor INT AUTO_INCREMENT, nombre_actor VARCHAR (100), anno_nacimiento INT, conocido VARCHAR (45), que_hace VARCHAR (45), premios INT, PRIMARY KEY (id_actor))"
                    cursor.execute(sql)
                    self.conexion.commit()
                    print("Tabla actores creada correctamente")
                    
                if ('detalles_peliculas',) in tablas:
                    print("La tabla detalles_peliculas ya existe en la base de datos.")
                else:
                    # Crear la tabla si no existe
                    sql = "CREATE TABLE detalles_peliculas (id_detalle_peli INT AUTO_INCREMENT, id_pelicula VARCHAR(20), puntuacion_imdb VARCHAR (45), puntuacion_rotten VARCHAR (45), directores VARCHAR (255), guionistas VARCHAR(255), argumento VARCHAR (2000), duracion VARCHAR (45), nombre_pelicula VARCHAR (100), PRIMARY KEY (id_detalle_peli), FOREIGN KEY (id_pelicula) REFERENCES MoviesDataset (id_pelicula))"
                    cursor.execute(sql)
                    self.conexion.commit()
                    print("Tabla detalles_peliculas creada correctamente")
                    
                if ('oscars',) in tablas:
                    print("La tabla oscars ya existe en la base de datos.")
                else:
                    # Crear la tabla si no existe
                    sql = "CREATE TABLE oscars (id_ceremonia INT, fecha_ceremonia INT,mejor_pelicula VARCHAR (255),mejor_director VARCHAR (100),mejor_actor VARCHAR (100),mejor_actriz VARCHAR (100),PRIMARY KEY (id_ceremonia))"
                    cursor.execute(sql)
                    self.conexion.commit()
                    print("Tabla oscars creada correctamente")
                               
                if ('int_pelis_actores',) in tablas:
                    print("La tabla int_pelis_actores ya existe en la base de datos.")
                else:
                    # Crear la tabla si no existe
                    sql = "CREATE TABLE int_pelis_actores (id_actor INT, id_pelicula VARCHAR(20), PRIMARY KEY (id_actor,id_pelicula), FOREIGN KEY (id_actor) REFERENCES actores (id_actor), FOREIGN KEY (id_pelicula) REFERENCES MoviesDataset (id_pelicula))"
                    cursor.execute(sql)
                    self.conexion.commit()
                    print("Tabla int_pelis_actores creada correctamente")
                
                
            except Error as ex:
                print("Error al crear la tabla: {0}".format(ex))

    
class API:    
    def __init__(self):
        try:
            self.conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306')
         
            #print(self.conexion)
        
        except Error as ex:
            print("Error al intentar la conexión con la base de datos {0}".format(ex))
            print("Error al intentar realizar la consulta: {0}".format(ex))
        
         
    def cargar_datos_BBDD (self,nombre_BBDD):
             
        # Cambiar a la base de datos especificada
        
        self.conexion.database = nombre_BBDD
        
        #Metemos los datos de la fase 1
        
        url ="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/Fase1.csv"
        
        data_pelis =pd.read_csv(url)
        
        data_pelis.fillna('N/A', inplace=True)
        data_pelis['mes_estreno'].fillna('N/A', inplace=True)
        
        #data_pelis.info()
             
        #print(data_pelis)
                
        lista_pelis=[tuple(i) for i in data_pelis.values]
        #print(lista_pelis)
        
        #df_fase1=pd.DataFrame(lista_pelis)
        
        if self.conexion.is_connected():
            
           mycursor = self.conexion.cursor()
           
            
           sql = "INSERT INTO moviesdataset (tipo_pelicula, titulo_pelicula, anno_estreno, mes_estreno,id_pelicula,genero_pelicula) VALUES (%s, %s, %s, %s,%s,%s)" 

                           
           #peliculas el nombre del archivo correspondiente
           try:
                mycursor.executemany(sql, lista_pelis)
                self.conexion.commit()
                print(mycursor.rowcount,"registros insertados")
           except mysql.connector.Error as err:
                print("Ha habido un error en la inserción")
                print(err)
        
        #Metemos los datos de la fase 2
        
        url ="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/Fase2.csv"
        
        data_detalle_pelis =pd.read_csv(url)
        
        data_detalle_pelis.fillna('N/A', inplace=True)
        #data_detalle_pelis['mes_estreno'].fillna('N/A', inplace=True)
        
        data_detalle_pelis.info()
             
        #print(data_pelis)
                
        lista_pelis=[tuple(i) for i in data_detalle_pelis.values]
        
        #print(lista_pelis)
        
        #df_fase1=pd.DataFrame(lista_pelis)
        
        if self.conexion.is_connected():
            
           mycursor = self.conexion.cursor()
           
           # Cambiar a la base de datos especificada
           self.conexion.database = nombre_BBDD
            
           sql = "INSERT INTO detalles_peliculas (id_pelicula,puntuacion_imdb,puntuacion_rotten,directores,guionistas,argumento,duracion,nombre_pelicula) VALUES (%s, %s, %s, %s,%s,%s, %s, %s)" 

                    
           #peliculas el nombre del archivo correspondiente
           try:
                mycursor.executemany(sql, lista_pelis)
                self.conexion.commit()
                print(mycursor.rowcount,"registros insertados")
           except mysql.connector.Error as err:
                print("Ha habido un error en la inserción")
                print(err) 
                
                
        # Metemos el codigo para rellenar los datos de la tabla intermedia.'''
        
        
                
        #Metemos los datos de la fase 3
        
        url ="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/Fase3.csv"
        
        data_actores =pd.read_csv(url)
        
        #data_actores.fillna('N/A', inplace=True)
        data_actores['anno_nacimiento'].fillna(0, inplace=True)
        data_actores['premios'].fillna(0, inplace=True)
        
        data_actores.info()
             
        #print(data_actores)
                
        lista_actores=[tuple(i) for i in data_actores.values]
        #print(lista_actores)
        
        #df_fase3=pd.DataFrame(lista_actores)
        
        if self.conexion.is_connected():
            
           mycursor = self.conexion.cursor()
           
           # Cambiar a la base de datos especificada
           self.conexion.database = nombre_BBDD

           sql = "INSERT INTO actores (nombre_actor, anno_nacimiento, conocido, que_hace, premios) VALUES (%s, %s, %s, %s,%s)" 

                    
           #insertamos la lista de actores
           try:
                mycursor.executemany(sql, lista_actores)
                self.conexion.commit()
                print(mycursor.rowcount,"registros insertados")
           except mysql.connector.Error as err:
                print("Ha habido un error en la inserción")
                print(err) 
    
        #Metemos los datos de la fase 4
        
        url ="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/Fase-4.csv"
        
        data_oscars =pd.read_csv(url)
        
        #data_oscars.fillna('N/A', inplace=True)
        #data_oscars['mes_estreno'].fillna('N/A', inplace=True)
        
        data_oscars.info()
             
        #print(data_oscars)
                
        lista_oscars=[tuple(i) for i in data_oscars.values]
        #print(lista_oscars)
        
        #df_fase3=pd.DataFrame(lista_oscars)
        
        if self.conexion.is_connected():
            
           mycursor = self.conexion.cursor()
           
           # Cambiar a la base de datos especificada
           self.conexion.database = nombre_BBDD
            
           sql = "INSERT INTO oscars (id_ceremonia, fecha_ceremonia, mejor_pelicula, mejor_director, mejor_actor, mejor_actriz) VALUES (%s, %s, %s, %s,%s,%s)" 

                     
           #insertamos la lista de oscars
           try:
                mycursor.executemany(sql, lista_oscars)
                self.conexion.commit()
                print(mycursor.rowcount,"registros insertados")
           except mysql.connector.Error as err:
                print("Ha habido un error en la inserción")
                print(err) 
                
        #Rellenamos la tabla intermedia:
        
        def insertar_datos_tabla_int_pelis_actores():
            try:
                # Conexión a la base de datos
                conexion = mysql.connector.connect(user='root', password='tu_contraseña', host='localhost', port='3306', database='cinemextract')
                cursor = conexion.cursor()
                
                url_actores="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/lista_actores_prueba.csv"
                url_peliculas="https://raw.githubusercontent.com/fernandaMarti/Proyecto-da-promo-H-modulo-2-team1-cine_freaks/main/Fase1.csv"

                # Leer datos de los archivos CSV
                datos_actores = pd.read_csv(url)
                datos_peliculas = pd.read_csv(url)

                # Insertar datos en la tabla intermedia
                for dato_actor in datos_actores:
                    for dato_pelicula in datos_peliculas:
                        sql_insert = "INSERT INTO int_pelis_actores (id_actor, id_pelicula) VALUES (%s, %s)"
                        valores = (dato_actor[0], dato_pelicula[4])  # Suponiendo que el ID del actor está en la primera columna y el ID de la película está en la primera columna
                        cursor.execute(sql_insert, valores)

                conexion.commit()
                print("Datos insertados correctamente en la tabla intermedia.")

            except Error as e:
                print("Error al insertar datos en la tabla intermedia:", e)
                conexion.rollback()

            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
    
    
    def hacer_consulta(self):
        
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                              host='127.0.0.1', database='cinemextract')
        
      
         
        mycursor = cnx.cursor()
        
        mostrar_consultas= "SELECT Num_consulta,descripcion FROM consultas"
        
        mycursor.execute(mostrar_consultas)
        
        myresult = mycursor.fetchall()
        
                
        os.system("clear")
        print("")      
        print("CONSULTAS SQL")
        print("")
        myresult = "\n".join(map(str, myresult))
        
        print("")
               
        return int(input("Introduzca la consulta que quiere realizar introduciendo el numero de consulta: "))
        
            
    def mi_sql(self,seleccion):
        
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                              host='127.0.0.1', database='cinemextract')
              
        mycursor = cnx.cursor()
        
        consulta_seleccionada= "SELECT consulta FROM consultas WHERE Num_consulta = %s"
                  
        mycursor.execute(consulta_seleccionada,(seleccion,))
        
        myresult = mycursor.fetchall()
        
                     
        return myresult
    
    
    def respuesta(self,consulta):
        
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                              host='127.0.0.1', database='cinemextract',port='3306')
        
        print(cnx)
        try:
            
            consulta_formateada = consulta[0][0]
                 
            mycursor = cnx.cursor()
                
            mycursor.execute(consulta_formateada)
        
            respuesta = mycursor.fetchall()
        
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            respuesta = None

        finally:
        # Asegurarse de cerrar el cursor y la conexión a la base de datos
            if mycursor:
                mycursor.close()
            if cnx:
                cnx.close()
                     
        return respuesta