################################################# DELGADO CAROLINA #################################################
from pymongo import MongoClient

class Bicicleta:
    def _init_(self, nro_de_serie, modelo, anio, precio):
        self.nro_de_serie = nro_de_serie
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def _str_(self):
        return f"n° de serie: {self.nro_de_serie}, modelo: {self.modelo}, año: {self.anio}, precio: ${self.precio}"

# Creamos la base de datos y la colección
class Bicicleteria:
    def _init_(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['bicicleteria']
# Eliminar la colección 'bicicletas' si existe
        if 'bicicletas' in self.db.list_collection_names():
            self.db.drop_collection('bicicletas')

        self.collection = self.db['bicicletas'] # Creamos la colección
        self.ganancias = 0  # Agregar el atributo ganancias
        self.cantidad_de_ventas = 0  # Agregar el atributo cantidad_de_ventas
        print("Bicicleteria creada")

################################################# SABA JUAN AGUSTÍN #################################################
# 1 - Añadir bicicleta - Creacion de bicicletas
    def crear_bici(self):
        print("\n---------------------------")
        print("Añadir bicicleta")
        print("---------------------------")
        nro_de_serie = input("Ingrese el nro de serie: ")
        modelo = input("Ingrese el modelo: ")
        anio = int(input("Ingrese el año: "))
        precio = float(input("Ingrese el precio: "))
        bici = Bicicleta(nro_de_serie, modelo, anio, precio)
        self.guardar_bici(bici)
        print("\nBicicleta creada con exito\n")
        return self.menu()

# Insertamos la bicicleta en la colección
    def guardar_bici(self, bicicleta):
        self.collection.insert_one({
            "nro_de_serie": bicicleta.nro_de_serie,
            "modelo": bicicleta.modelo,
            "anio": bicicleta.anio,
            "precio": bicicleta.precio
        })
################################################# COSTILLA CELINA #################################################
# 2 - Mostrar bicicletas - Mostrar todas las bicicletas
    def mostrar_bicis(self):
        print("\n---------------------------")
        for bici in self.collection.find():
            print(bici)
        return self.menu()

################################################# PUTRINO AGUSTIN #################################################
# 3 - Vender bicicleta - Eliminar bicicletas
    def vender_bici(self):
        print("\n---------------------------")
        print("Vender bicicleta")
        print("---------------------------\n")
        bicicletas = list(self.collection.find())
        if len(bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()

        self.listar_bicis(bicicletas)
        nro_de_serie = input("\nIngrese el nro de serie: ")
        bici = self.collection.find_one({"nro_de_serie": nro_de_serie})
        if bici: # Si la bicicleta existe
            self.ganancias += bici["precio"]
            self.cantidad_de_ventas += 1
            self.collection.delete_one({"nro_de_serie": nro_de_serie})
            print("\nBicicleta vendida")
        else: # Si la bicicleta no existe
            print("Bicicleta no encontrada")
        return self.menu()


    def listar_bicis(self, bicicletas):
        print("\n---------------------------")
        for bici in bicicletas:
            print(bici)

    # Ganancias y ventas - Mostrar ganancias y ventas
    def ganancias_y_ventas(self):
        print("\n---------------------------")
        print("Ganancias y ventas")
        print("---------------------------")
        print(f"Ganancias: ${self.ganancias}")
        print(f"Ventas: {self.cantidad_de_ventas}")
        return self.menu()
################################################# TORRES DAVID #################################################
# 5- Revisar precio - Mostrar precio de una bicicleta
    def revisar_precio(self):
        bicicletas = list(self.collection.find())
        if len(bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()
        # Mostramos las bicicletas

        self.listar_bicis(bicicletas)
        nro_de_serie = input("Ingrese el nro de serie: ")
        bici = self.collection.find_one({"nro_de_serie": nro_de_serie})
        if bici:
            print(f"\nPrecio: ${bici['precio']}")
        else:
            print("Bicicleta no encontrada")
        return self.menu()
################################################# TORRES MIRIAM #################################################
# 6 - Modificar precio - Modificar precio de una bicicleta
    def modificar_precio(self):
        print("\n---------------------------")
        print("Modificar precio")
        print("---------------------------\n")
        bicicletas = list(self.collection.find())
        if len(bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()

        self.listar_bicis(bicicletas)
        nro_de_serie = input("Ingrese el nro de serie: ")
        bici = self.collection.find_one({"nro_de_serie": nro_de_serie})
        if bici:
            precio = float(input("Ingrese el nuevo precio: "))
            self.collection.update_one({"nro_de_serie": nro_de_serie}, {"$set": {"precio": precio}})
            print("Precio modificado")
        else:
            print("Bicicleta no encontrada")
        return self.menu()
################################################# GIANGRAVE FACUNDO #################################################

