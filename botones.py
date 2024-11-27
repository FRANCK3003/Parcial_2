import pygame
from logica import *
from configuraciones import *




def pintar_centrar_texto(screen:pygame.Surface,text_render:str,text_rect:pygame.Rect):
    """centra el texto segun el rectangulo pasado
    Args:
        screen (pygame.Surface):superficie
        text_render (str): _description_
        text_rect (pygame.Rect): _description_
    """
    screen.blit(text_render,(text_rect.x+(text_rect.width - text_render.get_width())/2,text_rect.y+(text_rect.height - text_render.get_height())/2))


def escalar_imagenes_fondo (direc_imagen:str,tamanio:tuple)->pygame.Surface:
    """_summary_

    Args:
        direc_imagen (str): _description_
        tamanio (tuple): _description_

    Returns:
        _type_: _description_
    """    
    imagen = pygame.image.load(direc_imagen)
    imagen = pygame.transform.scale(imagen,(tamanio))
    return imagen


def crear_boton(boton_rec:pygame.Rect,color_rec:tuple,texto:str,texto_color:tuple):
    """ 
    Crea un botón representado como un diccionario, con caracteristicas para dibujar, 
    manejar eventos y sombras.

    Args:
        boton_rec (pygame.Rect): Un objeto Rect o las dimensiones del rectángulo del botón.
        color_rec (tuple): Una tupla que representa el color del botón en formato RGB.
        texto (str): El texto que se mostrará en el botón.
        texto_color (tuple): recive la _ donde esta ubicado.

    Returns:
        dict: un diccionario con las siguiente claves 
            - 'boton_rec': El objeto `pygame.Rect` 
            - 'color': El color del botón.
            - 'texto': El texto mostrado en el botón (str).
            - 'texto_color': El color del texto (tuple).
            - 'evento': Un indicador (bool) que señala si el botón fue activado.
    """    
    boton = {}
    boton_rectangulo = pygame.rect.Rect(boton_rec)
    boton['boton_rec'] = boton_rectangulo
    boton['color'] = color_rec
    boton['texto'] = texto
    boton['texto_color'] = texto_color

    boton['evento'] = False
    return boton

def casilla_juego(boton_rec,color_rec,texto,texto_color,fila,columna):
    """ Crea un botón representado como un diccionario, con caracteristicas para dibujar, 
    manejar eventos y sombras.
    
    args:
        boton_rec (pygame.Rect): Un objeto Rect o las dimensiones del rectángulo del botón.
        color_rec (tuple): Una tupla que representa el color del botón en formato RGB.
        texto (str): El texto que se mostrará en el botón.
        texto_color (tuple): Una tupla que representa el color del texto en formato RGB.
        fila (int): recive la fila donde esta ubicado.
        columna (int): recive la columna donde esta ubicado.

    Returns:
        dict: un diccionario con las siguiente claves 
            - 'boton_rec': El objeto `pygame.Rect` 
            - 'color': El color del botón.
            - 'texto': El texto mostrado en el botón (str).
            - 'texto_color': El color del texto (tuple).
            - 'fila': Un indica fila donde esta ubicada.
            - 'columna': Un indica columna donde esta ubicada.
            - 'clicado': .
            - 'marcado': .

    """
    boton = {}
    boton_rectangulo = pygame.rect.Rect(boton_rec)
    boton['boton_rec'] = boton_rectangulo
    boton['color'] = color_rec
    boton['texto'] = texto
    boton['texto_color'] = texto_color
    boton['evento'] = False
    boton['fila'] = fila
    boton['columna'] = columna
    boton['clicado'] = False
    boton['marcado'] = False

    return boton

def animacion_boton(screen:pygame.surface, boton:dict,fuente:pygame.font.Font, parametro:pygame.Rect, color:tuple, borde,texto_color:tuple):
    """dibuja y renderisa el boton sugun los nuevos parametro dados, sino lo dibuja con las configuraciones(boton)

    Args:
        screen (pygame.surface): superficie en donde lo dibuja
        boton (dict): confuguracion de boton 
        fuente (pygame.font.Font): tipo de fuente
        parametro (pygame.Rect): rectangualo a modificar
        color (tuple): color del boton (tuple)
        borde (int): bordes del boton 
        texto_color (tuple): color del texto
    """
    
    if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color, boton[parametro].move(5,5).inflate(0,0),border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,texto_color)
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'].move(5,5))
    else:
        pygame.draw.rect(screen, color, boton[parametro],border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,boton['texto_color'])
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'])


def animacion_cacilla(screen:pygame.Surface, boton:dict,fuente:pygame.font.Font, parametro:pygame.Rect, color:tuple, borde:int,texto_color:tuple):
    """_summary_

    Args:
        screen (pygame.Surface): _description_
        boton (dict): _description_
        fuente (pygame.font.Font): _description_
        parametro (pygame.Rect): _description_
        color (tuple): _description_
        borde (int): _description_
        texto_color (tuple): _description_
    """

    if boton['evento'] == True:
        pygame.draw.rect(screen, color, boton[parametro],border_radius=borde)
        fuentex = fuente.render(boton['texto'],True,texto_color)
        pintar_centrar_texto(screen,fuentex,boton['boton_rec'])
    else:
        pygame.draw.rect(screen, boton['color'], boton[parametro],border_radius=borde)




# def tablilla_buscaminas(dificultad):
#     matriz = inicializar_matriz(dificultad[0],dificultad[1])
#     bombas = crear_bombas(dificultad[2],matriz)
#     cargar_bomba(matriz,bombas)
#     detectar_bombas(matriz,bombas)
#     return matriz

def tablero(dificultad):
    matriz = inicializar_matriz(dificultad[0],dificultad[1])
    return matriz

def crear_botones_matriz(matriz,cordenada_x,cordenada_y):

    cuadricula = []
    for fila in range(len(matriz)):
        cordenada_y +=27
        if fila != 0:
            cordenada_x -= 25 * len(matriz[0])
        for columna in range(len(matriz[0])):
            cordenada_x += 25
            cuadricula.append(casilla_juego((cordenada_x,cordenada_y,20,20),(100,100,100),str(matriz[fila][columna]),(100,100,100),fila,columna))
    
    return cuadricula


