import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.\n")

    random_number = random.randint(1, 100)
    attempts = 10
    guess_list = []

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt #{attempt} - Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number between 1 and 100.\n")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Your guess must be between 1 and 100.\n")
            continue

        guess_list.append(guess)
        print(f"📝 Previous guesses: {', '.join(map(str, guess_list))}")

        if guess == random_number:
            print("\n🎉 Congratulations! You guessed the number correctly!")
            break
        elif guess < random_number:
            print("📉 Too low!\n")
        else:
            print("📈 Too high!\n")
    else:
        print(f"\n💥 Game Over! The number was {random_number}.")

    # Ask if user wants to play again
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        print("\nRestarting game...\n")
        number_guessing_game()
    else:
        print("👋 Thanks for playing!")

# Start the game
number_guessing_game()
