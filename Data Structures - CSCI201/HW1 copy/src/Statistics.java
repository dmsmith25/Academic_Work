import java.util.Scanner;

public class Statistics {
	
	/*
	 * This method uses other methods to prompt the user for a set of integers and will perform
	 * statistical operations on the data and inform the user.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in); // initialize scanner for main method
		
		Statistics array = new Statistics(); // create object in which other methods can be used on data
		
		boolean quit = false; // track whether the user has quit or not to end the do-loop
		do {
			System.out.println("Enter positive integers(1) or quit(0)?");
			int response = scan.nextInt();
			
			if(response == 1) {
				System.out.println("How many positive integers would you like to enter?");
				int size = scan.nextInt(); // get size of data set
				int[] data = array.getIntegers(size); // declare data set by using "getIntegetrs method to gather data set from user
				boolean stat_quit = false; // track whether the user has quit the use of this data set
				do {
					
					System.out.println("Please choose an option:\n(1)average\n(2)maximum\n(3)minimum\n(4)range\n(5)mode\n(0)quit");
					int stat_type = scan.nextInt(); // get which statistical operation the user wants the code to perform
					
					if(stat_type == 1) {
						System.out.println("Average is: " + array.getAverage(data)); // uses "getAverage" method to calculate the mean of the data set
					}else if(stat_type == 2) {
						System.out.println("Max is: " + array.getMax(data)); // uses "getMax" method to calculate the maximum value of the data set
					}else if(stat_type == 3) {
						System.out.println("Min is: " + array.getMin(data)); // uses "getMin" method to calculate the minimum value of the data set
					}else if(stat_type == 4) {
						System.out.println("Range is: " + array.getRange(data)); // uses "getRange" method to calculate the range of the data set
					}else if(stat_type == 5) {
						System.out.println("Mode is: " + array.getMode(data)); // uses "getMode" method to calculate the mode of the data set
					}else if(stat_type == 0) {
						stat_quit = true;
					}
					
				}while( stat_quit == false);
			}else if (response == 0) {
				quit = true;
			}
			
			
		}while(quit == false);
		
		System.out.println("Goodbye!");
		
		scan.close();
		
		

	}
	
	// This method gathers integers from user and returns an array this size of which is a parameter
	public int[] getIntegers(int num) {
		Scanner scan = new Scanner(System.in); // initialize scanner
		int[] data = new int[num]; // declare array of size 
		for(var i = 0; i < data.length; i++) {
			System.out.println("Please enter integer " + (i + 1));
			int next_int = scan.nextInt();
			data[i] = next_int; // adds each integer to array
		}
		
		
		return data;
		
		
	}
	
	// This method returns the average of an input array of integers
	public float getAverage(int[] data) {
		float average = 0; // declare average
		
		for(var i = 0; i < data.length; i++) {
			average += data[i];
		}
		
		average = average / data.length;
		
		return average;
	}
	
	// This method returns the maximum value in an input array of integers
	public int getMax(int[] data) {
		int max = data[0]; // declare max
		for(var i = 0; i < data.length; i++) {
			if(data[i] > max) {
				max = data[i];
			}
		}
		return max;
	}
	
	// This method returns the minimum value in an input array of integers
	public int getMin(int[] data) {
		int min = data[0]; // declares min
		for(var i = 0; i < data.length; i++) {
			if(data[i] < min) {
				min = data[i];
			}
		}
		return min;
	}
	
	// This method returns the range of an input array of integers
	public int getRange(int[] data) {
		Statistics array = new Statistics(); // generates new Statistics object to use other methods
		int range = array.getMax(data) - array.getMin(data); // uses "getMax" and "getMin" to calculate the range of the data
		return range;
	}
	
	// This method returns the mode of an input array of integers
	public int getMode(int[] data) {
		Statistics array = new Statistics(); // generates new Statistics object to use other methods
		int max = array.getMax(data); // initialize max by using the "getMax" method
		int[] freq_array = new int[max + 1]; // creates frequency array where the index corresponds to the value in the input array
		for(var i = 0; i < data.length; i++) {
			freq_array[data[i]] += 1;
		}
		
		int freq = array.getMax(freq_array); // initialize freq find the value with the most occurrences 
		int mode = 0;
		
		// This loop corresponds the location of the freq to value in the input array
		for(var i = 0; i < freq_array.length; i++) {
			if(freq == freq_array[i]) {
				mode = i;
			}
		}
		
		return mode;
	}
	
	

}
