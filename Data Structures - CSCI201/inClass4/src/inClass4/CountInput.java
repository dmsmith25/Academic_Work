package inClass4;
import java.util.Scanner;
public class CountInput {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter string: ");
		String str = scan.nextLine();
		
		System.out.println("Enter char: ");
		char character = scan.nextLine().charAt(0);
		
		int count = getCount(str,character);
		System.out.println(count);
		
		scan.close();

	}
	
	public static int getCount(String s, char c) {
		
		int count = 0;
		
		for(int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == c) {
				count++;
			}
		}
		
		return count;
		
	}

}
