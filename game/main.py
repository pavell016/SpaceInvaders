from turtle import speed
import pygame
import time
import random
import os
from PIL import Image
#  letras
pygame.font.init()
FONT = pygame.font.SysFont("times new roman", 20)
# set window parameters
WIDTH, HEIGHT = 650, 750
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders knockoff")

# Obtener la ruta absoluta al directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))
BG = pygame.image.load(os.path.join(current_dir, "space.jpeg"))

#ajusta la imagen segin la alzada y la hanchura de la ventana
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))


# player caracteristics
PLAYER_WIDTH=50
PLAYER_HEIGHT=40
PLAYER_IMG=pygame.image.load(os.path.join(current_dir,"player.png"))
PLAYER_IMG=pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH,PLAYER_HEIGHT))
PLAYER_VEL=5
# disparo powerup
ORIGINAL_PLAYER_IMG = PLAYER_IMG.copy()  #copia imagen jugador
# jugdor con powerup velocidad disparo
# Boosted player image
BOOSTED_PLAYER_IMG = pygame.image.load(os.path.join(current_dir, "shootbost_spaceship.png"))
BOOSTED_PLAYER_IMG = pygame.transform.scale(BOOSTED_PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))


# enemy caracteristics
ENEMY_WIDTH=60
ENEMY_HEIGT=50
ENEMY_VEL = 3
ENEMY_IMG=pygame.image.load(os.path.join(current_dir,"enemy.png"))
ENEMY_IMG=pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH,ENEMY_HEIGT))
ENEMY_LIVES=1
    # second wave of enemies
ENEMY_SECOND_IMG=Image.open(os.path.join(current_dir,"enemyf2.png"))
ENEMY_SECOND_IMG=pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH,ENEMY_HEIGT))

# lifes
HIT_COUNT=0
HEART_WIDTH=100
HEART_HEIGT=25
HP3=pygame.image.load(os.path.join(current_dir,"3hp.png"))
HP2=pygame.image.load(os.path.join(current_dir,"2hp.png"))
HP1=pygame.image.load(os.path.join(current_dir,"1hp.png"))
HP3=pygame.transform.scale(HP3, (HEART_WIDTH,HEART_HEIGT))
HP2=pygame.transform.scale(HP2, (HEART_WIDTH,HEART_HEIGT))
HP1=pygame.transform.scale(HP1, (HEART_WIDTH,HEART_HEIGT))

# disparos
LASER_WIDTH=5
LASER_HEIGT=10
LASER_VEL=10
LASER=pygame.image.load(os.path.join(current_dir,"disparo.png"))
LASER=pygame.transform.scale(LASER, (LASER_WIDTH,LASER_HEIGT))

# powerups

    # speed boost
BOOTS_HEIGT=50
BOOTS_WIDTH=50
BOOTS_VEL=3
BOOTS=pygame.image.load(os.path.join(current_dir,"boots.png"))
BOOTS=pygame.transform.scale(BOOTS, (BOOTS_WIDTH,BOOTS_HEIGT))
    # shoot boost
SPEEDBOOST_HEIGT=50
SPEEDBOOST_WIDTH=50
SPEEDBOOST_VEL=2
SPEEDBOOST=pygame.image.load(os.path.join(current_dir,"shotboost_powerup.png"))
SPEEDBOOST=pygame.transform.scale(SPEEDBOOST, (SPEEDBOOST_WIDTH,SPEEDBOOST_HEIGT))    

    # life powerup
LIFE_HEIGT=30
LIFE_WIDTH=30
LIFE_VEL=1
LIFE=pygame.image.load(os.path.join(current_dir,"hpup.png"))
LIFE=pygame.transform.scale(LIFE, (LIFE_WIDTH,LIFE_HEIGT))        

# end menu details
TOTAL_ENEMY_KILLED=0




def draw(player, elapsed_time, enemies, projectiles,powerups,Shoot_pow, Life_up, current_phase):
    WINDOW.blit(BG,(-1,0))

    # life draw
    if HIT_COUNT == 0:
        WINDOW.blit(HP3, (WIDTH - 110, 10))
    elif HIT_COUNT == 1:
        WINDOW.blit(HP2, (WIDTH - 110, 10))
    elif HIT_COUNT == 2:
        WINDOW.blit(HP1, (WIDTH - 110, 10))
    else:
        WINDOW.blit(HP3, (WIDTH - 110, 10))    

    # time
    time_text=FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10,10))

    # player draw
    WINDOW.blit(PLAYER_IMG, player.topleft)

    # enemy draw
    if current_phase == 1:
        for enemy in enemies:
            WINDOW.blit(ENEMY_IMG, enemy.topleft)
    elif current_phase == 2:       
        for enemy in enemies:
            WINDOW.blit(ENEMY_SECOND_IMG, enemy.topleft)
    # proyectiles
    for disparos in projectiles:
        WINDOW.blit(LASER, disparos.topleft)
    # speed draw
    for boost in powerups:
        WINDOW.blit(BOOTS, boost.topleft)
    # shoot draw
    for boost in Shoot_pow:
        WINDOW.blit(SPEEDBOOST, boost.topleft)
    # life draw
    for boost in Life_up:
        WINDOW.blit(LIFE, boost.topleft)
    pygame.display.update()


    # menu final
def endmenu(time):
    # Dimensiones de la ventana
    WIDTH_END, HEIGHT_END = 400, 400

    # Inicializar Pygame
    pygame.init()

    # Crear nueva ventana
    WINDOW_END = pygame.display.set_mode((WIDTH_END, HEIGHT_END))
    pygame.display.set_caption("Space Invaders Knockoff")

    # Colores y fuentes
    FONT = pygame.font.SysFont("Courier", 30)
    FONT_SMALL = pygame.font.SysFont("Courier", 20)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    # Llenar fondo
    WINDOW_END.fill(WHITE)

    # Mensaje de muerte
    lost_text = FONT.render("YOU DIED", 1, RED)
    WINDOW_END.blit(
        lost_text,
        (
            WIDTH_END / 2 - lost_text.get_width() / 2,
            HEIGHT_END / 4 - lost_text.get_height() / 2,
        ),
    )

    # Listar las estadísticas
    stats = [
        f"Enemies killed: {TOTAL_ENEMY_KILLED}",
        f"Time alive: {round(time)}s",
    ]

    for i, stat in enumerate(stats):
        stat_text = FONT_SMALL.render(stat, 1, RED)
        WINDOW_END.blit(stat_text, (40, HEIGHT_END / 2 + 30 + i * 25))

    # Actualizar la ventana
    pygame.display.update()

    # Retardo antes de salir
    pygame.time.delay(6000)

def main():

    # globales
    # vidas
    global HIT_COUNT
    global PLAYER_VEL
    global PLAYER_IMG
    # enemigos muertos
    global TOTAL_ENEMY_KILLED
    global ENEMY_LIVES  # Asegúrate de que ENEMY_LIVES pueda ser modificada

    # funcion disparo
    def disparar(player):
        projectile = pygame.Rect(player.centerx - LASER_WIDTH // 2, player.top, LASER_WIDTH, LASER_HEIGT)
        projectiles.append(projectile)

    run = True
    # player
    # pygame.Rect(X axis, Y axis, altura_personaje, hanchura personaje)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    # game timer 
    start_time = time.time()
    elapsed = 0
    # definir la velocitat en la que el while s'executa en tot tipus d'ordenadors
    clock = pygame.time.Clock()
    # enemigos
    enemy_increment = 2000
    enemy_count = 0

    enemies = []
    hit = False

    # proyectiles
    projectiles = []
    cooldown = 200
    lastshot = 0
    shoot_boost_active = False
    shoot_boost_start_time = 0

    # powerups
    Speed_pow = []
    Shoot_pow = []
    Life_up = []

    # fase actual
    current_phase = 1  # Comenzar en la primera fase

    while run:
        # gestionar el tiempo y las fases
        enemy_count += clock.tick(60)  # utilitza frames per segon
        elapsed_time = time.time() - start_time

        # Cambiar de fase cada 2 minutos
        if elapsed_time >= 120 and current_phase == 1:
            current_phase = 2
            ENEMY_LIVES = 2  # Aumentar vidas enemigas en la segunda fase
        
        # generar enemigos
        if enemy_count > enemy_increment:
            for _ in range(random.randint(1, 7)):
                enemy_X = random.randint(0, WIDTH - ENEMY_WIDTH)
                enemy = pygame.Rect(enemy_X, -ENEMY_HEIGT, ENEMY_WIDTH, ENEMY_HEIGT)
                enemies.append(enemy)
            enemy_increment = max(200, enemy_increment - 15)    
            enemy_count = 0   
                
        # generar un powerup de rapidez
        if random.random() < 0.0007:  
            powerup_X = random.randint(0, WIDTH - BOOTS_WIDTH)
            powerup = pygame.Rect(powerup_X, -BOOTS_HEIGT, BOOTS_WIDTH, BOOTS_HEIGT)
            Speed_pow.append(powerup)
        # generar un powerup de rapidez de disparo
        if random.random() < 0.0005:  
            powerup_X = random.randint(0, WIDTH - SPEEDBOOST_WIDTH)
            powerup = pygame.Rect(powerup_X, -SPEEDBOOST_HEIGT, SPEEDBOOST_WIDTH, SPEEDBOOST_HEIGT)
            Shoot_pow.append(powerup)
        # generar powerups para vida
        if random.random() < 0.0001:  
            powerup_X = random.randint(0, WIDTH - SPEEDBOOST_WIDTH)
            powerup = pygame.Rect(powerup_X, -LIFE_HEIGT, LIFE_WIDTH, LIFE_HEIGT)
            Life_up.append(powerup)    

        for event in pygame.event.get():
            # en el caso que se cierre la pestaña con la "X", se cerrará el juego
            if event.type == pygame.QUIT:
                run = False
                break

        # movimiento del personaje
        # escucha que teclas se están presionando
        keys = pygame.key.get_pressed()  
        # la lista de teclas se guardan en un diccionario
        # movimiento a la derecha
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: 
            player.x -= PLAYER_VEL
        # movimiento a la izquierda
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        # movimiento arriba
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        # movimiento abajo
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VEL 

        # disparar
        key = pygame.key.get_pressed()
        current_t = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_t - lastshot >= cooldown:
            disparar(player)
            lastshot = current_t

        # Speed boost powerup
        for powerup in Speed_pow[:]:
            powerup.y += BOOTS_VEL
            if powerup.y > HEIGHT:
                Speed_pow.remove(powerup)
            elif powerup.colliderect(player):  # Power-up collected
                Speed_pow.remove(powerup)
                PLAYER_VEL += 1

        # Shooting speed boost powerup
        for powerup in Shoot_pow[:]:
            powerup.y += SPEEDBOOST_VEL
            if powerup.y > HEIGHT:
                Shoot_pow.remove(powerup)
            elif powerup.colliderect(player):  # Power-up collected
                Shoot_pow.remove(powerup)
                PLAYER_IMG = BOOSTED_PLAYER_IMG  # change player img to boosted player img
                cooldown = 100
                shoot_boost_active = True
                shoot_boost_start_time = pygame.time.get_ticks()

        # Restore original image after 20 seconds
        if shoot_boost_active and pygame.time.get_ticks() - shoot_boost_start_time > 20000:  # 20 seconds
            PLAYER_IMG = ORIGINAL_PLAYER_IMG
            cooldown = 200
            shoot_boost_active = False

        # Life powerup
        for powerup in Life_up[:]:
            powerup.y += LIFE_VEL
            if powerup.y > HEIGHT:
                Life_up.remove(powerup)
            elif powerup.colliderect(player):  # Power-up collected
                Life_up.remove(powerup)
                HIT_COUNT -= 1
                       
        # mover enemigos
        for enemy in enemies[:]:
            enemy.y += ENEMY_VEL
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            elif enemy.colliderect(player):  
                enemies.remove(enemy)
                HIT_COUNT += 1
                if HIT_COUNT >= 3:
                    hit = True
                    break

        # mover disparos
        for projectile in projectiles[:]:
            projectile.y -= LASER_VEL  # Move the projectile upwards
            if projectile.y < 0:  # Remove projectiles that go off-screen
                projectiles.remove(projectile) 

        # enemy kill 
        for projectile in projectiles[:]:
            for enemy in enemies[:]:
                if projectile.colliderect(enemy):
                    ENEMY_LIVES -= 1
                    if ENEMY_LIVES <= 0:
                        enemies.remove(enemy)
                        ENEMY_LIVES = 2 if current_phase == 2 else 1  # Restaurar vidas según la fase
                    projectiles.remove(projectile)
                    TOTAL_ENEMY_KILLED += 1
                    break            

        if hit: 
            endmenu(elapsed_time)
            break                 
        
        
        draw(player, elapsed_time, enemies, projectiles, Speed_pow, Shoot_pow, Life_up, current_phase)

    # Salir del juego
    pygame.quit() 


if __name__ == "__main__":
    pygame.init()
    main()