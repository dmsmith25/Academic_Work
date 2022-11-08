import java.util.Scanner;

public class Arrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		
		// Create an array of size 10 of ints
		int[] heights = new int[10];
		
		//length of array
		System.out.println("length: " + heights.length);
		
		// fill the array
		heights[2] = 72;
		
		int x = 5;
		heights[x] = 61;
		
		//access elements
		int sum = heights[0] + heights[1];
		
		//print the element in the middle
		int mid = heights.length/2;
		System.out.println(heights[mid]);
		
		//Input 5 ints from user and print in reverse
		int[] arr = new int[5];
		
		//Get input
		for(int i = arr.length - 1; i>=0 ;i--) {
			System.out.println("Enter an int: ");
			arr[i] = scan.nextInt();
		}
		System.out.println(arr[1]);
		scan.close();
	}

}
