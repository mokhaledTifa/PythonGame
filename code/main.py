from settings import *
from Snake import Snake
from apple import Apple
class Main:
    def __init__(self):
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('PythonG')
        
        #game object
        self.bg_rects = [pygame.Rect((col + int(row % 2==0) ) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                            for col in range(0,COLS,2) for row in range(ROWS)]
        self.snake = Snake()
        self.apple = Apple(self.snake)

        #timer
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)
    def drow_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rect)
    def input(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] : self.snake.direction= pygame.Vector2(1,0)
        if keys[pygame.K_LEFT] : self.snake.direction= pygame.Vector2(-1,0)
        if keys[pygame.K_UP] : self.snake.direction= pygame.Vector2(0,-1)
        if keys[pygame.K_DOWN] : self.snake.direction= pygame.Vector2(0,1)
    def collision(self):
        #apple
        if self.snake.body[0]==self.apple.pos:
            self.snake.has_eaten = True
             

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type== self.update_event:                    
                   self.snake.update()
            #update
            self.input()
            self.collision()
            #drawing 
            self.drow_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()   
if __name__== '__main__':
    main=Main()
    main.run()