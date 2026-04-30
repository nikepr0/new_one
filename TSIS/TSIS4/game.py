import pygame
import random
import db

BLOCK = 20
WIDTH = 600
GAME_HEIGHT = 600 

class Game:
    def __init__(self, username, settings):
        self.username = username
        self.settings = settings
        self.player_id = db.get_or_create_player(username)
        self.pb = db.get_personal_best(self.player_id)
        self.reset()

    def reset(self):
        self.snake = [[300, 300], [280, 300], [260, 300]]
        self.direction = "RIGHT"
        self.score = 0
        self.level = 1
        self.base_speed = 7
        self.speed_mod = 0 # Модификатор от бонусов
        self.obstacles = []
        self.food = self.spawn_item("normal")
        self.poison = self.spawn_item("poison")
        self.powerup = None
        # Таймер для следующего появления бонуса (через 5-10 сек)
        self.pu_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)
        self.active_pu_end = 0
        self.shield_active = False

    def spawn_item(self, itype):
        while True:
            x = random.randrange(0, WIDTH, BLOCK)
            y = random.randrange(0, GAME_HEIGHT, BLOCK)
            pos = [x, y]
            
            # Проверка, чтобы не спавнить в змейке или стенах
            if pos not in self.snake and pos not in self.obstacles:
                if itype == "normal":
                    chance = random.random()
                    if chance < 0.7:
                        color, val, timer = (255, 0, 0), 1, 7000
                    elif chance < 0.9:
                        color, val, timer = (0, 100, 255), 3, 5000
                    else:
                        color, val, timer = (255, 215, 0), 5, 3000
                    
                    return {
                        "pos": pos, 
                        "color": color, 
                        "val": val, 
                        "timer": pygame.time.get_ticks() + timer
                    }
                
                if itype == "poison":
                    return {"pos": pos, "color": (138, 43, 226)}
                
                if itype == "pu":
                    kind = random.choice(["speed", "slow", "shield"])
                    return {
                        "pos": pos, 
                        "kind": kind, 
                        "timer": pygame.time.get_ticks() + 8000 # Исчезнет через 8 сек
                    }

    def update(self):
        now = pygame.time.get_ticks()

        # 1. Проверка таймеров еды и бонусов
        if now > self.food["timer"]:
            self.food = self.spawn_item("normal")
        
        if self.powerup and now > self.powerup["timer"]:
            self.powerup = None
            self.pu_spawn_time = now + random.randint(5000, 10000)

        # Спавн нового бонуса, если пришло время
        if not self.powerup and now > self.pu_spawn_time:
            self.powerup = self.spawn_item("pu")

        # Проверка окончания действия эффекта скорости
        if self.active_pu_end > 0 and now > self.active_pu_end:
            self.speed_mod = 0
            self.active_pu_end = 0

        # 2. Движение
        head = self.snake[0].copy()
        if self.direction == "UP": head[1] -= BLOCK
        elif self.direction == "DOWN": head[1] += BLOCK
        elif self.direction == "LEFT": head[0] -= BLOCK
        elif self.direction == "RIGHT": head[0] += BLOCK

        # 3. Коллизии
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= GAME_HEIGHT or 
            head in self.snake or head in self.obstacles):
            
            if self.shield_active:
                self.shield_active = False
                # Если врезались со щитом, просто не двигаемся в ту сторону или "отскакиваем"
                # В данной реализации — просто продолжаем играть, не добавляя голову
                return "MOVE" 
            
            db.save_game_session(self.player_id, self.score, self.level)
            return "GAMEOVER"

        self.snake.insert(0, head)

        # 4. Проверка поедания
        # Обычная еда
        if head == self.food["pos"]:
            self.score += self.food["val"]
            if self.score // 5 + 1 > self.level:
                self.level += 1
                self.generate_obstacles()
            self.food = self.spawn_item("normal")
            return "EAT"

        # Яд
        elif head == self.poison["pos"]:
            if len(self.snake) > 2:
                self.snake.pop(); self.snake.pop() # Укорачиваем
                self.poison = self.spawn_item("poison")
                return "POISON"
            else: 
                db.save_game_session(self.player_id, self.score, self.level)
                return "GAMEOVER"

        # Бонус (Power-up)
        elif self.powerup and head == self.powerup["pos"]:
            kind = self.powerup["kind"]
            if kind == "speed":
                self.speed_mod = 5
                self.active_pu_end = now + 5000
            elif kind == "slow":
                self.speed_mod = -3
                self.active_pu_end = now + 5000
            elif kind == "shield":
                self.shield_active = True
            
            self.powerup = None
            self.pu_spawn_time = now + random.randint(5000, 10000)
            return "POWERUP"

        else:
            self.snake.pop()

        return "MOVE"

    def generate_obstacles(self):
        self.obstacles = []
        if self.level >= 3:
            for _ in range(self.level + 2):
                while True:
                    x = random.randrange(0, WIDTH, BLOCK)
                    y = random.randrange(0, GAME_HEIGHT, BLOCK)
                    # Чтобы не замуровать змейку, проверяем расстояние от головы
                    dist = abs(x - self.snake[0][0]) + abs(y - self.snake[0][1])
                    if [x, y] not in self.snake and dist > BLOCK * 3:
                        self.obstacles.append([x, y])
                        break