class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")



class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")



class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
    


class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda
    

productos = {
    "varon" : {
        "zapato" : {
            "precio" : 34.00,
            "cantidad" : 10
        },
        
        "pantalon" : {
            "precio" : 80.00,
            "cantidad" : 17
        },
        
        "camisa" : {
            "precio" : 50.00,
            "cantidad" : 20
        },
        
    },
    "mujer" : {
        "tacones" : {
            "precio" : 39.00,
            "cantidad" : 9
        },
        
        "falda" : {
            "precio" : 46.00,
            "cantidad" : 15
        },
        
        "vestido" : {
            "precio" : 51.00,
            "cantidad" : 12
        },
    }

}


inventario = Inventario()

while 1:
    
    print("Bienvenido a la tienda!")
    print("Ingrese la clase de ropa")
    
    categoria = input("varon/mujer: ")
    
    if categoria == "varon":
        
        print("Has elegido ropa para varones")
        print(productos["varon"])
        
        nombre = input("Ingrese producto: ")
        talla = input("Ingrese talla: ")
        
        precio = productos["varon"][nombre]["precio"]
        cantidad = productos["varon"][nombre]["cantidad"]
        
        new_producto_v = RopaHombre(nombre, precio, cantidad, talla)
        inventario.agregar_prenda(new_producto_v)
        
    elif categoria == "mujer":
        
        print("Has elegido ropa para mujeres")
        print(productos["mujer"])
        
        nombra = input("Ingrese producto: ")
        talla = input("Ingrese talla: ")
        
        precio = productos["mujer"][nombra]["precio"]
        cantidad = productos["mujer"][nombra]["cantidad"]
        
        new_producto_m = RopaMujer(nombra, precio, cantidad, talla)
        inventario.agregar_prenda(new_producto_m)
        
    else:
    
        print("Gracias")
        inventario.mostrar_inventario()
        exit()
        
    