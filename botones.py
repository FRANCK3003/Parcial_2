import pygame
import json
from logica import *
from configuraciones import *
pygame.init()
fuente = pygame.font.Font("JUEGO_EN_CONJUNTO/assets/fuente_texto.otf",25)

screen = pygame.display.set_mode(size_screen)
modelo = {
    'boton':None,
    'color':None,
    'texto':None,
    'texto_color':None,
    'sombra':None,
            }


def pintar_centrar_texto(screen,text_render:str,text_rect):
    screen.blit(text_render,(text_rect.x+(text_rect.width - text_render.get_width())/2,text_rect.y+(text_rect.height - text_render.get_height())/2))


def escalar_imagenes_fondo (direc_imagen,tamanio):
    imagen = pygame.image.load(direc_imagen)
    imagen = pygame.transform.scale(imagen,(tamanio))
    return imagen


def crear_boton(boton_rec,color_rec,texto,texto_color):
    boton = {}
    boton_rectangulo = pygame.rect.Rect(boton_rec)
    boton['boton_rec'] = boton_rectangulo
    boton['color'] = color_rec
    boton['texto'] = texto
    boton['texto_color'] = texto_color
    boton['sombra'] = pygame.Rect.copy(boton_rectangulo)
    boton['evento'] = False
    return boton


def animacion_boton(screen, boton:dict,fuente, parametro, color, borde,texto_color):
    if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color, boton[parametro].move(5,5).inflate(0,0),border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,texto_color)
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'].move(5,5))
    else:
        pygame.draw.rect(screen, color, boton[parametro],border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,boton['texto_color'])
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'])


def animacion_cacilla(screen, boton:dict,fuente, parametro, color, borde,texto_color,imagen):
    if boton['evento'] == True and boton['texto'] == "-1":
        screen.blit(imagen,(boton['boton_rec'].x,boton['boton_rec'].y))
    
    elif boton['evento'] == True:
        pygame.draw.rect(screen, color, boton[parametro],border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,texto_color)
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'])
    else:
        pygame.draw.rect(screen, boton['color'], boton[parametro],border_radius=borde)




def tablilla_buscaminas(dificultad):
    matriz = inicializar_matriz(dificultad[0],dificultad[1])
    bombas = crear_bombas(dificultad[2],matriz)
    cargar_bomba(matriz,bombas)
    detectar_bombas(matriz,bombas)
    return matriz



def guardar_archivo_json(ruta:str, dato:any):
    with open(ruta,"w") as archivo:
        json.dump(dato,archivo,indent=4)


def cargar_json(ruta):
    with open(ruta,"r") as archivo:
        datos = json.load(archivo)
    return datos





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


def menu():
    clock = pygame.time.Clock()
    fondo_main_menu = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_bordo.png",size_screen)
    boton_jugar = crear_boton((565,250,150,37), (20,149,216), 'Jugar', (123,1,123))
    boton_ver_puntajes = crear_boton((565,350,150,37), (20,149,216), 'Ver Puntaje', (123,1,123))
    boton_salir = crear_boton((565,450,150,37), (20,149,216), 'Salir', (123,1,123))
    


    flag_main_menu = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if boton_jugar['boton_rec'].collidepoint(pygame.mouse.get_pos()) and flag_main_menu == False:
                    flag_main_menu = True
                    niveles()

                if boton_ver_puntajes['boton_rec'].collidepoint(pygame.mouse.get_pos()) and flag_main_menu == False:
                    flag_main_menu = True
                    ver_puntajes()

                if boton_salir['boton_rec'].collidepoint(pygame.mouse.get_pos()) and flag_main_menu == False:
                    run = False
        
        if flag_main_menu == False:
            screen.blit(fondo_main_menu,(0,0))
            animacion_boton(screen,boton_jugar,fuente,'boton_rec',boton_jugar['color'],20,("white"))
            animacion_boton(screen,boton_ver_puntajes,fuente,'boton_rec',boton_ver_puntajes['color'],20,("white"))
            animacion_boton(screen,boton_salir,fuente,'boton_rec',boton_salir['color'],20,("white"))
        # actualiza la pantalla
        pygame.display.flip()

        clock.tick(60)
    # Salgo de pygame
    pygame.quit()
