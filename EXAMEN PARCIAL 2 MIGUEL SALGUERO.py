#Miguel Salguero 1626923
# la parte de exportar en txt no pude hacer que funcione :c
import os

class Nodo:
    def __init__(self, pregunta=None, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

def preorden(raiz, recorrido):
    if raiz:
        recorrido.append(raiz.pregunta)
        preorden(raiz.si, recorrido)
        preorden(raiz.no, recorrido)

def inorden(raiz, recorrido):
    if raiz:
        inorden(raiz.si, recorrido)
        recorrido.append(raiz.pregunta)
        inorden(raiz.no, recorrido)

def postorden(raiz, recorrido):
    if raiz:
        postorden(raiz.si, recorrido)
        postorden(raiz.no, recorrido)
        recorrido.append(raiz.pregunta)

def exportar_recorrido(raiz):
    recorrido_preorden = []
    preorden(raiz, recorrido_preorden)
    recorrido_inorden = []
    inorden(raiz, recorrido_inorden)
    recorrido_postorden = []
    postorden(raiz, recorrido_postorden)

    with open(os.path.join(os.path.expanduser("~"), "Desktop", "recorrido_arbol.txt"), "w") as archivo:
        archivo.write("Recorrido en Preorden:\n")
        archivo.write("\n".join(map(str, recorrido_preorden)))  # Convertir a cadena antes de escribir
        archivo.write("\n\n")
        archivo.write("Recorrido en Inorden:\n")
        archivo.write("\n".join(map(str, recorrido_inorden)))  # Convertir a cadena antes de escribir
        archivo.write("\n\n")
        archivo.write("Recorrido en Postorden:\n")
        archivo.write("\n".join(map(str, recorrido_postorden)))  # Convertir a cadena antes de escribir

def jugar_juego(raiz):
    print("¡Bienvenido al juego de adivinanzas!")
    print("Piensa en algo, y yo intentaré adivinarlo.")
    nodo_actual = raiz
    while nodo_actual.si and nodo_actual.no:
        respuesta = input(nodo_actual.pregunta + " (s/n): ").lower()
        while respuesta not in ['s', 'n']:
            respuesta = input("¡Ups! Parece que no entendí, por favor responde 's' para sí o 'n' para no: ").lower()
        if respuesta == 's':
            nodo_actual = nodo_actual.si
        else:
            nodo_actual = nodo_actual.no

    if nodo_actual.si and nodo_actual.no:
        # Si aún hay preguntas en ambas ramas, seguimos preguntando
        jugar_juego(nodo_actual)
    elif nodo_actual.pregunta:
        adivinanza = nodo_actual.pregunta
        respuesta = input(f"¿Estoy pensando en '{adivinanza}'? (s/n): ").lower()
        while respuesta not in ['s', 'n']:
            respuesta = input("¡Vaya! Me he enredado, por favor responde 's' para sí o 'n' para no: ").lower()
        if respuesta == 's':
            print(f"¡Adiviné! Estabas pensando en '{adivinanza}'")
        else:
            objeto = input("¡Oh no! ¿Qué estabas pensando? ")
            pregunta_nueva = input(f"¡Vaya! No lo había adivinado... ¿Qué pregunta distinguiría '{objeto}' de '{adivinanza}'? ")
            respuesta_nueva = input(f"¿Cuál es la respuesta para '{objeto}'? (s/n): ").lower()
            while respuesta_nueva not in ['s', 'n']:
                respuesta_nueva = input("¡Lo siento, no te entendí! Responde 's' para sí o 'n' para no: ").lower()
            if respuesta_nueva == 's':
                nodo_actual.si = Nodo(objeto)
                nodo_actual.no = Nodo(adivinanza)
                print("¡Qué divertido! ¡Aprendí algo nuevo!")
            else:
                nodo_actual.si = Nodo(adivinanza)
                nodo_actual.no = Nodo(objeto)
                print("¡Ahora sí! ¡Seré mejor la próxima vez!")
    else:
        objeto = input("¡Ups! No pude adivinar lo que estabas pensando. ¿Qué era? ")
        pregunta_nueva = input(f"¡Vaya! No lo había adivinado... ¿Qué pregunta distinguiría '{objeto}' de '{nodo_actual.no.pregunta}'? ")
        respuesta_nueva = input(f"¿Cuál es la respuesta para '{objeto}'? (s/n): ").lower()
        while respuesta_nueva not in ['s', 'n']:
            respuesta_nueva = input("¡Lo siento, no te entendí! Responde 's' para sí o 'n' para no: ").lower()
        if respuesta_nueva == 's':
            nodo_actual.no = Nodo(objeto)
            print("¡Qué divertido! ¡Aprendí algo nuevo!")
        else:
            nodo_actual.no = Nodo(nodo_actual.no.pregunta)
            print("¡Ahora sí! ¡Seré mejor la próxima vez!")

def agregar_pregunta(raiz):
    print("\n¡Vamos a agregar una nueva pregunta para hacer el juego más emocionante!")
    pregunta = input("¿Qué pregunta distinguiría entre dos objetos, animales o personajes? ")
    respuesta = input(f"¿Cuál es la respuesta para '{pregunta}'? (s/n): ").lower()
    while respuesta not in ['s', 'n']:
        respuesta = input("¡Vaya! Me he enredado, por favor responde 's' para sí o 'n' para no: ").lower()
    if respuesta == 's':
        objeto = input("¿Qué objeto, animal o personaje tenías en mente? ")
        raiz.si = Nodo(pregunta, Nodo(objeto), Nodo(raiz.pregunta))
    else:
        objeto = input("¿Qué objeto, animal o personaje tenías en mente? ")
        raiz.no = Nodo(pregunta, Nodo(raiz.pregunta), Nodo(objeto))
    print("\n¡Perfecto! ¡El juego ahora es aún más emocionante!")

def jugar_de_nuevo(raiz):
    jugar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar == 's':
        jugar_juego(raiz)
        jugar_de_nuevo(raiz)
    elif jugar == 'n':
        print("\n¡Gracias por jugar! ¡Hasta la próxima!")

def mostrar_instrucciones():
    print("\nInstrucciones:")
    print("- Piensa en un objeto, animal o personaje.")
    print("- Responde las preguntas con 's' para sí y 'n' para no.")
    print("- Intentaré adivinar lo que estás pensando.")
    print("- Si no puedo adivinarlo, agregaré una nueva pregunta para aprender.")
    print("- Diviértete!")

def main():
    # Construir el árbol de adivinanzas
    raiz = Nodo("¿Es un animal?")
    raiz.si = Nodo("¿Tiene patas?")
    raiz.si.si = Nodo("Perro")
    raiz.si.no = Nodo("Gato")
    raiz.no = Nodo("¿Es un objeto?")
    raiz.no.si = Nodo("Teléfono")
    raiz.no.no = Nodo("¿Es un personaje?")
    raiz.no.no.si = Nodo("¿Es animado?")
    raiz.no.no.si.si = Nodo("Rayo Mcqueen")
    raiz.no.no.si.no = Nodo("Iron Man")

    while True:
        print("\nMenú:")
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Exportar Recorrido del Árbol")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            jugar_juego(raiz)
            jugar_de_nuevo(raiz)
        elif opcion == '2':
            mostrar_instrucciones()
        elif opcion == '3':
            exportar_recorrido(raiz)
            print("El recorrido del árbol se ha exportado exitosamente.")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
