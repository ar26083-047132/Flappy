import pygame, sys

def draw_bg():
    screen.blit(bg_surface,(bg_x_pos, 0))
    screen.blit(bg_surface,(bg_x_pos + size_win_x, 0))
def draw_floor():
        screen.blit(floor_surface,(floor_x_pos, 900))
        screen.blit(floor_surface,(floor_x_pos + size_win_x, 900))

pygame.init()

size_win_x = 576
size_win_y = 1024

#Gama Varibles
gravity= 0.25
bird_movement = 0
screen = pygame.display.set_mode((size_win_x, size_win_y)) #576, 1024

clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0
bg_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("flap")
                bird_movement = 0
                bird_movement -=12
        if event.type == SPAWNPIPE:
            print("spawn pipe")
    draw_bg()
    if bg_x_pos < -575:
        bg_x_pos = 0

    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    bg_x_pos -= 0.25
    draw_floor()
    if floor_x_pos < -575:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)