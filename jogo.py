# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Head Soccer!')
info1_screen_duration = 2000  # Duracao da tela de informação
info1_screen_start_time = 0 # Começou o relógio ou não, varíavel que controla isso

info2_screen_duration = 600 # Duracao da segunda tela de informação
 
# Tela de entrada
logo_do_jogo = pygame.image.load('assets/img/5t.png').convert()
logo_do_jogo = pygame.transform.scale(logo_do_jogo, (700, 400))

# Gamescreen
gamescreen = pygame.image.load('assets/img/gamescreen.png').convert()
gamescreen = pygame.transform.scale(gamescreen, (800, 400))

# Personagem 1 (Olha para a esquerda)
personagem1 = pygame.image.load('assets/img/Character01.png').convert_alpha()
personagem1 = pygame.transform.scale(personagem1, (50, 50))

# Personagem 2 (Olha para a direita)
personagem2 = pygame.image.load('assets/img/player02.png').convert_alpha()
personagem2 = pygame.transform.scale(personagem2, (50, 50))

# Gol 1
gol1 = pygame.image.load('assets/img/goalNormal.png').convert_alpha()
gol1 = pygame.transform.scale(gol1, (80, 180))

# Gol 2
gol2 = pygame.image.load('assets/img/goalNormal2.png').convert_alpha()
gol2 = pygame.transform.scale(gol2, (80, 180))

# Bola: imagem + scale
bola = pygame.image.load('assets/img/pickupBall.png').convert_alpha()
bola = pygame.transform.scale(bola, (30, 30))

# Tela de informação
informacao = pygame.image.load('assets/img/info.png').convert()
informacao = pygame.transform.scale(informacao, (700, 400))

# Tela de informação 2
informacao2 = pygame.image.load('assets/img/info2.png').convert()
informacao2 = pygame.transform.scale(informacao2, (700, 400))

#Freeze 
freeze = pygame.image.load('assets/images/pickupBad.png').convert_alpha()
freeze = pygame.transform.scale(freeze, (30, 30))

#Size
size = pygame.image.load('assets/images/pickupSize.png').convert_alpha()
size = pygame.transform.scale(size, (30, 30))

# Clock (determina FPS)
clock = pygame.time.Clock()

# ----- Gera mensagem
gol_fonte = pygame.font.Font ('assets/font/fonte2.ttf', 60)
font = pygame.font.SysFont(None, 25)
start = font.render('press "SPACE" to play', True, (255, 255, 255))

# ----- Função do movimento do jogador 01
class Player1 (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 4) * 3
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0

        self.gravity = 0.5
        self.ta_no_chao = True
        self.jumpforce = -10
        self.jumping = False

        self.pontuacao = 0

        self.frozen = False
        self.frozen_count = 0

        self.sized = False
        self.size_count = 0

    def update (self):

        if self.frozen == False:

            self.rect.x += self.speedx 

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH

            if self.rect.left < 0:
                self.rect.left = 0
            
            if self.ta_no_chao == False and self.jumping == True:
                self.jumping = False
                self.speedy += self.jumpforce 
                self.rect.y += self.speedy

            self.speedy += self.gravity
            self.rect.y += self.speedy

            if self.rect.bottom >= HEIGHT:  
                self.rect.bottom = HEIGHT  
                self.speedy = 0
                self.ta_no_chao = True 
                self.jumping = False

        # Freeze acontece na colisão
        if freeze in todos_sprites and self.rect.colliderect(freeze.rect):
            player2.frozen = True
            player2.frozen_count = pygame.time.get_ticks()
            todos_sprites.remove(freeze)

        if self.frozen and pygame.time.get_ticks() - self.frozen_count > 3000:  
            self.frozen = False
            self.frozen_count = 0 
            todos_sprites.add(freeze) 

        if size in todos_sprites and self.rect.colliderect(size.rect):
            player2.rect.top = 50
            player2.rect.centerx = WIDTH/2
            player2.sized = True
            player2.size_count = pygame.time.get_ticks()
            todos_sprites.remove(size)

        if self.sized == True and pygame.time.get_ticks() - self.size_count > 3000:
            player2.rect.top = HEIGHT - 30
            player2.rect.centerx = (WIDTH / 4) * 3
            self.sized = False
            self.size_count = 0
            todos_sprites.add(size) 

    def reset_position(self):
        #Reseta a bola e recomeca velocidades
        self.rect.centerx = (WIDTH / 4) * 3
        self.rect.bottom = HEIGHT - 10
        player2.rect.centerx = WIDTH / 4
        player2.rect.bottom = HEIGHT - 10

    # ----- Função do movimento do jogador 02
class Player2 (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)
            
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0

        self.gravity = 0.5
        self.ta_no_chao = True
        self.jumpforce = -10
        self.jumping = False

        self.pontuacao = 0
        self.frozen = False

        self.frozen_count = 0

        self.sized = False
        self.size_count = 0

    def update (self):

        if self.frozen == False:

            self.rect.x += self.speedx 

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH

            if self.rect.left < 0:
                self.rect.left = 0
                
            if self.ta_no_chao == False and self.jumping == True:
                self.jumping = False
                self.speedy += self.jumpforce 
                self.rect.y += self.speedy

            self.speedy += self.gravity
            self.rect.y += self.speedy

            if self.rect.bottom >= HEIGHT:  
                self.rect.bottom = HEIGHT  
                self.speedy = 0
                self.ta_no_chao = True 
                self.jumping = False

        # Freeze acontece na colisão
        if freeze in todos_sprites and self.rect.colliderect(freeze.rect):
            player1.frozen = True
            player1.frozen_count = pygame.time.get_ticks() #usar o clock do python
            todos_sprites.remove(freeze) 

        if self.frozen and pygame.time.get_ticks() - self.frozen_count > 3000:  
            self.frozen = False
            self.frozen_count = 0 
            todos_sprites.add(freeze) 

        if size in todos_sprites and self.rect.colliderect(size.rect):
            player1.rect.top = 50
            player1.rect.centerx = WIDTH/2
            player1.sized = True
            player1.size_count = pygame.time.get_ticks()
            todos_sprites.remove(size)

        if self.sized == True and pygame.time.get_ticks() - self.size_count > 3000: 
            player1.rect.top = HEIGHT - 30
            player1.rect.centerx = (WIDTH / 4) * 3
            self.sized = False
            self.size_count = 0 
            todos_sprites.add (size)

    def reset_position(self):
        #Reseta a bola e recomeca velocidades
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT - 10
        player1.rect.centerx = (WIDTH / 4) * 3
        player1.rect.bottom = HEIGHT - 10
    

# ----- Função do movimento da Bola
class Bola (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT / 2
        self.r = 15

        self.speedx = 0  #Velocidade x
        self.speedy = -10  #Velocidade y
        self.aceleracao = 0.5  #Gravidade
        self.restituicao = 0.8  #Perda de energia (restituição)

        self.atravessou = False # fez gol?

    def update (self):
        #Atualiza posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy 

        #Gravidade
        self.speedy += self.aceleracao   

        #Bola não cair da tela, nem passar do teto
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy * self.restituicao #Bater no chão e voltar pra cima
            if abs(self.speedy) < 1: #Não deixar a bola pular para sempre
                self.speedy = 0 #Visto em https://www.reddit.com/r/pygame/s/YYwvxHjkPZ / https://github.com/sk-Prime/simple_pygames

        if self.rect.top <= 0:
            self.rect.top = 0
            self.speedy = -self.speedy * self.restituicao
        
        #Colisões com jogadores
        if player1.rect.colliderect(self.rect):
            self.speedy += player1.speedy * self.restituicao
            self.speedx += player1.speedx * self.restituicao

        if player2.rect.colliderect(self.rect):
            self.speedy += player2.speedy * self.restituicao
            self.speedx += player2.speedx * self.restituicao 

        #Colisões com bordas
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx * self.restituicao

        if self.rect.left <= 0:
            self.rect.left = 0
            self.speedx = -self.speedx * self.restituicao

        #Pontuação
        if self.rect.colliderect(gol1.travessao_rect) or self.rect.colliderect(gol2.travessao_rect):
            self.speedy = -self.speedy  # Faz a bola rebater para cima

        # Verifica se é gol e conta os pontos 
        if (self.rect.right < gol1.rect.right and self.rect.top > gol1.rect.top and not self.atravessou and not self.rect.colliderect(gol1.travessao_rect)):
            player1.pontuacao += 1
            player1.reset_position()
            self.atravessou = True  # Gol valeu
            self.reset_position()

        elif (self.rect.left > gol2.rect.left and self.rect.top > gol2.rect.top and not self.atravessou and not self.rect.colliderect(gol2.travessao_rect)):
            player2.pontuacao += 1
            player2.reset_position()
            self.atravessou = True  # Gol valeu
            self.reset_position()
        
    def reset_position(self):
        #Reseta a bola e recomeca velocidades
        self.rect.centerx = WIDTH / 2
        self.rectbottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = -10
        self.atravessou = False #reseta a variável de gol ou não

class Gol (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT

        self.travessao_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 10) #travessão (rect)

class Gol2 (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 40
        self.rect.bottom = HEIGHT

        self.travessao_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 10) #travessão (rect)

class Freeze (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(180 + 20, WIDTH - 200)
        self.rect.y = random.randint(180 + 70, HEIGHT - 20)

class Size (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(180 + 20, WIDTH - 200)
        self.rect.y = random.randint(180 + 70, HEIGHT - 20)

# ----- Criar o jogador 01 e jogador 02 + add ele em um grupo como do tutorial
player1 = Player1(personagem1)
player2 = Player2(personagem2)
bola = Bola(bola)
gol1 = Gol (gol1)
gol2 = Gol2 (gol2)
freeze = Freeze (freeze)
size = Size (size)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(player1)
todos_sprites.add(player2)
todos_sprites.add(bola)
todos_sprites.add (gol1)
todos_sprites.add (gol2)
todos_sprites.add (freeze)
todos_sprites.add (size)

# ----- Inicia estruturas de dados
game = True
screen = 1
piscar_texto = 0
mostrar = True
nova_time = 0

# ===== Loop principal =====
while game:

    clock.tick(60)

    # ----- Trata eventos

    for event in pygame.event.get():

        # ----- Verifica consequências

        if event.type == pygame.QUIT:
            game = False

        elif event.type == pygame.KEYDOWN:

            # Leva para a segunda tela
            if event.key == pygame.K_SPACE: 
                if screen == 1:
                    screen = "info_screen"
                    info_screen_start_time = pygame.time.get_ticks()  # Marca o tempo atual

            # Personagem 01 Movimento
            # Mexe o personagem 01 para esquerda e direita, adicionando uma velocidade 
            if event.key == pygame.K_LEFT:
                player1.speedx -= 5

            if event.key == pygame.K_RIGHT:
                player1.speedx += 5

            # Pula apenas se o jogador tiver no chão (Player 01)
            if event.key == pygame.K_UP and player1.ta_no_chao == True:
                player1.ta_no_chao = False
                player1.jumping = True 

            # Dash Player 01, quando shift tá apertado e direção apertada
            if event.key == pygame.K_RSHIFT:
                    if player1.rect.x - 20 > 0 and player1.speedx == -5:
                        player1.rect.x -= 50

                    if player1.rect.x + 20 < WIDTH and player1.speedx == +5:
                        player1.rect.x += 50  

            # Personagem 02 Movimento
            # Mexe o personagem 02 para esquerda e direita, adicionando uma velocidade 
            if event.key == pygame.K_a:
                player2.speedx -= 5

            if event.key == pygame.K_d:
                player2.speedx += 5

            # Pula apenas se o jogador tiver no chão (Player 02)
            if event.key == pygame.K_w and player2.ta_no_chao == True:
                player2.ta_no_chao = False
                player2.jumping = True  

            # Dash Player 02, quando q tá apertado e direção apertada
            if event.key == pygame.K_q:
                    if player2.rect.x - 20 > 0 and player2.speedx == -5:
                        player2.rect.x -= 50

                    if player2.rect.x + 20 < WIDTH and player2.speedx == +5:
                        player2.rect.x += 50             
        
        elif event.type == pygame.KEYUP:

            # Controla a velocidade do personagem 1, quando tirar da tecla para de mexer
            if event.key == pygame.K_LEFT:
                player1.speedx += 5
    
            if event.key == pygame.K_RIGHT:
                player1.speedx -= 5
            
            # Controla a velocidade do personagem 2, quando tirar da tecla para de mexer
            if event.key == pygame.K_a:
                player2.speedx += 5

            if event.key == pygame.K_d:
                player2.speedx -= 5 
        
    nova_time += 1

    current_time = pygame.time.get_ticks() # tempo atual (usar a função que conta o tempo do PyGame)

    # Jogadores colidem um com o outro e não passam por cima do outro
    if player1.rect.colliderect(player2.rect):
        player1.rect.x = player1.rect.x + 8
        player2.rect.x = player2.rect.x - 8

    # Código inspirado no https://stackoverflow.com/questions/42472019/flickering-text-in-pygame
    # Texto piscante
    if piscar_texto >= 60: 
        mostrar = not mostrar  
        piscar_texto = 0

    piscar_texto += 1

    # Troca de telas
    if screen == 1:
        # Informação sobre screen 1
        window.fill((255,245,255))  # Preenche com a cor branca
        window.blit(logo_do_jogo, (0, 0))

        # Informações sobre start
        if mostrar:
            window.blit (start, (256, 231))

    elif screen == "info_screen":
        # Tela de informação
        window.fill((0, 0, 0))  # Cor de fundo para a tela de informação
        window.blit(informacao, (0, 0))

    # Verifica se a duração da tela de informação passou
        if (current_time - info_screen_start_time > info1_screen_duration):
            screen = "info2_screen" # Vai para a tela2 de informação após o tempo definido

    elif screen == "info2_screen":
        window.fill((0, 0, 0))  
        window.blit(informacao2, (0, 0))
        if nova_time - 0 > info2_screen_duration:
            screen = 2
            
    elif screen == 2:
        # Informação sobre screen 2
        window.fill((188,143,143))
        window.blit(gamescreen, (-50, 0))
        todos_sprites.draw(window)

        #Pontuação
        rect_x1, rect_y1 = WIDTH - 195, 10   # Rectangle position
        rect_x2, rect_y2 = 95, 10   # Rectangle position
        rect_width, rect_height = 115, 90  # Rectangle size, smaller than the screen

        #pygame.draw.rect (window, (0, 0, 0), (0,230,80,170))
        #pygame.draw.rect (window, (0, 0, 0), (620,230,80,170))

        pygame.draw.rect(window, (0, 0, 0), (rect_x1, rect_y1, rect_width, rect_height))
        pygame.draw.rect(window, (0, 0, 0), (rect_x2, rect_y2, rect_width, rect_height))

        if player1.pontuacao < 10:
            player1_gol_fonte = gol_fonte.render(f"0{player1.pontuacao}", True, (255, 0, 0))
        else:
            player1_gol_fonte = gol_fonte.render(f"{player1.pontuacao}", True, (255, 0, 0))

        if player2.pontuacao < 10:
            player2_gol_fonte = gol_fonte.render(f"0{player2.pontuacao}", True, (255, 0, 0))
        else:
            player2_gol_fonte = gol_fonte.render(f"{player2.pontuacao}", True, (255, 0, 0))
        # Mostrar a pontuação
        window.blit(player1_gol_fonte, (WIDTH - 170, 25))
        window.blit(player2_gol_fonte, (120, 25)) 

        # Update jogadores posição atual
        player1.update()
        player2.update()
        bola.update()
        freeze.update ()
        size.update()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados