import os, time, random, sys

def run_game():
    w, h = 20, 15
    player_x = w // 2
    enemies = []
    score = 0
    
    while True:
        # Жаңа кедергі қосу
        if random.random() < 0.3:
            enemies.append([random.randint(0, w-1), 0])
        
        # Экранды тазалау
        os.system('clear')
        print(f"--- SCORE: {score} --- (Q - Exit)")
        
        # Алаңды салу
        field = [[' ' for _ in range(w)] for _ in range(h)]
        field[h-1][player_x] = '0' # Ойыншы
        
        for e in enemies[:]:
            e[1] += 1 # Төмен түсу
            if e[1] >= h:
                enemies.remove(e)
                score += 1
            elif e[1] == h-1 and e[0] == player_x:
                print("\nGAME OVER! СЕНІ ҰСТАП АЛДЫ!")
                return
            else:
                field[e[1]][e[0]] = '#' # Кедергі

        for row in field:
            print('|' + ''.join(row) + '|')
            
        # Басқару (Тез жауап беру үшін)
        move = input("Бағыт (a - сол, d - оң): ").lower()
        if move == 'a' and player_x > 0: player_x -= 1
        elif move == 'd' and player_x < w-1: player_x += 1
        elif move == 'q': break

run_game()
      
