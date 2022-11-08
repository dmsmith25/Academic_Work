import java.util.Scanner;
import java.util.Random;
public class HiLo {

	
	/* This method prompts the user whether they want to play a number guessing game where the computers
	 * gives the user hints about what value the number is.
	 */
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		
		boolean play_again = true;
		boolean finish;
		int guesses;
		
		// Do loop that prompts the user to start game and finishes when the user quits the game
		do {
			System.out.println("Welcome! Enter integer for end of range (must be > 0): ");
			int max = scan.nextInt();
			
			guesses = 1; // Used to count guesses, starts at 1 because the user must give at least one guess
			finish = false; // Track if user has finished the game
			
			Random rand = new Random(); // Generate random object
			
			int rand_int = rand.nextInt(max) + 1; // Generate the random integer the user is trying to guess
			
			int guess; // initialize the guess the user will make
			
			// while loop carries out the part of the game where the user guesses what the random num is
			while(finish == false) {
				System.out.println("Enter a guess or 0 to quit: ");
				guess = scan.nextInt();
				if (guess == rand_int) {
					System.out.println("Correct! That took you " + guesses + " guesses.");
					finish = true;
				}else if (guess == 0) {
					System.out.println("You quit!");
					finish = true;
				}else if (guess > rand_int){
					System.out.println("Too high");
				}else if (guess < rand_int) {
					System.out.println("Too low");
				}
				
				guesses++;
					
			}
			
			System.out.println("Play again (y/n)?");
			scan.nextLine();
			String response = scan.nextLine();
			
			//Checks to see if user wants to play again and end the do-loop
			if(response.equals("n")) {
				play_again = false;
				System.out.println("Thanks for playing!");
			}
			
			
			
		} while (play_again == true);
		
		
		
		scan.close();
	}

}
