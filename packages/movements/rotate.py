import pygame
from packages.limitations.limit_boundary import check_bound

def rotate_obj(screen, image, offset, coor, degree):
    temp_img = pygame.transform.rotate(image, degree)
    size = (temp_img.get_width(), temp_img.get_height())
    coor, degree, delay = check_bound((screen.get_width(), screen.get_height()), 
                                         offset, coor, size, degree)

    img = pygame.transform.rotate(image, degree)
    screen.blit(img, coor)

    return img, coor, degree, delay

