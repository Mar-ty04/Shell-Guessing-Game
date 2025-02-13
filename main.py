#Marisol Morales & Andreas Moreno, 1/29/2023, Shell Guessing Game Lab 1

import check_input
import random


def main():
  user_amount = 100
  continue_playing = True

  print('-Shell Game-')
  print('Find the ball to double your bet!')

  while user_amount > 0 and continue_playing is True:
    print()
    print(f'You have ${user_amount}.')

    bet_amount = check_input.get_int_range('Bet amount? ', 1, user_amount)

    print('  ___     ___     ___')
    print(' /   \\   /   \\   /   \\ ')
    print('/  1  \\ /  2  \\ /  3  \\ ')
    print('------- ------- -------')

    make_guess = check_input.get_int_range('Make a guess: ', 1, 3)
    winning_cup = random.randint(1, 3)

    if winning_cup == 1:
      print('  ___     ___     ___')
      print(' /   \\   /   \\   /   \\ ')
      print('/  o  \\ /     \\ /     \\ ')
      print('------- ------- -------')

    elif winning_cup == 2:
      print('  ___     ___     ___')
      print(' /   \\   /   \\   /   \\ ')
      print('/     \\ /  o  \\ /     \\ ')
      print('------- ------- -------')

    elif winning_cup == 3:
      print('  ___     ___     ___')
      print(' /   \\   /   \\   /   \\ ')
      print('/     \\ /     \\ /  o  \\ ')
      print('------- ------- -------')

    if make_guess == winning_cup:
      print('Congratulations!')
      print()
      user_amount -= bet_amount
      user_amount = user_amount + (bet_amount * 2)
    else:
      print('Sorry... you lose.')
      user_amount -= bet_amount

    if user_amount <= 0:
      print("You're out of money! Game over!")
      break

    continue_playing = check_input.get_yes_no('Play again? (Y/N): ')
    if continue_playing is False:
      
      break


main()
