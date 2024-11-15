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

# number of frames to loop through - [idle, run, kick, hurt, duck]
animation_total_frames = 12
animation_steps = [3, 7, 3, 4, 7]

# tells what action is dino doing
action = 0

# timer to change each frame
last_update = pygame.time.get_ticks()
animation_cooldown = 100  # in ms
frame = 0

# Nos of frames
# 3 idle
# 7 run
# 2 kick
temp_img_list = []
for x in range(24):
    if x < 3:
        temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

    if x >= 3 and x < 10:
        if x == 3:
            animation_list.append(temp_img_list)
            temp_img_list = []
        temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

    if x >= 10 and x < 13:
        if x == 10:
            animation_list.append(temp_img_list)
            temp_img_list = []
        temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

    if x >= 13 and x < 17:
        if x == 13:
            animation_list.append(temp_img_list)
            temp_img_list = []
        temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

    if x >= 17 and x < 24:
        if x == 17:
            animation_list.append(temp_img_list)
            temp_img_list = []
        temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))

# for animation in animation_steps:
#     temp_img_list = []
#     for x in range(animation):
#         temp_img_list.append(sprite_sheet.get_image(x, 24, 24, 5, BLACK))
#
#     animation_list.append(temp_img_list)

animation_list.append(temp_img_list)


while run:

    screen.fill(BG)

    # # to display sprite sheet
    # screen.blit(sprite_img, (0, 0))

    # update animation  testing
    action =2 
    current = pygame.time.get_ticks()
    if current - last_update >= animation_cooldown:
        frame = (frame + 1) % animation_steps[action]
        last_update = current

    # to test the running animation
    screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
