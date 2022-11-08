import java.util.Scanner;
public class StatesArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//An array of size 3 of USState objects 
		int[] nums = new int[3];
		
		USState[] states = new USSState[3]; // USState = name of object class
		
		Scanner scan = new Scanner(System.in);
		
		
		for(int i=0; i <states.length; i++) {
			System.out.println("Enter state name: ");
			String n = scan.nextLine();
			
			System.out.println("Enter state abbr: ");
			String a = scan.nextLine();
			
			/*
			USState st = new USState(n, a);
			states[i] = st;
			*/
			// OR
			
			states[i] = new USState(n, a);
			
			states[i].setPopulation(15);
		}
		

	}

}
