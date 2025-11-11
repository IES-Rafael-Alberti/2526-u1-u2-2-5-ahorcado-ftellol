"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Fabio Tello Lopez
Fecha: 06/11/2025
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns
    -------
    str
        La palabra a adivinar en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la palabra sea válida
    # - Verificar que tenga al menos 5 caracteres (len())
    # - Verificar que solo contenga letras (isalpha())
    # - Convertir a mayúsculas (upper())

    palabra = str(input("Introduce la palabra a adivinar (mínimo 5 letras): "))

    while len(palabra) < 5 or not palabra.isalpha():
        if len(palabra) < 5:
            print ("Error: La palabra debe tener al menos 5 caracteres.")
            palabra = str(input("Introduce la palabra a adivinar (mínimo 5 letras): "))
        elif not palabra.isalpha():
            print("Error: La palabra solo puede contener letras.")
            palabra = str(input("Introduce la palabra a adivinar (mínimo 5 letras): "))

    palabra = palabra.upper()

    return palabra


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Parameters
    ----------
    letras_usadas : list
        Lista de letras ya introducidas
        
    Returns
    -------
    str
        La letra introducida en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida
    # - Verificar que sea solo un carácter (len() == 1)
    # - Verificar que sea una letra (isalpha())
    # - Verificar que no esté en letras_usadas (operador 'in')
    # - Convertir a mayúsculas (upper())

    letra = str(input("Dime una letra: "))
    letra = letra.upper()

    while not letra.isalpha() or len(letra) != 1 or letra in letras_usadas:
        if not letra.isalpha():
            print ("¡Letra incorrecta!, no es una letra")
            letra = str(input("Dime una letra: "))
            letra = letra.upper()
        elif len(letra) != 1:
            print ("¡Letra incorrecta!, solo se puede introducir una letra")
            letra = str(input("Dime una letra: "))
            letra = letra.upper()
        elif letra in letras_usadas:
            print ("¡Letra incorrecta!, esta letra ya ha sido usada")
            letra = str(input("Dime una letra: "))
            letra = letra.upper()

    letras_usadas.append(letra)

    return letra


def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Parameters
    ----------
        palabra_oculta : str
            La palabra con _ y letras adivinadas
        intentos : int
            Número de intentos restantes
        letras_usadas : list
            Lista de letras ya usadas
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes
    # - Imprimir la palabra con espacios entre caracteres
    # - Imprimir las letras usadas

    print ("Intentos restantes:", intentos)
    print (palabra_oculta)
    print ("Letras usadas", letras_usadas)



def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Parameters
    ----------
        palabra : str
            La palabra completa a adivinar
        palabra_oculta : str
            La palabra actual con _ y letras adivinadas
        letra : str
            La letra que se ha adivinado
        
    Returns
    -------
        str
            La palabra oculta actualizada
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string

    lista_palabra = list(palabra_oculta)

    for indice, caracter in enumerate(palabra):
        if caracter == letra:
            lista_palabra[indice] = letra

    palabra_oculta = "".join(lista_palabra)

    return palabra_oculta


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # TODO: Solicitar la palabra al jugador 1
    # palabra = solicitar_palabra()
    
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    # limpiar_pantalla()
    
    # TODO: Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False

    palabra = solicitar_palabra()
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo
    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta


    limpiar_pantalla()

    intentos = 0
    longitud = len(palabra)
    palabra_oculta = "_" * longitud
    palabra_oculta = " ".join(palabra_oculta)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False

    while not juego_terminado and intentos > 0:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)

        acierto = False
        for i in range(longitud):
            if palabra [i] == letra:
                posicion = i * 2
                palabra_oculta = palabra_oculta[:posicion] + letra + palabra_oculta[posicion + 1:]
                acierto = True

        if not acierto:
                intentos -= 1
                print ("¡Letra incorrecta!")
        else:
            print("¡Bien! La letra", letra, "está en la palabra.")

        if "_" not in palabra_oculta:
                juego_terminado = True
                print ("¡FELICIDADES! Has adivinado la palabra:", palabra)

    if not juego_terminado:
        print ("\n💀 Te has quedado sin intentos.")
        print ("La palabra correcta era:", palabra)


def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == "s" :
        main()


if __name__ == "__main__":
    main()
