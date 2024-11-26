import pygame

from botones import *
from cargar_archivo import *



def tabla_puntuaciones(lista_puntaje):
    sysfuente = pygame.font.SysFont("Arial black",37)
    contador = 100
    # while flag:
    for i in lista_puntaje:
        contador += 100

        fuentex = sysfuente.render(f'{i['nombre']}     {i['puntuacion']}',True,'white')
        screen.blit(fuentex,(300,contador))



def ver_puntajes():
    fondo_puntaje = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_puntaje.png",size_screen)
    boton_volver = crear_boton((1000,550,150,37),(20,149,216),'Volver',(123,1,123))
    

    try:
        lista_score = cargar_json("JUEGO_EN_CONJUNTO/Player score/player_score.json")
    except:
        guardar_archivo_json("JUEGO_EN_CONJUNTO/Player score/player_score.json",[])

    lista_score = cargar_json("JUEGO_EN_CONJUNTO/Player score/player_score.json")

    
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

        tabla_puntuaciones(lista_score)

        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        pygame.display.update()
    menu()


# ---------------------------------------------------------
def contadore(fuente,cont_seg,cont_min,):
    if cont_min == 0:
        relog_contador = fuente.render(f"Time: {cont_seg}",True,"white","black")
    else:
        relog_contador = fuente.render(f"Time: {cont_min} : {cont_seg}",True,"white","black")
    screen.blit(relog_contador,(1000,100))


def guardar_puntuacion(puntos_en_pantalla,die,cont_puntos):
    sysfuente = pygame.font.SysFont("Arial black",37)
    you_die_img = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/you_die.png",size_screen)
    lose_music = pygame.mixer.Sound("JUEGO_EN_CONJUNTO/assets/Game Over.mp3")
    

    lose_music.set_volume(0.05)
    boton_volver = crear_boton((1000,600,150,37),(20,149,216),'Volver',(123,1,123))
    
    
    nombre_ingresado = ""


    flag = True
    while flag:
        if die == True:
            lose_music.play()
            screen.blit(you_die_img,(0,0))

        else:
            pass


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_volver['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                    flag = False
                    lose_music.stop()
                    niveles()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cargar_archivo('JUEGO_EN_CONJUNTO/Player score/player_score.json',{"nombre":nombre_ingresado,"puntuacion":cont_puntos})
                    print("uwu")
                elif event.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[0:-1]                                      
                else:
                    nombre_ingresado += event.unicode
        nombre_usuario = sysfuente.render(nombre_ingresado,True,"white")  
        
        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        screen.blit(puntos_en_pantalla,(100,100))
        screen.blit(nombre_usuario,(500,500))


        pygame.display.update()

def jugar(dificultad):
    jugar_music = pygame.mixer.Sound("JUEGO_EN_CONJUNTO/assets/wolf_play.mp3")
    fondo_jugar = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/imagen_fondo_jugar.png",size_screen)
    explosion = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/explosion.png",(20,20))
    
    boton_reiniciar = crear_boton((50,650,150,37),(20,149,216),'Reiniciar',(123,1,123))
    boton_volver = crear_boton((1000,650,150,37),(20,149,216),'Volver',(123,1,123))
    
    fuente_matriz = pygame.font.SysFont('arial black',24)
    matriz = tablilla_buscaminas(dificultad)
    juego = crear_botones_matriz(matriz,170,150)
    
    #------------------------------------------------
    mi_evento = pygame.USEREVENT + 1
    un_segundo = 1000
    pygame.time.set_timer(mi_evento,un_segundo)
    
    contador_segundos = 0
    contador_minutos = 0
    
    contador_puntos = 0
    
    you_die = False
    jugar_music.play()
    jugar_music.set_volume(0.05)
    
    #------------------------------------------------
    flag = True
    while flag:
        if you_die == False:
            
            screen.blit(fondo_jugar,(0,0))
            puntos_en_pantalla = fuente_matriz.render(f"{contador_puntos}",True,"white","black")
            for boton in juego:
                animacion_cacilla(screen,boton,fuente_matriz,'boton_rec',(150, 150, 150),0,'white',explosion)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                    pygame.quit()

                if event.type == mi_evento:
                    contador_segundos += 1
                if contador_segundos  == 60:
                    contador_minutos += 1
                    contador_segundos += 1
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    for boton in juego:
                        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                            boton['evento'] = True
                            
                        if boton['evento'] == True and boton['texto'] == "-1":
                            jugar_music.stop()
                            you_die = True
                            flag = False
                        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()) and not boton['texto'] == "-1":
                            contador_puntos += 1
                
                    if boton_reiniciar['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                        jugar_music.stop()
                        flag = False
                        jugar(dificultad)
                    if boton_volver['boton_rec'].collidepoint(pygame.mouse.get_pos()):
                        jugar_music.stop()
                        flag = False
                        niveles()
                    
            contadore(fuente_matriz,contador_segundos,contador_minutos)
            screen.blit(puntos_en_pantalla,(100,100))
            animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
            animacion_boton(screen,boton_reiniciar,fuente,'boton_rec',boton_reiniciar['color'],20,("white"))
        pygame.display.update()
    guardar_puntuacion(puntos_en_pantalla,you_die,contador_puntos)

# ---------------------------------------------------------

def niveles():
    
    fondo_niveles = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_selector_nivel.png",size_screen)
    boton_volver = crear_boton((1000,550,150,37),(20,149,216),'Volver',(123,1,123))
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

def menu():
    # pygame.mixer.music.load("JUEGO_EN_CONJUNTO/assets/Toxicity.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.05)

    fondo_main_menu = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_bordo.png",size_screen)
    boton_jugar = crear_boton((565,250,150,37), (20,149,216), 'Jugar', (123,1,123))
    boton_ver_puntajes = crear_boton((565,350,150,37), (20,149,216), 'Ver Puntaje', (123,1,123))
    boton_salir = crear_boton((565,450,150,37), (20,149,216), 'Salir', (123,1,123))
    
    menu_music = pygame.mixer.Sound("JUEGO_EN_CONJUNTO/assets/Toxicity.mp3")
    menu_music.play()
    menu_music.set_volume(0.05)
    clock = pygame.time.Clock()


    flag_main_menu = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if boton_jugar['boton_rec'].collidepoint(pygame.mouse.get_pos()) and flag_main_menu == False:
                    flag_main_menu = True
                    menu_music.stop()
                    niveles()

                if boton_ver_puntajes['boton_rec'].collidepoint(pygame.mouse.get_pos()) and flag_main_menu == False:
                    flag_main_menu = True
                    run = False
                    menu_music.stop()
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