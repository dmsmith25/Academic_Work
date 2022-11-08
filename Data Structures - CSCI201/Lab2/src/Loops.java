import java.util.Scanner;

public class Loops {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//do-while - executes at least once
		int count = 10;
		do {
			System.out.println(count);
			count++;
			
		}while(count < 5);
		
		System.out.println("do-while done");
		
		
		
		// while - may not execute
		count = 10;
		while (count < 5) {
			System.out.println(count);
			count++;
		}
		
		System.out.println("while done");
		
		//Input 5 ints from user, print sum
		Scanner scan = new Scanner(System.in);
		
		int sum = 0;
		
		for(int i=0; i<5; i++) {
			
			System.out.println("Enter num: ");
			sum += scan.nextInt();
		}
		
		System.out.println(sum);
		
		// Nested loop
		count = 0;
		int i=0;
		
		while(i < 10) { //iterates 10 times
			for(int j=20; j>= 0; j--) // iterates 21 times
				count++;
			
			i++;
			
		}
		
		scan.close();
	}

}
