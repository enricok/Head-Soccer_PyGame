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
gamescreen = pygame.transform.scale(gamescreen, (720, 500))

clock = pygame.time.Clock()
# ----- Gera mensagem
font = pygame.font.SysFont(None, 25)
start = font.render('press "SPACE" to play', True, (255, 255, 255))

# ----- Função do movimento do jogador 1

class Player1 (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0

        self.gravity = 5
        self.ta_no_chao = True
        self.jumpforce = -35
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
                
 # ----- Criar o jogador 1 + add ele em um grupo como do tutorial

player = Player1(personagem1)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)

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
            if event.key == pygame.K_LEFT:
                player.speedx -= 5

            # Dash, quando shift tá apertado e direção apertada
            if event.key == pygame.K_RSHIFT:
                    if player.rect.x - 20 > 0 and player.speedx == -5:
                        player.rect.x -= 50
                    if player.rect.x + 20 < WIDTH and player.speedx == +5:
                        player.rect.x += 50

            if event.key == pygame.K_RIGHT:
                player.speedx += 5

            # Pula apenas se o jogador tiver no chão
            if event.key == pygame.K_UP and player.ta_no_chao == True:
                player.ta_no_chao = False
                player.jumping = True                
        
        elif event.type == pygame.KEYUP:

            # Controla a velocidade, quando tirar da tecla para de mexer
            if event.key == pygame.K_LEFT:
                player.speedx += 5
            if event.key == pygame.K_RIGHT:
                player.speedx -= 5
                

    #código inspirado no https://stackoverflow.com/questions/42472019/flickering-text-in-pygame

    if piscar_texto >= 60: 
        mostrar = not mostrar  
        piscar_texto = 0

    ####

    piscar_texto += 1
    player.update ()

    if screen == 1:
        window.fill((255,245,255))  # Preenche com a cor branca
        window.blit(logo_do_jogo, (0, 0))
        if mostrar:
            window.blit (start, (256, 231))

    if screen == 2:
        window.fill((188,143,143))
        window.blit(gamescreen, (0, -3))
        todos_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

