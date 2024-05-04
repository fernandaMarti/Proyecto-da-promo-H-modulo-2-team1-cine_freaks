import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
         self.conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',database='cinemextract',port='3306')
         
         print(self.conexion)
        
        except Error as ex:
            print("Error al intentar la conexión con la base de datos {0}".format(ex))
            print("Error al intentar realizar la consulta: {0}".format(ex))
                   
    
    def listaPeliculas(self):
        if self.conexion.is_connected():
            try:
                cursor =self.conexion.cursor()
                cursor.execute("SELECT * FROM moviesdataset ORDER BY id_pelicula ASC")
                resultados=cursor.fetchall()
                print (resultados)
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
                
                sql= "DELETE FROM moviesdataset WHERE id_registro = '{0}' "
                
                cursor.execute(sql.format(codigocodigoPeliEliminar))
                
                self.conexion.commit()
                
                print ("Película dada de baja correctamente")
                
            except Error as ex:
                
                print("Error al intentar realizar la consulta: {0}".format(ex))
        
                