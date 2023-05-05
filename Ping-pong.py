from pygame import*
#importando las clases(area de clase)
class GameSprite (sprite.Sprite):
    #constructor de la clase
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        #inicializando las propiedades del objeto
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        #cada objeto debe tener la propiedad rect(rectangulo donde esta)
        self.rect= self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
#creando la clase heredera(player)
class Player(GameSprite):
    #metodo para controlar el objeto on las teclas
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<wn_height-80:
            self.rect.y += self.speed
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<wn_height-80:
            self.rect.y += self.speed
#escena del videojuego
wn_height = 500
wn_width = 600
background = (200,255,255)
wn = display.set_mode((wn_width,wn_height))
wn.fill(background)
#banderas responsables del juego
game = True
finish = False
clock = time.Clock()
FPS = 60
#cargando fuentes en nuestro programa
font.init()
font1 = font.Font(None,35)
lose1 = font1.render("Jugador 1 pierde",True,(180,0,0))
lose2 = font1.render("Jugador 2 pierde",True,(180,0,0))
#creando los elementos de los jugadores
racket1 = Player('racket.png',30,200,50,150,4)
racket2 = Player('racket.png',520,200,50,150,4)
ball = GameSprite('tenis_ball.png',200,200,50,50,4)
speed_x = 3
speed_y = 3
#ciclo principal del juego
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        wn.fill(background)
        racket1.updateL()
        racket2.updateR()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= -1
            #si la pelota pega en las paredes de arriba y abajo
        if ball.rect.y > wn_height-50 or ball.rect.y < 0:
            speed_y*= -1
        #si la pelota choca izquierda o derecha
        if ball.rect.x > wn_width-50:
            finish = True
            wn.blit(lose2,(200,200))
        if ball.rect.x < 0:
            finish = True
            wn.blit(lose1,(200,200))



        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)

