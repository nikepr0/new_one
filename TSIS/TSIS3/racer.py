import pygame
import random
import sys
import os

BASE_DIR = os.path.dirname(__file__)

# ─── Colours (Золотая палитра) ────────────────────────────────────────────────
GRAY      = (100, 100, 100)
DARK_GRAY = ( 20,  22,  30) 
WHITE     = (255, 255, 240)
BLACK     = (  0,   0,   0)
GOLD      = (255, 215,   0) 
GOLD_DARK = (184, 134,  11)
CYAN      = (  0, 220, 255)
PURPLE    = (160,  80, 240)
NITRO_COL = (  0, 220, 255)
SHIELD_COL= (255, 215,   0) 
REPAIR_COL= ( 80, 220,  80)
OIL_COL   = ( 15,  15,  25)

ROAD_LEFT  = 100
ROAD_RIGHT = 400
ROAD_W     = ROAD_RIGHT - ROAD_LEFT
LANES      = [170, 250, 330]

# ─── Asset loader ──────────────────────────────────────────────────────────────

def load_image(name, size):
    path = os.path.join(BASE_DIR, "assets", "cars", name)
    if not os.path.exists(path):
        surf = pygame.Surface(size)
        surf.fill((200, 200, 200))
        return surf
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

def tint_car(image, color):
    t = image.copy()
    for x in range(t.get_width()):
        for y in range(t.get_height()):
            p = t.get_at((x, y))
            if p[3] > 0:
                new_r = (color[0] * p[0]) // 255
                new_g = (color[1] * p[1]) // 255
                new_b = (color[2] * p[2]) // 255
                t.set_at((x, y), (new_r, new_g, new_b, p[3]))
    return t

def load_sound(name):
    path = os.path.join(BASE_DIR, "assets", "sounds", name)
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    return None

DIFFICULTY = {
    "easy":   {"base_speed": 3,   "speed_step": 0.3, "enemy_interval": 130, "obstacle_interval": 230},
    "normal": {"base_speed": 4,   "speed_step": 0.5, "enemy_interval": 110, "obstacle_interval": 190},
    "hard":   {"base_speed": 5.5, "speed_step": 0.7, "enemy_interval": 80,  "obstacle_interval": 140},
}

# ─── Main game ─────────────────────────────────────────────────────────────────

def run_game(screen, clock, settings, player_name):
    W, H = screen.get_size()
    
    selected_diff = settings.get("difficulty", "normal").lower()
    diff = DIFFICULTY.get(selected_diff, DIFFICULTY["normal"])
    
    ei = diff["enemy_interval"]
    oi = diff["obstacle_interval"]
    
    font_hud = pygame.font.SysFont("consolas", 22, bold=True)
    
    snd_coin   = load_sound("click.mp3")
    snd_crash  = load_sound("crash.mp3")
    snd_nitro  = load_sound("nitro.mp3")
    snd_repair = load_sound("repair.mp3")
    snd_shield = load_sound("shield.mp3")
    snd_engine = load_sound("engine.mp3")
    sound_on   = settings.get("sound", True)

    if sound_on and snd_engine:
        snd_engine.set_volume(0.2); snd_engine.play(-1)

    car_type = settings.get("car_type", "Sport").lower()
    player_color = tuple(settings.get("car_color", [255, 215, 0]))
    base_img = load_image(f"{car_type}_white.png", (60, 90) if car_type != "truck" else (60, 100))
    player_img = tint_car(base_img, player_color)
    player = player_img.get_rect(center=(250, 600))

    enemy_base = load_image("enemy.png", (60, 90))
    taxi_base  = load_image("taxi_white.png", (60, 90))
    truck_base = load_image("truck_white.png", (60, 100))
    sport_base = load_image("sport_white.png", (60, 90))

    traffic_templates = [
        {"img": tint_car(enemy_base, (150, 150, 150))},
        {"img": tint_car(taxi_base,  (218, 165, 32))},
        {"img": tint_car(truck_base, (100, 100, 110))},
        {"img": tint_car(sport_base, (255, 215, 0))},
    ]

    score, coins_count, distance, frame, road_offset = 0, 0, 0, 0, 0
    enemy_speed = diff["base_speed"]
    last_level, running = 0, True
    enemies, obstacles, barriers, coins, powerups = [], [], [], [], []
    active_pu, pu_timer = None, 0
    nitro_active, shield_active = False, False

    def safe_lane(existing_rects, min_gap=400): # Увеличен зазор, чтобы исключить наслоение
        temp_lanes = list(LANES)
        random.shuffle(temp_lanes)
        for lane in temp_lanes:
            # Создаем высокую невидимую зону проверки над местом спавна
            candidate = pygame.Rect(lane - 35, -500, 70, 500 + min_gap)
            if not any(candidate.colliderect(r) for r in existing_rects):
                return lane
        return None

    def get_all_rects():
        return ([e["rect"] for e in enemies] + [o["rect"] for o in obstacles] + 
                [b["rect"] for b in barriers] + [c["rect"] for c in coins])

    while running:
        dt = clock.tick(60)
        frame += 1
        current_speed = enemy_speed * (1.6 if nitro_active else 1.0)
        distance += int(current_speed * 0.1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if sound_on and snd_engine: snd_engine.stop()
                return score, distance, coins_count

        keys = pygame.key.get_pressed()
        sx = 7 * (1.4 if nitro_active else 1.0)
        if keys[pygame.K_LEFT] and player.left > ROAD_LEFT: player.x -= sx
        if keys[pygame.K_RIGHT] and player.right < ROAD_RIGHT: player.x += sx

        all_rects = get_all_rects()
        occupied_this_frame = []

        # Спавн машин
        if frame % ei == 0:
            lane = safe_lane(all_rects)
            if lane:
                occupied_this_frame.append(lane)
                tm = random.choice(traffic_templates)
                # Все враги теперь едут с одной скоростью (чуть медленнее игрока), чтобы не врезаться друг в друга
                enemies.append({"img": tm["img"], "rect": tm["img"].get_rect(center=(lane, -110))})

        # Спавн препятствий и монет
        if frame % oi == 0:
            lane = safe_lane(all_rects)
            if lane and lane not in occupied_this_frame:
                item = random.choice(["obstacle", "barrier", "coin"])
                if item == "obstacle":
                    kind = random.choice(["oil", "pothole"])
                    rect = pygame.Rect(lane-35, -60, 70, 50) if kind == "oil" else pygame.Rect(lane-20, -35, 40, 35)
                    obstacles.append({"rect": rect, "kind": kind})
                elif item == "barrier":
                    barriers.append({"rect": pygame.Rect(lane - 35, -50, 70, 20)})
                elif item == "coin":
                    c_data = random.choice([
                        {"color": GOLD, "value": 1},
                        {"color": GOLD_DARK, "value": 2},
                        {"color": PURPLE, "value": 3}
                    ])
                    coins.append({"rect": pygame.Rect(lane-15, -30, 30, 30), "color": c_data["color"], "value": c_data["value"]})
        
        if frame % 500 == 0 and not powerups:
            lane = safe_lane(all_rects)
            if lane:
                kind = random.choice(["nitro", "shield", "repair"])
                powerups.append({"rect": pygame.Rect(lane-20, -40, 40, 40), "kind": kind, "timer": 8000})

        # Обновление позиций и коллизии
        # Трафик едет со скоростью чуть меньше текущей скорости мира
        rel_traffic_speed = current_speed - 2
        
        for en in enemies[:]:
            en["rect"].y += rel_traffic_speed
            if en["rect"].y > H + 100: enemies.remove(en)
            elif player.colliderect(en["rect"]):
                if shield_active: shield_active = False; enemies.remove(en)
                else: running = False

        for ob in obstacles[:]:
            ob["rect"].y += current_speed
            if ob["rect"].y > H: obstacles.remove(ob)
            elif player.colliderect(ob["rect"]):
                if active_pu == "repair": obstacles.remove(ob); active_pu = None
                elif shield_active: shield_active = False; obstacles.remove(ob)
                else: running = False

        for br in barriers[:]:
            br["rect"].y += current_speed
            if br["rect"].y > H: barriers.remove(br)
            elif player.colliderect(br["rect"]):
                if shield_active: shield_active = False; barriers.remove(br)
                else: running = False

        for co in coins[:]:
            co["rect"].y += current_speed
            if co["rect"].y > H: coins.remove(co)
            elif player.colliderect(co["rect"]):
                coins_count += co["value"]; score += co["value"]*10; coins.remove(co)
                if sound_on and snd_coin: snd_coin.play()

        for pu in powerups[:]:
            pu["rect"].y += current_speed
            if pu["rect"].y > H: powerups.remove(pu)
            elif player.colliderect(pu["rect"]):
                active_pu = pu["kind"]
                if active_pu == "nitro": nitro_active = True; pu_timer = 4000
                elif active_pu == "shield": shield_active = True; pu_timer = -1
                elif active_pu == "repair": pu_timer = 5000
                powerups.remove(pu)

        if active_pu in ["nitro", "repair"] and pu_timer > 0:
            pu_timer -= dt
            if pu_timer <= 0: nitro_active = False; active_pu = None

        # Прогрессия скорости
        score = coins_count * 10 + distance // 10
        level = distance // 150
        if level > last_level:
            enemy_speed = min(diff["base_speed"] + level * diff["speed_step"], 12)
            last_level = level

        # ── Рендеринг ─────────────────────────────────────────────────────────
        screen.fill((15, 15, 20)) 
        pygame.draw.rect(screen, (30, 30, 35), (ROAD_LEFT, 0, ROAD_W, H))
        
        # Рендеринг разметки исправлен (от -80 для бесшовности)
        road_offset = (road_offset + current_speed) % 80
        for y in range(-80, H + 80, 80):
            pygame.draw.rect(screen, GOLD_DARK, (ROAD_LEFT + ROAD_W//3 - 2, y + road_offset, 4, 40))
            pygame.draw.rect(screen, GOLD_DARK, (ROAD_LEFT + 2*ROAD_W//3 - 2, y + road_offset, 4, 40))

        for ob in obstacles:
            col = OIL_COL if ob["kind"] == "oil" else (45, 45, 50)
            pygame.draw.ellipse(screen, col, ob["rect"])
        for br in barriers: pygame.draw.rect(screen, GOLD, br["rect"])
        for en in enemies: screen.blit(en["img"], en["rect"])
        for co in coins: pygame.draw.circle(screen, co["color"], co["rect"].center, 12)
        for pu in powerups: pygame.draw.rect(screen, CYAN, pu["rect"], border_radius=5)
        
        if shield_active: pygame.draw.ellipse(screen, GOLD, player.inflate(20, 20), 2)
        
        screen.blit(player_img, player)
        
        # HUD
        bar = pygame.Surface((W, 60), pygame.SRCALPHA); bar.fill((0, 0, 0, 180))
        screen.blit(bar, (0, 0))
        screen.blit(font_hud.render(f"SCORE: {score}", True, GOLD), (20, 15))
        
        diff_txt = font_hud.render(f"MODE: {selected_diff.upper()}", True, CYAN)
        screen.blit(diff_txt, (W//2 - diff_txt.get_width()//2, 10))
        
        dist_txt = font_hud.render(f"{distance} m", True, WHITE)
        screen.blit(dist_txt, (W//2 - dist_txt.get_width()//2, 32))
        
        if active_pu:
            p_txt = font_hud.render(active_pu.upper(), True, GOLD)
            screen.blit(p_txt, (W - p_txt.get_width() - 20, 15))

        pygame.display.flip()

    if sound_on and snd_engine: snd_engine.stop()
    if sound_on and snd_crash: snd_crash.play()
    return score, distance, coins_count