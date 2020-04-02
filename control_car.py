import pygame
from gpiozero import LED
pygame.init()
pygame.display.set_mode()
forward = LED(5)
back = LED(6)
left = LED(13)
right = LED(19)
speed = LED(2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                forward.on()
            if event.key == pygame.K_DOWN:
                back.on()
            if event.key == pygame.K_LEFT:
                left.on()
            if event.key == pygame.K_RIGHT:
                right.on()
            if event.key == pygame.K_SPACE:
                speed.on()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                forward.off()
            if event.key == pygame.K_DOWN:
                back.off()
            if event.key == pygame.K_LEFT:
                left.off()
            if event.key == pygame.K_RIGHT:
                right.off()
            if event.key == pygame.K_SPACE:
                speed.off()
