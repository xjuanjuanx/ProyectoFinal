from mysql.connector import *
import mysql.connector

class Conexion(object):
    conexion = ""
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host ="localhost", # 127.0.0.1
                port = 3306, #Puerto del mysql
                user = "root", #Usuario de conexion al mysql
                password = "", #clave de conexion al mysql
                db = "crudpython_db" #base de datos a la cual nos conectamos
            )
        except Error as ex:
            return(f"Error al realizar la conexion:\n {ex}")
        




    
