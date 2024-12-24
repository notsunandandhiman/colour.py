import pygame 
import random

pygame.init()


SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2



BLUE = pygame.Color('blue')
LIGHT = pygame.Color('lightblue')
RED = pygame.Color('red')
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
GREY = pygame.Color('grey')


class Sprite1(pygame.sprite.Sprite):


    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1])]


    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKROUND_COLOR_CHANGE_EVENT))


    def change_color(self):
        self.image.fill (random.choice([YELLOW, GREY, GREEN, WHITE]))
    


        def change_backround_colour():
        global bg_colour
        bg_colour = random.choice([BLUE, BLACK , RED])


        all_sprites_list = pygame.sprite.Group()

        sp1 = Sprite1(WHITE, 20 , 30)

        sp1.rect.x = random.randint(0, 480)
        sp1.rect.y = random.randint(0, 370)

        all_sprites_list.add(sp1)
        
        screen = pygame.display.set_mode((500, 400))

        pygame.display.set_caption("Colourful Bounce")
        bg_colour =BLUE
        clock = pygame.time.Clock()

        while not exit:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit = True
                    
                elif event.type == SPRITE_COLOR_CHANGE_EVENT:
                    sp1.change_color()
                elif event.type == BACKROUND_COLOR_CHANGE_EVENT:
                    change_backround_colour()
                    while not exit:
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                exit = True
                elif event.type == SPRITE_COLOR_CHANGE_EVENT:
                    sp1.change_color()
                elif event.type == BACKROUND_COLOR_CHANGE_EVENT:
                    change_backround_colour()

        all_sprites_list.update()

        screen.fill(bg_colour)

        all_sprites_list.draw(screen)

        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(240)
        



            

