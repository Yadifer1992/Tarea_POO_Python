# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__edad = edad

    # Métodos públicos para acceder a los atributos privados (Getters)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Métodos públicos para modificar los atributos privados (Setters)
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    # Método general que será sobrescrito por las clases hijas (polimorfismo)
    def hacer_sonido(self):
        return "Este animal hace un sonido."

    # Método para mostrar la información del animal
    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

# Clase derivada: Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la clase base (super)
        super().__init__(nombre, edad)
        self.raza = raza  # Atributo adicional

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        return "Guau guau"

    # Sobrescritura del método mostrar_info para incluir la raza
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Raza: {self.raza}"

# Clase derivada: Gato (hereda de Animal)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color  # Atributo adicional

    def hacer_sonido(self):
        return "Miau miau"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Color: {self.color}"

# Crear instancias de las clases (objetos)
perro1 = Perro("Firulais", 5, "Labrador")
gato1 = Gato("Michi", 3, "Blanco")

# Mostrar información y comportamiento (uso de métodos)
print("Información del Perro:")
print(perro1.mostrar_info())
print("Sonido:", perro1.hacer_sonido())

print("\nInformación del Gato:")
print(gato1.mostrar_info())
print("Sonido:", gato1.hacer_sonido())

# Modificar atributos con setters
perro1.set_edad(6)
gato1.set_nombre("Pelusa")

# Ver los cambios
print("\nDespués de actualizar los datos:")
print(perro1.mostrar_info())
print(gato1.mostrar_info())