import pygame
pygame.init()
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
