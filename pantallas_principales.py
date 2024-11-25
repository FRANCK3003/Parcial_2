import pygame
from botones import *



def ver_puntajes():

    sysfuente = pygame.font.SysFont("Arial black",37)
    fondo_puntaje = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/Fondo_puntaje.png",size_screen)
    boton_volver = crear_boton((1000,550,150,37),(20,149,216),'Volver',(123,1,123))
    
    nombre_ingresado = ""
    try:
        lista_score = cargar_json("JUEGO_EN_CONJUNTO/Player score/player_score.json")
    except:
        guardar_archivo_json("JUEGO_EN_CONJUNTO/Player score/player_score.json",[])

    lista_score = cargar_json("JUEGO_EN_CONJUNTO/Player score/player_score.json")
    nombre_usuario = sysfuente.render(nombre_ingresado,True,"black")

    
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
                nombre_usuario = sysfuente.render(nombre_ingresado,True,"black")
        
        
        
        screen.blit(nombre_usuario,(1000,400))
        animacion_boton(screen,boton_volver,fuente,'boton_rec',boton_volver['color'],20,("white"))
        pygame.display.update()
    print(nombre_ingresado)
    lista_score.append(nombre_ingresado)
    
    score_points = guardar_archivo_json("JUEGO_EN_CONJUNTO/Player score/player_score.json", lista_score)
    print(score_points)
    menu()


# ---------------------------------------------------------


def jugar(dificultad):
    fondo_jugar = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/imagen_fondo_jugar.png",size_screen)
    explosion = escalar_imagenes_fondo("JUEGO_EN_CONJUNTO/assets/explosion.png",(20,20))
    boton_volver = crear_boton((1000,550,150,37),(20,149,216),'Volver',(123,1,123))
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