package inClass4;
import java.util.Scanner;
public class globalString {
	
	static String str; //global scope - accessible by entire program

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter string: ");
		str = scan.nextLine();
		
		System.out.println("Enter char: ");
		char character = scan.nextLine().charAt(0);
		
		int count = getCount(character);
		System.out.println(count);
		
		scan.close();

	}
	
	public static int getCount(char c) {
		
		int count = 0;
		
		for(int i = 0; i < str.length(); i++) {
			if(str.charAt(i) == c) {
				count++;
			}
		}
		
		return count;
		
	}

}
