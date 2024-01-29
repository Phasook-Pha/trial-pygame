import random
import pygame

def import_img(path, size):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)
    return img

def draw_img(img_size, offset, mode, rgb, prop):
    surface = pygame.Surface(img_size, pygame.SRCALPHA, 32)
    #surface = pygame.Surface(img_size, 0, 32)
    if mode == 'rect' or mode == 'poly' or mode == 'elli':
        ori_x = offset[0]
        ori_y = offset[1]
        size_x = img_size[0] - (offset[0] * 2)
        size_y = img_size[1] - (offset[1] * 2)
        if mode == 'rect':
            img = pygame.draw.rect(surface, rgb, (ori_x, ori_y, size_x, size_y), width = prop)
        elif mode == 'poly':
            coor_num = random.randint(5, 12)      # Randomize the amount of connected coordinates
            coors = []
            for index in range(0, coor_num):
                coor_x = random.randint(ori_x, size_x)
                coor_y = random.randint(ori_y, size_y)
                coors.append((coor_x, coor_y))
            img = pygame.draw.polygon(surface, rgb, coors, width = prop)
        elif mode == 'elli':
            img = pygame.draw.ellipse(surface, rgb, (ori_x, ori_y, size_x, size_y), width = prop)
        else:
            surface = None
    elif mode == 'circ':
        ori_x = img_size[0] // 2
        ori_y = img_size[1] // 2
        if mode == 'circ':
            min_offset = min(offset)
            min_size  = min(img_size)
            radius = (min_size - min_offset) // 2
            img = pygame.draw.circle(surface, rgb, (ori_x, ori_y), radius, width = prop)
        else:
            surface = None
    else:
        surface = None
    return surface
