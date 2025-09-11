import random
def play():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors or q to quit): ").lower()
        
        if user_choice == 'q':
            print("👋 Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win!")
        else:
            print("💀 You lose!")

# Run the game
if __name__ == "__main__":
    play()
