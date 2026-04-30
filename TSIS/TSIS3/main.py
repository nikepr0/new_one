import pygame
import sys

from persistence import load_settings, save_score
from ui import (main_menu, settings_screen, leaderboard_screen,
                game_over_screen, username_screen)
from racer import run_game

def main():
    pygame.init()
    pygame.mixer.init()

    WIDTH, HEIGHT = 500, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turbo Racer — TSIS3")
    clock = pygame.time.Clock()

    settings    = load_settings()
    player_name = None

    while True:
        choice = main_menu(screen, clock)

        if choice == "quit":
            pygame.quit()
            sys.exit()

        elif choice == "settings":
            settings = settings_screen(screen, clock)

        elif choice == "leaderboard":
            leaderboard_screen(screen, clock)

        elif choice == "play":
            if player_name is None:
                player_name = username_screen(screen, clock)

            while True:   # retry loop
                score, distance, coins = run_game(
                    screen, clock, settings, player_name)

                save_score(player_name, score, distance)

                result = game_over_screen(
                    screen, clock, score, distance, coins, player_name)

                if result == "retry":
                    continue          # play again with same name
                else:
                    player_name = None   # reset name for next run
                    break

if __name__ == "__main__":
    main()