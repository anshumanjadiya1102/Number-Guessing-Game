import java.util.Scanner;
import java.util.Random;

public class Number_Guessing_Game {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int numberToGuess = random.nextInt(100) + 1;
        int numberOfTries = 0;
        int guess;
        boolean hasGuessedCorrectly = false;

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I'm thinking of a number between 1 and 100. Try to guess it!");
        System.out.println("Press Ctrl+D (Unix/macOS) or Ctrl+Z (Windows) then Enter to exit.");

        while (true) {
            System.out.print("Enter your guess: ");

            // Detect EOF
            if (!scanner.hasNext()) {
                System.out.println("\nNo more input detected (EOF). Exiting game.");
                break;
            }

            // Check for valid integer
            if (!scanner.hasNextInt()) {
                System.out.println("Invalid input. Please enter a valid integer.");
                scanner.next(); // discard invalid input
                continue;
            }

            guess = scanner.nextInt();
            numberOfTries++;

            if (guess < 1 || guess > 100) {
                System.out.println("Out of range! Please guess a number between 1 and 100.");
            } else if (guess < numberToGuess) {
                System.out.println("Too low! Try again.");
            } else if (guess > numberToGuess) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println(" 🎉 Congratulations! You guessed the number in " + numberOfTries + " tries.");
                break; // Exit loop after correct guess
            }
        }

        scanner.close();
        System.out.println("Thanks for playing!");
    }
}
