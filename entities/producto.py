class Producto(object):
    #Atributos privado
    __idProducto: int
    __nombreProducto: str
    __descripcion: str
    __precio: float
    __cantidad: int
    __categoria: str
    
    def __init__(self):
        pass
    
    #encapsulamiento
    
    def getIdProducto(self):
        return self.__idProducto
    def setIdPorducto(self,idProducto):
        self.__idProducto = idProducto
    
    def getNombreProducto(self):
        return self.__nombreProducto
    def setNombreProducto(self,nombreProducto):
        self.__nombreProducto = nombreProducto
    
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion
        
    def getPrecio(self):
        return self.__precio
    def setPrecio(self,precio):
        self.__precio = precio
        
    def getCantidad(self):
        return self.__cantidad
    def setCantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def getCategoria(self):
        return self.__categoria
    def setCategoria(self,categoria):
        self.__categoria = categoria
        