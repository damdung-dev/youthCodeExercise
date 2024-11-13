import random

def rock_paper_scissors(user_choice):
    choices = {'b': 'Paper', 'd': 'Rock', 'k': 'Scissors'}
    computer_choice = random.choice(['b', 'd', 'k'])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'b' and computer_choice == 'd') or \
         (user_choice == 'd' and computer_choice == 'k') or \
         (user_choice == 'k' and computer_choice == 'b'):
        result = "You win!"
    else:
        result = "Computer wins!"
        
    return f"Your choice: {choices[user_choice]}, Computer's choice: {choices[computer_choice]}. {result}"

# Example usage
user_choice = input("Enter 'b' for Paper, 'd' for Rock, 'k' for Scissors: ").strip().lower()
if user_choice in ['b', 'd', 'k']:
    print(rock_paper_scissors(user_choice))
else:
    print("Invalid input.")
