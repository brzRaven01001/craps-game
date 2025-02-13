import random

def roll_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1 + dice2

def play_craps():
    while True:
        print("\nStarting a new Craps round")
        
        dice1, dice2, results = roll_dices()
        print(f"You rolled {dice1} + {dice2} = {results}")
        
        if results in [7, 11]:
            print("Natural! You won!\n")
            return
        elif results in [2, 3, 12]:
            print("Craps! You lose!\n")
        else:
            point = results
            print(f"Your Point is {point}. Keep going until you get {point} (win) or 7 (defeat).\n")
            
            while True:
                input("Press ENTER to roll the dices...")
                dice1, dice2, new_result = roll_dices()
                print(f"You rolled {dice1} + {dice2} = {new_result}")
                
                if new_result == point:
                    print("You got a Point ({point}) and won!\n")
                    return
                elif new_result == 7:
                    print("You got a 7! You lose!\n")
                    break
                
            while True:
                response = input("Would you like to try again? (Y/N): ").strip().lower()
                if response == "y":
                    break
                elif response == "n":
                    print("Thank you for playing!\n")
                    exit()
                else:
                    print("Invalid option. Type 'S' to play again ou 'N' to exit.")

def menu():
    while True:
        print("------- Welcome to Craps -------")
        print("1 - Play")
        print("2 - Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            play_craps()
        elif choice == "2":
            print("Thank You for playing!")
            break
        else:
            print("Invalid opition. Try again.\n")
            
menu()