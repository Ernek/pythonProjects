import random

class Game:
    def __init__(self):
        # call the get_computer_pick() method
        self.computer_pick = self.get_computer_pick()

        # call the user_pick() method
        self.user_pick = self.get_user_pick()
        
        # call get_result to determine if the user wins or looses or 
        # draws against the computer 
        self.result = self.get_result()


    def get_computer_pick(self):
        # get random number among 1, 2, 3
        random_number = random.randint(1,3)

        # possible options
        options = {1:'rock', 2:'paper', 3:'scissors'}

        # return the value present at random_number
        return options[random_number]
    
    def get_user_pick(self):
        # Make sure the user writes the correct option 
        while True:

            user_pick = input('Enter rock/paper/scissors: ')

            user_pick = user_pick.lower()

            if user_pick in ('rock', 'paper', 'scissors'):
                break 
            else:
                print('Wrong input, make sure you write one of the three options correctly')

        # converting the user's pick to lowercase and return it
        return user_pick
    
    def get_result(self):
        if self.computer_pick == self.user_pick:
            return 'draw'
        
        elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
            return 'win'
        elif self.user_pick == 'scissors' and self.computer_pick == 'paper':
            return 'win'
        elif self.user_pick == 'paper' and self.computer_pick == 'rock':
            return 'win'
        else:
            return 'lose'

    def print_result(self):
        print(f"Computer's pick: {self.computer_pick}")
        print(f"Your pick: {self.user_pick}")
        print(f"You {self.result}")

# playing the game once:
# game = Game()
# game.print_result()

# playing the game if user wants to keep playing 
while True:
    game = Game()
    game.print_result()

    play_again = input('Do you want to play again (y/n): ')
    
    if play_again in ('y','n'):
        if play_again == 'y':
            continue
        else:
            break
    else:
        print('Make sure you write only "y" next time if you wanna keep playing')
        break
