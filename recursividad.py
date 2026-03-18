def retroceder(historial, pasos):

    # Condicional Inicial
    if pasos == 0 or len(historial) == 0:
        return historial

    pagina = historial.pop()
    print("Retrocediendo desde:", pagina)

    # Detener el programa si llega a aparecer "Error 404" chamo
    if pagina == "Error 404":
        print("Se encontró Error 404. Retroceso detenido.")
        return historial

    # Paso recursivo
    return retroceder(historial, pasos - 1)


# Ejemplo de prueba
historial = [
    "google.com",
    "chat.openai.com",
    "wikipedia.org",
    "Error 404",
    "youtube.com"
]

retroceder(historial, 3)

print("Historial final:", historial)