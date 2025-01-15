import random
import os

from players import Player, CompPlayer
from items import Potion



def battle(fighterlist):
    """ """
    all_alive = True
    cycle = 1
    player2turn = False

    random.shuffle(fighterlist)

    for fighter in fighterlist:
        player1 = fighterlist.pop()
        player2 = fighterlist.pop()

    print('*{} vs {}*'.format(player1.name.upper(), player2.name.upper()))
    input('*********************\n(press enter to continue)'.format(cycle))

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # clears screen w/ console specific cmd
        print('*** BATTLE MODE ***')
        print('ROUND {}'.format(cycle))
        print('{}\'s health is {}'.format(player1, player1.health))
        print('{}\'s health is {}'.format(player2, player2.health))
        print('')

        if player1.health <= 0:
            all_alive = False
            print('fight over! {} won!'.format(player2))
            break

        elif player2.health <= 0:
            all_alive = False
            print('fight over! {} won!'.format(player1))
            break

        elif player2turn == True:
            player2.fight(enemy=player1)

            if player1.health < 0:
                player1.health = 0
            cycle += 1
            player2turn = False
            input('(press enter to continue)') # Next round!

        else:
            player1.fight(enemy=player2)

            if player2.health < 0:
                player2.health = 0
            player2turn = True
            input('(press enter to continue)')



def main():
    """ """
    fighters = []

    player = Player('Curtis')
    monster = CompPlayer()

    fighters.append(player)
    fighters.append(monster)

    potions = [Potion(attribute=random.randint(1,4)) for fighter in fighters]
    monster.inventory.append(potions.pop())
    player.inventory.insert(0, potions.pop())

    print('WELCOME TO TURNBASED !\n')


    battle(fighters)


    keepfighting = input('\nCONTINUE? (y/n)\n').lower()

    if keepfighting == 'y':
    	main()
    elif keepfighting == 'n':
    	print('See yuh next time!')
    else:
    	print('{}? I\'ll take that as a no...'.format(keepfighting))





if __name__ == '__main__':
    main()




