import random
from botones import crear_boton

def inicializar_matriz(cant_filas:int, cant_columnas:int)->list:
    matriz = []
    for _ in range(cant_filas):
        matriz += [[0] * cant_columnas]
    return matriz


def crear_bombas(cantidad,matriz):
    lista_bombas = set()


#  y fila , x columna
    while cantidad > len(lista_bombas):
        y = random.randint(0,len(matriz)-1) 
        x = random.randint(0,len(matriz[0])-1) 

        lista_bombas.add((y,x))

    return lista_bombas


def cargar_bomba(matriz, lista_bombas):
    for y,x in lista_bombas:
        matriz[y][x] = -1


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
            if 0 <= ny < filas and 0 <= nx < columnas:
                # Incrementar solo si no es una bomba
                if matriz[ny][nx] != -1:
                    matriz[ny][nx] += 1



def parceo_dato(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz)):
            matriz[y][x] = str(matriz[y][x])


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:^1}',end=" ")
        print(" ")


def crear_botones_matriz(matriz,cordenada_x,cordenada_y):
    cuadricula = []
    for fila in range(len(matriz)):
        cordenada_y +=27
        if fila != 0:
            cordenada_x -= 25 * len(matriz[0])
        for columna in range(len(matriz[0])):
            cordenada_x += 25
            cuadricula.append(crear_boton((cordenada_x,cordenada_y,20,20),(100,100,100),str(matriz[fila][columna]),(100,100,100)))
    
    return cuadricula

# test = inicializar_matriz(16,30)
# lista_bombas = crear_bombas(100,test)
# print(lista_bombas)
# cargar_bomba(test,lista_bombas)
# print(test)
# detectar_bombas(test,lista_bombas)
# print(test)
# mostrar_matriz(test)


# import pygame

# parceo_dato(test)
# fuego = crear_botones_matriz(test)
# pygame.init()
# fuente = pygame.font.SysFont('arial',24)
# screen = pygame.display.set_mode((1280,720))


# run = True
# while run:
#     # recorremos los eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     screen.fill('white')
#     for boton in fuego:
#         animacion_boton(screen,boton,fuente,'boton_rec',(150, 150, 150),0,'white')

#     pygame.display.flip()




