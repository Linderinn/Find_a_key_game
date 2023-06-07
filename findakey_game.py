from random import randint
from math import sqrt

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0,GAME_HEIGHT)
player_x = 0
player_y= 0
player_found_key = False
steps=0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
print(key_x, key_y)

while not player_found_key:
    steps += 1
    print()
    print ('You can move in certain directions [W/S/A/D]: ')

    move = input('Where are you going? ')
    match move.lower():
        case 'w':
            player_y += 1

            if player_y > GAME_HEIGHT:
                print('Ouch! You hit the wall!')
            player_y = GAME_HEIGHT

        case 's':
            player_y -= 1

            if player_y < 0:
                print('Ouch! You hit the wall!')
            player_y = 0

        case 'a':
            player_x -= 1

            if player_x < 0:
                print('Ouch! You hit the wall!')
            player_x = 0

        case 'd':
            player_x +=1

            if player_x > GAME_WIDTH:
                print('Ouch! You hit the wall!')
                player_x = GAME_WIDTH

        case 'q':
                print('This is the end of the game!')
                quit()

        case _:
            print('I dont know where are you going...')
            continue
         
    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    print(distance_before_move)
    print(distance_after_move)
    if player_x == key_x and player_y == key_y:
        print('The treasure is yours! Congratulations! You have earned 100 points to awesomeness!')
        print(f'You have made {steps} moves. Congrats!')
        player_found_key = True

    elif distance_before_move < distance_after_move:
        print('Farther...!')
        
    else:
        print('Closer...!')

        distance_before_move = distance_after_move

print(player_x, player_y)
