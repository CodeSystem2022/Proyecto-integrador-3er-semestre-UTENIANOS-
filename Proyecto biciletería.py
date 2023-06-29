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

