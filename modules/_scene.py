import pygame
import pygame.locals as v
import sys
from _scene_types import *

SIZE_IPHONE = (320, 480)
SIZE_IPHONE4 = (320, 480)
SIZE_IPHONE5 = (320, 568)
size = SIZE_IPHONE4

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pythonista scene emulator")

BACKGROUND_COLOR = (0, 0, 0)
TINT_COLOR = (0, 0, 0)
FILL_COLOR = (0, 0, 0)
GRAVITY    = (0, 0, 0)
STROKE_WIDTH = 0

def text(txt, font_name, font_size, x, y, alignment):
    screen.blit(pygame.font.SysFont("Ubuntu Mono", 14).render(txt, 1, TINT_COLOR), (x, y))

def gravity():
    return GRAVITY

def background(r, g, b):
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = (r*255., g*255., b*255.)

def blend_mode(): pass

def ellipse(x, y, w, h):
    pygame.draw.ellipse(screen, FILL_COLOR, (x, y, w, h))

def stroke_weight(line_width):
    """
    stroke_weight(line_width) -- Set the current stroke weight (line
        width) for drawing rectangles and ellipses.
    """
    global STROKE_WIDTH
    STROKE_WIDTH = line_width

def no_stroke():
    """
    no_stroke() -- Disable drawing outlines for rectangles and ellipses.
    """
    stroke_weight(0)

def no_fill(): pass
def no_tint(): pass

def push_matrix(): pass
def pop_matrix(): pass
def rotate(deg):
    """
    rotate(deg) -- Rotate the current transformation matrix
    (affects following drawing operators).
    """
    pass

def translate(tx, ty):
    """
    translate(tx, ty) -- Translate the current transformation martix
    (affects following drawing operators).
    """
    pass

def scale(): pass
def load_image(): pass
def image(name, x, y, w, h):
    img = pygame.image.load("app/Textures/%s.png" % name)
    screen.blit(img, (x, y))

def rect(x, y, w, h):
    pygame.draw.rect(screen, FILL_COLOR, (x, y, w, h))

def fill(r, g, b, a=1.0):
    global FILL_COLOR
    FILL_COLOR = (r*255., g*255., b*255.)

def stroke(r, g, b): pass
def tint(r, g, b, a=1):
    global TINT_COLOR
    TINT_COLOR = (r*255, g*255, b*255)

def get_image_path(): pass
def load_image_file(): pass
def line(): pass
def get_screen_scale(): pass
def unload_image(): pass
def image_quad(): pass

def randid():
    return "0x00"

def run(scene_obj, orientation, frame_interval, anti_alias):
    fps = 60*frame_interval
    clock = pygame.time.Clock()
    scene_obj._setup_scene(*size)
    mouse_pressed = False
    id = randid()
    touch = Touch(0, 0, 0, 0, id)
    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == v.QUIT:
                scene_obj._stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
                x, y = event.pos
                scene_obj._touch_began(x, y, id)
                prev = (x, y)

            elif event.type == v.MOUSEMOTION and mouse_pressed:
                x, y = event.pos
                id = randid()
                scene_obj._touch_moved(x, y, prev[0], prev[1], id)

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False
                x, y = event.pos
                id = randid()
                scene_obj._touch_ended(x, y, id)

        scene_obj._draw(0)
        pygame.display.flip()
        clock.tick(fps)
