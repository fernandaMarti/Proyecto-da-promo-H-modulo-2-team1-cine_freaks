import mysql.connector
from mysql.connector import Error
#Importamos las librerias necesarias
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from time import sleep


class DAO:
    def __init__(self):
        try:
         self.conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',database='cinemextract',port='3306')
         
         #print(self.conexion)
        
        except Error as ex:
            print("Error al intentar la conexión con la base de datos {0}".format(ex))
            print("Error al intentar realizar la consulta: {0}".format(ex))
                   
    
    def listaPeliculas(self):
        if self.conexion.is_connected():
            try:
                cursor =self.conexion.cursor()
                cursor.execute("SELECT * FROM moviesdataset ORDER BY id_pelicula ASC")
                resultados=cursor.fetchall()
                cursor.close
                return resultados
                
            except Error as ex:
                               
                print("Error al intentar realizar la consulta: {0}".format(ex))
                
    def altaPelicula(self,pelicula):
        if self.conexion.is_connected():
            try:
                
                cursor =self.conexion.cursor()
                sql="INSERT INTO moviesdataset (id_pelicula, titulo_pelicula, tipo_pelicula, genero_pelicula, anno_estreno, mes_estreno) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')"
                cursor.execute(sql.format(pelicula[0],pelicula[1],pelicula[2],pelicula[3],pelicula[4],pelicula[5]))
                self.conexion.commit()
                print ("Película dada de alta correctamente")
            
                
            except Error as ex:
                               
                print("Error al intentar realizar la consulta: {0}".format(ex))
        

    def actualizarPelicula (self,pelicula):
        if self.conexion.is_connected():
            try:
                print(pelicula)
                cursor =self.conexion.cursor()
                sql="UPDATE moviesdataset SET titulo_pelicula ='{1}',tipo_pelicula='{2}', genero_pelicula='{3}', anno_estreno='{4}', mes_estreno='{5}' WHERE id_pelicula ='{0}' "
                cursor.execute(sql.format(pelicula[0],pelicula[1],pelicula[2],pelicula[3],pelicula[4],pelicula[5]))
                self.conexion.commit()
                print ("Película dada de alta correctamente")

                
            except Error as ex:
                           
                print("Error al intentar realizar la consulta: {0}".format(ex))
    
    
    
    def eliminarPelicula(self,codigocodigoPeliEliminar):
         
         if self.conexion.is_connected():
             
            try:
                cursor =self.conexion.cursor()
                
                sql= "DELETE FROM moviesdataset WHERE id_pelicula = '{0}' "
                
                cursor.execute(sql.format(codigocodigoPeliEliminar))
                
                self.conexion.commit()
                
                print ("Película dada de baja correctamente")
                
            except Error as ex:
                
                print("Error al intentar realizar la consulta: {0}".format(ex))
    
    def crear_BBDD(self,nombre_BBDD):
        
         if self.conexion.is_connected():
             
            try:
                cursor =self.conexion.cursor()
                
                sql= "CREATE DATABASE %s"
                
                cursor.execute(sql, (nombre_BBDD,))
                
                self.conexion.commit()
                
                print ("Base de datos creado correctamente")
                
            except Error as ex:
                
                print("Error al crear la base de datos: {0}".format(ex))
    
    # Falta ver como pasamos los parámetros para crear la tabla
              
    def crear_Tabla(self,nombre_Tabla,param):
        
        if self.conexion.is_connected():
             
            try:
                cursor =self.conexion.cursor()
                
                sql= "CREATE TABLE %s (name VARCHAR(255), address VARCHAR(255))"
                
                cursor.execute(sql.format(nombre_Tabla))
                
                self.conexion.commit()
                
                print ("Tabla creada correctamente")
                
            except Error as ex:
                
                print("Error al crear la tabla: {0}".format(ex))
        
    
class API:    
    
    def llamar_API(url,type='movie', genere='Drama'):
        #definimos la querystring y la API key
        
        querystring = {"titleType":type,"startYear":"2010","endYear":"2024","genre":genere}
        API_key = '2d7083a699mshd0e8039e2063bedp140338jsn9b141653fce1'
        
        # API_key Nuria = '58296df2a9mshb28a81ec4003c84p15333ejsn11ad25c7c1b8'
        # API_key Sharon = '2d7083a699mshd0e8039e2063bedp140338jsn9b141653fce1'
        # API_key3 Silvia = '039163dca0msh7ecfddf47a57b42p193f39jsn80c27500a5c2'
        
        headers = {"X-RapidAPI-Key": API_key,"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"}

        # creamos una lista para almacenar las respuestas de la funcion de llamada a la API
        lista_respuestas = []
        lista_info_respuestas = []
        dict = {'Tipo':[],
                 'Nombre':[],
                 'Año_estreno':[],
                 'Mes_estreno': [],
                 'Id':[]}
        
               
        while url.startswith('https'):
           
            #realizmos la llamada y almacenamos los códigos de respuesta en la lista de respuestas
            response_pelis = requests.get(url, headers=headers, params=querystring)
            
            lista_respuestas.append(response_pelis.status_code)
            
            lista_info_respuestas.append(response_pelis.reason)
            
            if response_pelis.status_code == 200:

                #convertimos los resulatos a formato json
                js_response_pelis = response_pelis.json()

                #guardamos la inforación de la API dónde tenemos la dirección de la siguiente página
                next = js_response_pelis['next']

                #guardamos la parte donde tenemos la infomación en una variable
                info_pelis = js_response_pelis['results']

                #guardamos toda la información en el diccionario con un for loop    
                for peli in info_pelis:

                    dict['Tipo'].append(peli['titleType']['text'])
                    dict['Nombre'].append(peli['titleText']['text'])
                    dict['Id'].append(peli['id'])
                    dict['Año_estreno'].append(peli['releaseYear']['year'])

                    #Hacemos un try/expect para las películas que no se han estrenado todavía            
                    try:
                        dict['Mes_estreno'].append(peli['releaseDate']['month'])
                    except:            
                        dict['Mes_estreno'].append('por estrenar')

                #iniciamos el loop try-except para que cree la variable de la nueva url mientras tengamos una url en ´next´
                try:
                    #definimos la base de la nueva url
                    url_fixed = "https://moviesdatabase.p.rapidapi.com"
                    #definimos la nueva url
                    url=url_fixed+next
                    #definimos el nuevo querystring
                    querystring = {}

                except:
                    break

            else:
                print(f'Error {response_pelis.status_code} en la llamada a la API {response_pelis.reason}')
                break

        print(f'Fin: Se han añadido l@s {type}s del género {genere} a tu diccionario.')
        
        #Almacenamos la infomacion del diccionario en distintas listas, cada una corresponde a una key 
        lista_tipos = dict['Tipo']
        lista_nombre = dict['Nombre']
        lista_anno = dict['Año_estreno']
        lista_mes = dict['Mes_estreno']
        lista_id = dict['Id']

        #Creamos un zip con las listas que hemos creado para que nos guarde la infoamción de cada una de las pelis en una tupla
        zip_pelis = zip(lista_tipos, lista_nombre, lista_anno, lista_mes, lista_id)
        lista_tuplas_pelis = list(zip_pelis)
        len(lista_tuplas_pelis)
        print(lista_tuplas_pelis)
       
        return lista_tuplas_pelis
    
    def crearcsv (tuplas_pelis):
        pass
    
    def crear_BBDD():
        pass
    
    def acciones_BBDD():
        pass