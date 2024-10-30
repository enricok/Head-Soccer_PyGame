# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Head Soccer!')

# Tela de entrada
logo_do_jogo = pygame.image.load('assets/img/5t.png').convert()
logo_do_jogo = pygame.transform.scale(logo_do_jogo, (700, 400))

# Personagem 1
personagem1 = pygame.image.load('assets/img/Character01.png').convert_alpha()
personagem1 = pygame.transform.scale(personagem1, (50, 50))

# Tela principal
gamescreen = pygame.image.load('assets/img/gamescreen.png').convert()
gamescreen = pygame.transform.scale(gamescreen, (800, 400))

# Personagem 2
personagem2 = pygame.image.load('assets/img/player02.png').convert_alpha()
personagem2 = pygame.transform.scale(personagem2, (50, 50))

# Gol 1
gol1 = pygame.image.load('assets/img/goalNormal.png').convert_alpha()
gol1 = pygame.transform.scale(gol1, (80, 180))

# Gol 2
gol2 = pygame.image.load('assets/img/goalNormal2.png').convert_alpha()
gol2 = pygame.transform.scale(gol2, (80, 180))

# Clock (determina FPS)
clock = pygame.time.Clock()

# ----- Gera mensagem
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

        self.gravity = 5
        self.ta_no_chao = True
        self.jumpforce = -30
        self.jumping = False

    def update (self):

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

        self.gravity = 5
        self.ta_no_chao = True
        self.jumpforce = -30
        self.jumping = False

    def update (self):

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
    

# ----- Criar o jogador 01 e jogador 02 + add ele em um grupo como do tutorial
player = Player1(personagem1)
player2 = Player2 (personagem2)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)
todos_sprites.add (player2)

# ----- Inicia estruturas de dados
game = True
screen = 1
piscar_texto = 0
mostrar = True

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
                screen = 2


            # Personagem 01 Movimento
            # Mexe o personagem 01 para esquerda e direita, adicionando uma velocidade 
            if event.key == pygame.K_LEFT:
                player.speedx -= 5

            if event.key == pygame.K_RIGHT:
                player.speedx += 5

            # Pula apenas se o jogador tiver no chão (Player 01)
            if event.key == pygame.K_UP and player.ta_no_chao == True:
                player.ta_no_chao = False
                player.jumping = True 

            # Dash Player 01, quando shift tá apertado e direção apertada
            if event.key == pygame.K_RSHIFT:
                    if player.rect.x - 20 > 0 and player.speedx == -5:
                        player.rect.x -= 50

                    if player.rect.x + 20 < WIDTH and player.speedx == +5:
                        player.rect.x += 50  


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
                player.speedx += 5
    
            if event.key == pygame.K_RIGHT:
                player.speedx -= 5
            
            # Controla a velocidade do personagem 2, quando tirar da tecla para de mexer
            if event.key == pygame.K_a:
                player2.speedx += 5

            if event.key == pygame.K_d:
                player2.speedx -= 5


    # Código inspirado no https://stackoverflow.com/questions/42472019/flickering-text-in-pygame
    #Texto piscante
    if piscar_texto >= 60: 
        mostrar = not mostrar  
        piscar_texto = 0
    piscar_texto += 1

    # Update jogadores posição atual
    player.update()
    player2.update()

    # Troca de telas
    if screen == 1:
        # Informação sobre screen 1
        window.fill((255,245,255))  # Preenche com a cor branca
        window.blit(logo_do_jogo, (0, 0))

        # Informações sobre start
        if mostrar:
            window.blit (start, (256, 231))

    if screen == 2:
        # Informação sobre screen 2
        window.fill((188,143,143))
        window.blit(gamescreen, (-50, 0))
        todos_sprites.draw(window)

        # Informações sobre gols
        window.blit (gol1 , (0, HEIGHT - 180))
        window.blit (gol2 , (WIDTH - 80, HEIGHT - 180))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

