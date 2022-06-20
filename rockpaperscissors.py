import random
import re
def play():
    user = input("Enter your choice:\nfor rock: 'r'\nfor paper: 'p'\nfor scissors: 's'\n").lower()
    computer = random.choice(['r','p','s'])
    print(user)
    try:
        valid_input = r"['r','s','p']"
        if re.search(valid_input,user):
            if user == computer:
                return 'It\'s a tie🤞🤞'
    
            if is_win(user,computer):
                return 'You won!🥳🥳'

            return 'You lost!👎👎'
        else :
            raise ValueError()

    except ValueError:
        print('Wrong Input❌❌❌')
    
def is_win(player,computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play())
