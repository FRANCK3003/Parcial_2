import pygame.font
from configuraciones import *
from botones import *
from logica import *
import pygame
import json
# Inicializamos pygame Y el mixer
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
# RESOLUCION

screen = pygame.display.set_mode(size_screen)
#----------------------------------------

#----------------------------------------



# FONDO DE MENUS Y SUBMENUS
explosion = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/explosion.png",(20,20))
fondo_main_menu = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_bordo.png",size_screen)
fondo_niveles = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_selector_nivel.png",size_screen)
fondo_jugar = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/imagen_fondo_jugar.png",size_screen)
fondo_puntaje = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_puntaje.png",size_screen)
# MUSICA
musica = pygame.mixer.music.load("JUEGO_EN_CONJUNTO/assets/Toxicity.mp3")
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.05)

fuente = pygame.font.Font("JUEGO_EN_CONJUNTO/assets/fuente_texto.otf",25)



# -------------------------------------------------------------------------------------------------------------------------------

# BOTONES MENU

boton_jugar = crear_boton((565,300,150,37), (20,149,216), 'Jugar', (123,1,123))
boton_ver_puntajes = crear_boton((565,400,150,37), (20,149,216), 'Ver Puntaje', (123,1,123))
boton_salir = crear_boton((565,500,150,37), (20,149,216), 'Salir', (123,1,123))
boton_volver = crear_boton((1000,600,150,37),(20,149,216),'Volver',(123,1,123))

sysfuente = pygame.font.SysFont("Arial",37)

#---------------------------------------------------------------------------------------------------------------------------------



def niveles():
    boton_facil = crear_boton((570,150,150,37), ("white"), 'FACIL', (123,1,123))
    boton_medio = crear_boton((570,335,150,37), ("white"), 'MEDIO', (123,1,123))
    boton_dificil = crear_boton((570,540,150,37), ("white"), 'DIFICIL', (123,1,123))
    boton_siguiente = crear_boton((950,500,250,37),(20,149,216),'EMPEZAR PARTIDA',(123,1,123))
    # por default en facil
    retorno = 8,8,10
    flag = True
    while flag:
        screen.blit(fondo_niveles,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                flag = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_facil['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    retorno = 8,8,10

                if boton_medio['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    retorno = 16,16,40
                
                if boton_dificil['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    retorno = 16,30,100
                
                if boton_volver['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    flag = False
                    menu()
                if boton_siguiente['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    flag = False
                    jugar(retorno)
        
        animacion_boton(screen,boton_facil,fuente,'boton_rec',boton_facil['color'],0,("black"))
        animacion_boton(screen,boton_medio,fuente,'boton_rec',boton_medio['color'],0,("black"))
        animacion_boton(screen,boton_dificil,fuente,'boton_rec',boton_dificil['color'],0,("black"))
        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        animacion_boton(screen,boton_siguiente,fuente,'boton_rec',boton_volver['color'],20,("white"))
        pygame.display.update()


def tablilla_buscaminas(dificultad):
    matriz = inicializar_matriz(dificultad[0],dificultad[1])
    bombas = crear_bombas(dificultad[2],matriz)
    cargar_bomba(matriz,bombas)
    detectar_bombas(matriz,bombas)
    return matriz

def jugar(dificultad):
    fuente_matriz = pygame.font.SysFont('arial black',24)
    matriz = tablilla_buscaminas(dificultad)
    juego = crear_botones_matriz(matriz,170,150)
    #------------------------------------------------
    mi_evento = pygame.USEREVENT + 1
    un_segundo = 1000
    pygame.time.set_timer(mi_evento,un_segundo)

    contador_segundos = 0
    contador_minutos = 0
    #------------------------------------------------
    flag = True
    while flag:
        screen.blit(fondo_jugar,(0,0))
        
        if contador_minutos == 0:
            relog_contador = fuente_matriz.render(f"Time: {contador_segundos}",True,"white","black")
        else:
            relog_contador = fuente_matriz.render(f"Time: {contador_minutos} : {contador_segundos}",True,"white","black")
        
        for boton in juego:
            animacion_cacilla(screen,boton,fuente_matriz,'boton_rec',(150, 150, 150),0,'white',explosion)
        
        for event in pygame.event.get():
            if event.type == mi_evento:
                contador_segundos += 1
                if contador_segundos == 60:
                    contador_minutos += 1
                    contador_segundos = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for boton in juego:
                    if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                        boton['evento'] = True
                
                if boton_volver['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    flag = False
                    niveles()
        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        screen.blit(relog_contador,(1000,100))
        pygame.display.update()

def guardar_archivo_json(ruta:str, dato:any):
    with open(ruta,"w") as archivo:
        json.dump(dato,archivo,indent=4)


def ver_puntajes():
    nombre_ingresado = ""
    nombre_usuario = fuente.render(nombre_ingresado,True,"black")
    
    flag = True
    while flag:
        screen.blit(fondo_puntaje,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                flag = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[0:-1]
                else:
                    nombre_ingresado += event.unicode
                nombre_usuario = fuente.render(nombre_ingresado,True,"black")
        
        print(nombre_ingresado)
        
        screen.blit(nombre_usuario,(1000,400))
        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        pygame.display.update()
    menu()


def menu():
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
            # animacion_boton(screen,boton_niveles,fuente,'boton_rec',boton_niveles['color'],20,("white"))
            animacion_boton(screen,boton_jugar,fuente,'boton_rec',boton_jugar['color'],20,("white"))
            animacion_boton(screen,boton_ver_puntajes,fuente,'boton_rec',boton_ver_puntajes['color'],20,("white"))
            animacion_boton(screen,boton_salir,fuente,'boton_rec',boton_salir['color'],20,("white"))
        # actualiza la pantalla
        pygame.display.flip()

        clock.tick(60)
    # Salgo de pygame
    pygame.quit()

menu()
