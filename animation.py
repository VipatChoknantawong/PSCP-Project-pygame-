import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("ChoCho Adventure!")

x = 100
y = 100
width = 40
height = 60
speed = 50
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

""" KEY PRESS """
run = True
while run:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
    # if keys[pygame.K_LEFT]:
    #     left = True
    #     right = False
    # elif keys[pygame.K_RIGHT]:
    #     right = True
    #     left = False
    # else:
    #     right = False
    #     left = False
    #     walkCount = 0
    # # PRESS SPACE
    # if not(isJump):
    #     if keys[pygame.K_SPACE]:
    #         isJump = True
    #         right = False
    #         left = False
    #         walkCount = 0