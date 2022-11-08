import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

/*
 * I have neither given nor received unauthorized aid on this assignment.
 * - Dean Smith
 */



public class TimeTest {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Reading filename from command line.");
		System.out.println(">>" + args[0] + " read"); // File name
		
		boolean stop = false;
		while(stop == false) {
			
			System.out.println();
			System.out.println("      ADT Menu");
			System.out.println("0. Quit\n"
					+ "1. LinkedList (insert at end)\n"
					+ "2. StackArray\n"
					+ "3. StackList\n"
					+ "4. QueueList\n"
					+ "5. ArrayList\n"
					+ "6. array\n"
					+ "Your choice >>");
			int resp = scan.nextInt();
			String file = args[0];
			Scanner fr = new Scanner(new File(file)); // Read in file
			fr.nextLine(); // Skip instructions
			
			String rawData = fr.nextLine(); // Data in string form
			String[] listData = rawData.split(" "); // Make Data into an array
			
			if(resp == 1) {
				System.out.println("CPU time: " + LinkedList(listData));
			}else if(resp == 2){
				System.out.println("CPU time: " + StackArray(listData));
			}else if(resp == 3) {
				System.out.println("CPU time: " + StackList(listData));
			}else if(resp == 4) {
				System.out.println("CPU time: " + QueueList(listData));
			}else if(resp == 5){
				System.out.println("CPU time: " + ArrayList(listData));
			}else if(resp == 6) {
				System.out.println("CPU time: " + Array(listData));
			}else {
				stop = true;
			}
			
			
			
			
			
			 
			
			
			
			
		}
		
		System.out.println("Goodbye!");
		
		

	}
	/*
	 *  This method takes in a string array of instructions which is run through 
	 *  a Queue implemented by a list and returns the runtime
	 */
	public static long QueueList(String[] data) {
		QueueLi test = new QueueLi(); // initialize Queue List
		long start = System.currentTimeMillis(); // start timer for runtime
		for(var i = 0; i < data.length; i++) {
			if(data[i].charAt(0) == 'i') { // if insertion
				int a = data[i].charAt(1);
				test.enqueue(a);
			}else { // if deletion
				test.dequeue();
			}
		}
		long end = System.currentTimeMillis(); // end timer for runtime
		
		return end - start; 
		 
			
	}
	
	/*
	 * This method takes in a string array of instructions which is run through 
	 *  a Stack implemented by a list and returns the runtime
	 */
	public static long StackList(String[] data) {
		StackLi test = new StackLi(); // initialize Stack
		long start = System.currentTimeMillis(); // start runtime timer
		for(var i = 0; i < data.length; i++) { // if insertion
			if(data[i].charAt(0) == 'i') {
				int a = data[i].charAt(1);
				test.push(a);
			}else { // if deletion
				test.pop();
			}
		}
		long end = System.currentTimeMillis(); //end runtime timer
		
		return end - start;
		
	}
	/*
	 * This method takes in a string array of instructions which is run through 
	 *  an ArrayList and returns the runtime
	 */
	public static long ArrayList(String[] data) {
		ArrayList<Integer> test = new ArrayList<Integer>(); // initialize ArrayList
		long start = System.currentTimeMillis(); // start runtime timer
		for(var i = 0; i < data.length; i++) {
			if(data[i].charAt(0) == 'i') { // if insertion
				int a = data[i].charAt(1);
				test.add(a);
			}else { // if deletion
				Integer a = (int) data[i].charAt(1);
				test.remove(a);
			}
		}
		long end = System.currentTimeMillis(); // end runtime timer
		
		return end - start;
	}
	
	/*
	 * This method takes in a string array of instructions which is run through 
	 *  a fixed size Array and returns the runtime
	 */
	public static long Array(String[] data) {
		Integer[] test = new Integer[250000]; // initialize the array with size 250000
		int next = 0; // next empty index in array
		int beg = 0; // beginning index with value
		long start = System.currentTimeMillis();
		for(var i = 0; i < data.length; i++) {
			if(data[i].charAt(0) == 'i') { // if insertion
				int a = data[i].charAt(1);
				test[next] = a;
				next++;
			}else { // if deletion
				int a = data[i].charAt(1);
				for(var j = beg; j < test.length; j++) {
					if(test[j] == a) {
						test[j] = -1;
						if(j == beg) {
							beg++;
						}
						j = test.length; // end loop
					}
				}
				
			}
		}
		long end = System.currentTimeMillis(); // end runtime timer
		
		return end - start;
	}
	
	/*
	 * This method takes in a string array of instructions which is run through 
	 *  a LinkedList and returns the runtime
	 */
	public static long LinkedList(String[] data) {
		LinkedList<Integer> test = new LinkedList<Integer>(); // initialize Linked List
		long start = System.currentTimeMillis(); // start runtime timer
		for(var i = 0; i < data.length; i++) {
			if(data[i].charAt(0) == 'i') { // if insertion
				int a = data[i].charAt(1);
				test.add(a);
			}else { // if deletion
				Integer a = (int) data[i].charAt(1);
				test.remove(a);
			}
		}
		long end = System.currentTimeMillis(); // end runtime timer
		
		return end - start;
	}
	
	/*
	 * This method takes in a string array of instructions which is run through 
	 *  a Stack implemented by an ArrayList and returns the runtime
	 */
	public static long StackArray(String[] data) {
		Stack<Integer> test = new Stack<Integer>(); //initialize Stack
		long start = System.currentTimeMillis(); // 
		for(var i = 0; i < data.length; i++) {
			if(data[i].charAt(0) == 'i') { // if insertion
				int a = data[i].charAt(1);
				test.add(a);
			}else { // if deletion
				Integer a = (int) data[i].charAt(1);
				test.pop();
			}
		}
		long end = System.currentTimeMillis(); // end runtime timer
		
		return end - start;
	}
	

}
