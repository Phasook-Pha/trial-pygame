import pygame

from packages.objects.draw import import_img, draw_img
from packages.movements.rotate import rotate_obj
from packages.movements.move_coor import change_coor

pygame.init()

screen_size = (1024, 720)
screen = pygame.display.set_mode(screen_size)

img_size = (300, 200)
offset_size = (10, 5)
color = (0, 120, 0)
width = 2
img = draw_img(img_size, offset_size, 'elli', color, width)
plot_coor = (900, 650)

running = True
angle = 0       # Degree
delay = 100     
while running:
    if delay > 1:
        plot_coor = change_coor(plot_coor, 80)
    else:
        plot_coor = plot_coor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            running = True
    screen.fill((50, 50, 50))
    rotate_img, plot_coor, angle, delay = rotate_obj(screen, img, offset_size, plot_coor, angle)

    pygame.display.update()
    pygame.time.delay(delay)
