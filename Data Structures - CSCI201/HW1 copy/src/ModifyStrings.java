import java.util.Scanner;
public class ModifyStrings {

	/* This method takes a phrase from the user and how many characters of that phrase the user wants to see.
	 * The method then prints a shortened version of the phrase at the length specified by the user. The
	 * method will also inform the user if the phrase is not long enough for the specified number of characters.
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in); // Generate the scanner to take in user input
		
		System.out.println("Enter phrase: ");
		String phrase = scan.nextLine(); // Takes phrase input from user
		
		System.out.println("Enter integer: ");
		int integer = scan.nextInt(); // Takes how many characters of the phrase the user wants to see
		
		
		if(integer <= phrase.length()) {
			
			System.out.println("New phrase: " + phrase.substring(0,integer)); // Prints the shortened phrase
		
		
		}else {
			// In the case that the phrase is not as long as the number specified by the user then the user is notified
			System.out.println("Error: integer exceeds length of string (" + phrase.length() + ")");
		}
		
		scan.close();

	}

}
