from models.DAOProducto import DOAProducto
from mysql.connector import *
from controllers.funcionesProducto import *
import os

def menuPrincipal():
    continuar = True
    while continuar:
        os.system("cls")
        opcionCorrecta = False
        while not opcionCorrecta:
            print("===========MENU PRINCIPAL===========")
            opc = int(input("\n---Seleciones una opcion---\n\n1. Mostrar Productos\n2. Registrar Productos\n3. Modificar Producto\n4. Eliminar Producto\n5. Salir\n"))
            if opc <1 or opc >5:
                print("Opcion incorrecta, ingresa nuevamente")
                opcionCorrecta = True
                continuar = True
            elif opc == 1:
                opcionCorrecta = True
                ejecutar(opc)
                input("Presione una tecla para continuar")
            elif opc == 2:
                opcionCorrecta == True
                ejecutar(opc)
                input("precione una tecla para continuar")
            elif opc == 3:
                opcionCorrecta == True
                ejecutar(opc)
                input("Precione una tecla para continuar")
            elif opc == 4:
                opcionCorrecta == True
                ejecutar(opc)
                input("Precione una tecla para continuar")
            elif opc == 5:
                continuar = False
                input("Gracias por usar el programa")
                break
            
def ejecutar(opc):
    daoProducto = DOAProducto()
    match opc:
        case 1:
            try:
                productos = daoProducto.verProductos()
                if len(productos) > 0:
                    verProductos(productos)
                else:
                    print("No hay productos registrados")
            except Error as ex:
                print(f"Error: {ex}")
        case 2:
            producto = getDatosRegistro()
            try:
                daoProducto.registrarProducto(producto)
            except Error as ex:
                print(f"Error: {ex}")
        case 3:
            productos = daoProducto.verProductos()
            producto = getDatosModificar(productos)
            try:
                if producto:
                    daoProducto.editarProducto(producto)
            except Error as ex:
                print(f"Error: {ex}")
        case 4:
            productos = daoProducto.verProductos()
            producto = getIdEliminar(productos)
            try:
                daoProducto.eliminarProducto(producto)
            except:
                print("Ha ocurrido un error")
        case _:
            print("Opcion no valida")
            
menuPrincipal()


