import java.util.Scanner;
public class IfElse {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter integer: ");
		int Num = scan.nextInt();
		
		boolean valid;
		
		if(Num > 0) {
			valid = true;
			System.out.println("num is valid");
		}else {
			valid = false;
		}
		
		System.out.println(valid);
		
		
		
		
		scan.close();
	}

	
}
