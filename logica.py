import random

def inicializar_matriz(cant_filas:int, cant_columnas:int)->list:
    """
    Crea una matriz de dimensiones especificadas, inicializada con ceros.

    Parámetros:
    cant_filas (int): Número de filas de la matriz.
    cant_columnas (int): Número de columnas de la matriz.

    Retorna:
    list: Una matriz donde todos los elementos están inicializados a 0.
    """
    matriz = []
    for _ in range(cant_filas):
        matriz += [[0] * cant_columnas]
    return matriz


def crear_bombas(cantidad,matriz):
    """
    Genera un conjunto de coordenadas aleatorias para colocar bombas en una matriz.

    Parámetros:
    cantidad (int): Número de bombas a colocar.
    matriz (list): La matriz que define el espacio donde se colocarán las bombas.
    
    Retorna:
    set: Un conjunto de tuplas con las bombas . Las posiciones son únicas.
    """
    lista_bombas = set()
#  y fila , x columna
    while cantidad > len(lista_bombas):
        y = random.randint(0,len(matriz)-1) 
        x = random.randint(0,len(matriz[0])-1) 

        lista_bombas.add((y,x))

    return lista_bombas


def cargar_bomba(matriz, lista_bombas):
    """
    Coloca las bombas en una matriz modificando las posiciones indicadas.

    Parámetros:
    matriz (list): La matriz en la que se colocarán las bombas. como valor  `-1`.
    lista_bombas (set): Un conjunto de tuplas, donde cada tupla representa las coordenadas de una bomba a colocar en la matriz.

    Retorna:
    None: La función modifica la matriz proporcionada directamente.
    """
    for y,x in lista_bombas:
        matriz[y][x] = -1

#                               Lista de seters
def detectar_bombas(matriz,lista_bombas):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for y,x in lista_bombas:
        
        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
            ]
        
        
        for dy, dx in direcciones:
            ny, nx = y + dy, x + dx
            # Verificar que no salga de los límites
            # evitamos index error sin try except

            if 0 <= ny < filas and 0 <= nx < columnas:
                # Incrementar solo si no es una bomba
                
                if matriz[ny][nx] != -1:
                    matriz[ny][nx] += 1



def parseo_dato(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz)):
            matriz[y][x] = str(matriz[y][x])


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:^1}',end=" ")
        print(" ")


# def detectar_x(boton):
#     filas = len(matriz)
#     columnas = len(matriz[0])
    
        
#         direcciones = [
#             (-1, -1), (-1, 0), (-1, 1),
#             (0, -1),          (0, 1),
#             (1, -1), (1, 0), (1, 1)
#             ]
        
        
#         for dy, dx in direcciones:
#             if boton['texto'] == 0
#             # Verificar que no salga de los límites
#             # evitamos index error sin try except

#             if 0 <= ny < filas and 0 <= nx < columnas:
#                 # Incrementar solo si no es una bomba
                
#                 if matriz[ny][nx] != -1:
#                     matriz[ny][nx] += 1