import java.util.Scanner;

public class Input {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter date: ");
		int date = scan.nextInt();
		scan.nextLine();

		System.out.println("Enter day: ");
		String day = scan.nextLine();
		
		System.out.println("Happy " + date + " " + day);
		
		
		
		
		scan.close();
	}

}
