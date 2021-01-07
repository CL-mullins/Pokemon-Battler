import pygame



    #Initialize pygame setting

# class Background():
#     def __init__(self, image_file, location):
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location

# BackGround = Background("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/battlebg.png",[0,0])

# (width, height) = (300, 200)
# screen = pygame.display.set_mode((width, height))
# screen.fill([255, 255, 255])
# screen.blit(BackGround.image, BackGround.rect)

bg = pygame.image.load("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/battlebg.png")
background_colour = (255,255,255)
(width, height) = (300, 200)
picture = pygame.transform.scale(bg, (width, height))
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
screen.blit(picture, (0,0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False