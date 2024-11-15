import pygame
import spritesheet

pygame.init()

SCREEEN_WIDTH = 1000
SCREEEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEEN_WIDTH, SCREEEN_HEIGHT))
pygame.display.set_caption("spriteyay")

run = True

BG = (50, 50, 50)
BLACK = (0, 0, 0)

sprite_img = pygame.image.load(
    "./anim/img/sheets/DinoSprites - doux.png"
).convert_alpha()

sprite_sheet = spritesheet.SpriteSheet(sprite_img)


# NOW IN spritesheet class
# def get_image(sheet, frame, width, height, scale, color):
#     image = pygame.Surface((width, height)).convert_alpha()
#     image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
#     image = pygame.transform.scale(image, (width * scale, height * scale))
#
#     # makes the specific color in the image transparent, since the background is black, that is made transparent
#     image.set_colorkey(color)
#
#     return image
#     pass


frame0 = sprite_sheet.get_image(0, 24, 24, 5, BLACK)
frame1 = sprite_sheet.get_image(1, 24, 24, 5, BLACK)
frame2 = sprite_sheet.get_image(2, 24, 24, 5, BLACK)
frame3 = sprite_sheet.get_image(3, 24, 24, 5, BLACK)

# animaion list - holds all frames to loop through
animation_list = []

# number of frames to loop through
animation = 4

# timer to change each frame
last_update = pygame.time.get_ticks()
animation_cooldown = 500  # in ms

frame = 0


# append all frames to animation list
for x in range(animation):
    animation_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

while run:

    screen.fill(BG)

    # # to display sprite sheet
    # screen.blit(sprite_img, (0, 0))

    # update animation
    current = pygame.time.get_ticks()
    if current - last_update >= animation_cooldown:
        frame = (frame + 1) % animation
        last_update = current

    screen.blit(animation_list[frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
