import java.util.Scanner;
public class TimeConverter {

	/*This method takes the user input for a number of seconds and converts that amount
	 * of seconds into hours, minutes, and seconds.
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in); // initialize scanner
		
		System.out.println("Seconds: ");
		int seconds = scan.nextInt(); // declares value of seconds input by user
		
		int convert_hours = seconds/3600; // declares hours by converting input seconds to hours
		int convert_mins = (seconds - (convert_hours * 3600)) / 60; // converts left over time not included in hours into minutes
		int convert_secs = (seconds - (convert_hours * 3600) - (convert_mins * 60)); // converts left over time from hours and minutes into seconds
		
		// Prints out the full conversion of seconds to hours, minutes, and seconds
		System.out.println(seconds + " second(s) = " + convert_hours + " hour(s), " + convert_mins + " minute(s), " + convert_secs + " second(s)");

		scan.close();
	}

}
