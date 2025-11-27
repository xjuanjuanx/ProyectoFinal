from config.conexion import Conexion
from entities.producto import Producto
from mysql.connector import *

class DOAProducto(Conexion):
    def verProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM productos;")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"Error al intentar hacer la consulta {ex}")
        else:
            print("Error, no hay conexion")        
    def registrarProducto(self, p = Producto()):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO productos(nombreProducto, descripcion, precio, cantidad, categoria)"
                sql += "VALUES('{0}', '{1}', '{2}', '{3}', '{4}')"
                cursor.execute(sql.format(p.getNombreProducto(),p.getDescripcion(),p.getPrecio(),p.getCantidad(),p.getCategoria()))
                self.conexion.commit()
                print("Producto registrado con exito\n")
            except Error as ex:
                print(f"Error al intentar hacer la consulta {ex}") 
        else:
            print("Error, no hay conexion")
    def editarProducto(self, p = Producto()):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE productos SET nombreProducto = '{0}', descripcion = '{1}',precio = '{2}',\
                cantidad = '{3}', categoria = '{4}'"
                sql += "WHERE idProducto = '{5}';"
                cursor.execute(sql.format(p.getNombreProducto(),p.getDescripcion(),p.getPrecio(),p.getCantidad(),p.getCategoria(),p.getIdProducto()))
                self.conexion.commit()
                print("Producto actualizado con exito\n")
            except Error as ex:
                print(f"Error al intentar hacer la consulta {ex}") 
        else:
            print("Error, no hay conexion")
    def eliminarProducto(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"DELETE FROM productos WHERE idProducto = '{id}';"
                cursor.execute(sql)
                self.conexion.commit()
                print("Producto ha sido eliminado\n")
            except Error as ex:
                print(f"Error al intentar hacer la consulta {ex}") 
        else:
            print("Error, No hay conexion")
                
            