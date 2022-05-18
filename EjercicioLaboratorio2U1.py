
from operator import truth
#Función para el encabezado ESPE
def encabezado():
    print("***************************************")
    print("UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE")
    print("        Tomas Quirumbay Morales        ")
    print("              2do - ITIN               ")
    print("    Programación Orientada a objetos   ")
    print("***************************************")
encabezado()

#Función para crear el menú principal
def menu():
    print("***************************************")
    print("             Menú Principal            ")
    print("    Escriba 1 para ir al ejercicio     ")
    print("         Escriba 2 para salir          ")
    print("***************************************")
    while True:
        try:
            opcionMenu=int(input("Escoja la opción que desee: "))
            if opcionMenu==1:
                #Llamar a la función del ejercicio
                encontrarArea()
                break
            elif opcionMenu==2:
                print("Usted ha salido con éxito")
                #exit(0)
                break
            else:
                print("No existe esa opción, por favor vuelva a intentarlo")
        #Validación de opciones del menú principal
        except ValueError:
                print("**************************************")
                print("      Error, volver a intentarlo      ")
                print("**************************************")
menu()

#Se crea la función "encontrar area"
def encontrarArea(b,h):
    #Imprimirá el mensaje y se verá en pantalla una vez colocado los datos por consola
    print("=======================================================================")
    print("Se ha ingresado la base y la altura de un triángulo para hallar su área")
    print("=======================================================================")
    #Se crea la varianle "area" para hacer la operación del ejercicio
    area = (b*h)/2
    #Imprime el mensaje con la respuesta que haya dado el usuario en la consola
    print("El area del triángulo es: ", area)
    #Retornará la variable "area"
    return area
    #Permite al usuario ingresar los datos por consola y no datos definidos
encontrarArea(float(input("Ingrese la longitud de la base: ")), float(input("Ingrese la longitud de la altura: ")))

#Función para regresar al menú principal
def volverMenu():
    print("**************************************")
    print("     ¿Regresar al menú principal?     ")
    print("              yes/not                 ")
    print("**************************************")
    while True:
        try:
            opcion=input("Escoja la opción que desee: ")
            if opcion=="yes":
                #Llamar a la función menú
                menu()
                break
            elif opcion=="not":
                    print("Usted ha salido con éxito")
                    break
            else:
                    print("Por favor, vuelva a intentarlo")
        #Validación de opcioón para regresar al menú
        except ValueError:
                print("**************************************")
                print("      Error, volver a intentarlo      ")
                print("**************************************")
volverMenu()
