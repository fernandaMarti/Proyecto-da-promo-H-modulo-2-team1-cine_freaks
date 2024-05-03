
from Conexion.conexion import DAO
import opciones
#Vamos a hacer un Crud con Python

def menuPrincipal():
    
    continuar =True
    while continuar:
        opcionCorrecta =False
        
        while not opcionCorrecta:
            
            print("===========================    Menú    ==============================")
            print("1. Ver peliculas")
            print("2. Alta Pelicula")
            print("3. Eliminar Pelicula")
            print("4. Editar Pelicula")
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
            print ("Ocurrio un error")    
        
    elif opcion ==2:
        pelicula =None
        try:
            dao.altaPelicula(pelicula)
        except:
            print ("Ocurrio un error")
        
    elif opcion ==3:
        print ("Es la opcion 3")
    elif opcion ==4:
        print ("Es la opcion 4")
        
    elif opcion ==5:
        quit
    else:
        pass

menuPrincipal()

