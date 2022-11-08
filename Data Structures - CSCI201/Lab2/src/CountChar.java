import java.util.Scanner;
public class CountChar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter Phrase: ");
		String phrase = scan.nextLine();
		
		System.out.println("Enter Character: ");
		String letter = scan.next();
		char character = letter.charAt(0);
		scan.nextLine();
		
		int locChar = phrase.indexOf(character);
		

		if(locChar >= 0) {
			
			System.out.println("First " + character + " at index " + locChar);
		
		
		}else {
			System.out.println("No " + character + " in phrase");
		}
		
		
		scan.close();
		
		
		

	}

}
