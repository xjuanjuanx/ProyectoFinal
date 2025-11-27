from entities.producto import Producto

categorias = ["Ropa Masculina","Ropa Femenina", "Tecnologia", "Ferreteria", "Alimentos", "Hogar"]

def verProductos(productos):
    if not productos:
        print(f"\nNo hay productos registrados\n")
        return
    
    print(f"\nLista Productos\n")
    print("-"*120)
    print(f"{'ID':<5} {'Nombre':<35} {'Descripción':<40} {'Precio':<10} {'Cantidad': <10} {'Categoria':<15}")
    print("-"*120)
    
    for i, prod in enumerate(productos, start= 1):
        print(f"{prod[0]:<5} {prod[1]:<35} {prod[2]:<40} {prod[3]:<10} {prod[4]:<10} {prod[5]:<15}")
    print("-"*120)

def getDatosRegistro():
    nombre = descripcion = ""; precio = 0.0; cantidad = 0
    while True:
        nombre = input("Ingrese el nombre del producto:\n").strip()
        if nombre:
            break
        else:
            print("El nombre no puede tener espacio vacios, intente de nuevo")
    
    descripcion = input("Ingrese la descripcion del producto:\n").strip()
    precioC = False
    while not precioC:
        precio = input(f"Ingrese el precio de {nombre}\n")
        if precio.isnumeric():
            if (float(precio)>0):
                    precioC = True
                    precio = float(precio)
            else:
                print("El precio debe ser mayor a 0")
        else:
            print("Ingrese valores numericos")
    cantidadC = False
    while not cantidadC:
        cantidad = input(f"Ingrese la cantidad de {nombre}:\n").strip()
        if cantidad.isnumeric():
            if (int(cantidad)>0):
                cantidadC = True
                cantidad = int(cantidad)
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Ingrese solo valores numericos")
    
    print("Seleccione una Categoria:\n")
    for i, categoria in enumerate(categorias,1):
        print(f"{i} {categoria}")
    
    categoriaC = False
    categoriaS = ""
    while not categoriaC:
        opcion = input(f"ingrese el numero de la categoria de {nombre}:\n").strip()
        if opcion.isnumeric():
            if (int(opcion)>0 and int(opcion) <= len(categorias)):
                categoriaC = True
                categoriaS = categorias[int(opcion)-1]
            else:
                print("La categoria debe ser una de las propuestas")
        else:
            print("Ingrese valores numericos")
    print(" ")
    
    producto = Producto()
    producto.setNombreProducto(nombre)
    producto.setDescripcion(descripcion)
    producto.setPrecio(precio)
    producto.setCantidad(cantidad)
    producto.setCategoria(categoriaS)
    print(f"\nProducto ingresado: {nombre}\n")
    return producto

def getDatosModificar(productos):
    while True:
        try:
            verProductos(productos)
            idProd = int(input("Ingrese el ID del producto a editar:\n"))
            
            indexProducto = next((i for i, e in enumerate(productos) if e[0] == idProd), None)
            
            if indexProducto is None:
                print("Producto no encontrado.")
                return None
            else:
                producto = list(productos[indexProducto])
                print("\nCampos disponibles para editar:")
                campos = ["nombreProducto", "descripcion","precio","cantidad","categoria"]
                for i, campo in enumerate(campos, start=1):
                    print(f"{i}: {campo}")
                opcion = int(input("\ingrese el campo a editar\n"))
                if opcion < 1 or opcion >len(campos):
                    print("Opcion no valida")
                    return None
                if opcion >= 1 and opcion < 5:
                    nuevoValor = input(f"Ingrese nuevo valor para {(campos[opcion-1])}:\n ").strip()
                    campo = campos[opcion-1]
                    if campo == "precio":
                        nuevoValor=float(nuevoValor)
                    if campo == "cantidad":
                        nuevoValor = int(nuevoValor)
                else:
                    if campo == "categoria":
                        categoriaCorrecta = False
                        while not categoriaCorrecta:
                            print("\nCategorias disponibles:")
                            for i,categoria in enumerate(categorias,start=1):
                                print(f"{i}: {categoria}")
                        nuevoValor = input("Seleccione el numero de la categoria:\n").strip()
                        if nuevoValor.isnumeric():
                            nuevoValor = int(nuevoValor)
                            if 1<=nuevoValor <= len(categorias):
                                categoriaCorrecta = True
                                nuevoValor = categorias[nuevoValor-1]
                            else:
                                print("Opcion fuera de rango")
                        else:
                            print("Error, ingrese un valor numerico")
            producto[opcion] = nuevoValor
            
            productoEdit = Producto()
            productoEdit.setNombreProducto(producto[1])
            productoEdit.setDescripcion(producto[2])
            productoEdit.setPrecio(producto[3])
            productoEdit.setCantidad(producto[4])
            productoEdit.setCategoria(producto[5])
            productoEdit.setIdPorducto(producto[0])
            return productoEdit
        except ValueError:
            print("Error, Entrada no valida") 
            return None   
def getIdEliminar(productos):
    if not productos:
        print("No hay productos registrados")
        return ""
    verProductos(productos)
    codigo = input("Ingrese el codigo del producto a eliminar:\n").strip()
    
    if not codigo:
        print("Error: No se agrego ningun valor")
        return ""
    
    existeCodigo = False
    for prod in productos:
        if prod[0]==int(codigo):
            existeCodigo =True
            break
    
    if not existeCodigo:
        print("Error: Codigo no encontrado")
        return ""
    
    confirmar = input(f"Estas seguro de eliminar el producto con codigo {codigo}? Si/No\n").strip().lower()
    
    if confirmar == "si":
        codigo = int(codigo)
        return codigo
    else:
        print("Operacion Cancelada")
        return ""    
        
        
    
        
                
                