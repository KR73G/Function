#Funciòn Void

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Mundo")

#Funciòn con parametros

def saludar(nombre):
    print("Hola, mundo " + nombre + "!")

saludar("Soy Raul")

#Funciòn return

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)
