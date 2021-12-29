#
#Written by: Abhijeet Ingle
#Credits:Joma Tech Youtube Channel
#        Andy Sloane(Author of the original project in C)
          
import pygame
import math

pygame.init()

white_color = (255, 255, 255)
black_color = (0, 0, 0)
hue = 0

WIDTH = 1900
HEIGHT = 1080

x_start, y_start = 0, 0

xSpace = 10
ySpace = 20

rows = HEIGHT // ySpace
columns = WIDTH // xSpace
total_screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0  

theta_spacing = 10
phi_spacing = 1  

donut_fillers = "0123456789!?"  # luminance index

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, white_color)
    display_surface.blit(text, (x_start, y_start))



run = True
while run:

    screen.fill((black_color))

    z = [0] * total_screen_size  
    b = [' '] * total_screen_size  

    for j in range(0, 628, theta_spacing):  # from 0 to 360 degrees
        for i in range(0, 628, phi_spacing):  # from 0 to 360 degrees
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)


            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))


            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = donut_fillers[N if N > 0 else 0]

    if y_start == rows * ySpace - ySpace:
        y_start = 0

    for i in range(len(b)):
        A += 0.00002  #
        B += 0.00001  
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += xSpace
        else:
            y_start += ySpace
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += xSpace

    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
