import pygame

screenSize = (800,600)

pygame.init()
pygame.font.init()
gameDisplay = pygame.display.set_mode((screenSize[0],screenSize[1]))
pygame.display.set_caption('Function Visualizer')
clock = pygame.time.Clock()



class Menu:
    done = False
    colors = {"white":(255,255,255),"black":(0,0,0),"red":(255,0,0)}
    menuFont = pygame.font.SysFont('Times New Roman', 30)
    titleFont = pygame.font.SysFont('Times New Roman', 50)
    def __init__(self, menuType, numButtons,bgColor,buttonColor,messages,title):
        self.menuType = menuType
        self.numButtons = numButtons
        self.bgColor = bgColor
        self.buttonColor = buttonColor
        self.messages = messages
        self.title = title
        self.buttons = []
    
    def drawBackground(self):
        gameDisplay.fill(self.colors[self.bgColor])

    def drawText(self,text,xCoord,yCoord):
        textsurface = self.menuFont.render(text, False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(xCoord, yCoord))
        gameDisplay.blit(textsurface,text_rect)

    def drawTitle(self,title):
        textsurface = self.menuFont.render(title, False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(screenSize[0]*0.5, screenSize[1]*0.1))
        gameDisplay.blit(textsurface,text_rect)
    
    def drawButtons(self,text):
        count = 1
        xCoord = screenSize[0] * 0.5
        for message in self.messages:
            yCoord = 0 + (screenSize[1]/len(self.messages)) * count
            button = pygame.Rect(xCoord - 25, yCoord - 25, 50, 50)
            self.buttons.append(button)
            #textsurface = self.menuFont.render(message, False, (255, 255, 255))
            count += 0.5
            #text_rect = textsurface.get_rect(center=(xCoord, yCoord))
            pygame.draw.rect(gameDisplay, [255, 0, 0], button)
            self.drawText(message,xCoord,yCoord)
            #gameDisplay.blit(textsurface,text_rect)
            pygame.display.update()
        count = 0

    def testfunction(self):
        self.drawBackground()
        self.drawButtons(1)
        self.drawTitle(self.title)
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    clicked_buttons = [s for s in self.buttons if s.collidepoint(mouse_pos)]
                    print(clicked_buttons)
                    print(self.buttons.index(clicked_buttons[0]))
                    
                    

            pygame.display.update()
            clock.tick(60)


#carImg = pygame.image.load('racecar.png')
#gameDisplay.blit(carImg, (x,y))

mylist = ["hello","asdasdad","asfasdasd","asdasdgre"]

x  = Menu("main",4,"black","red",mylist,"Pick a function")

x.testfunction()