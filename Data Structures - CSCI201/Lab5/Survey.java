import java.io.*;
import java.util.Scanner;

public class Survey {

	public static int numreviewers = 10;
	public static int numflavors = 5;
	public static int[][] arr;
	
	public static void main(String[] args) throws IOException{
		//Initialize the 2D array to hold the ratings
		arr = new int[numreviewers][numflavors];
		
		//Initialize the file to read from
		String infile = "ratings.txt";
		
		//read the input file and store ratings in arr (declared above)
		readFile(infile);	
		
		//Initialize arrays to hold averages
		double[] avgsperflavor = getAvgPerFlavor();
		double[] avgsperreviewer = getAvgPerReviewer();
			
			
		//Initialize the file to write to		
		String outfile = "averages.txt";
		
		//write the averages stored in avgsperflavor, avgsperreviewer to outfile 
		writeAverages(outfile, avgsperflavor, avgsperreviewer);
				
	}
	

	/**
	 * TO DO
	 * Reads the ratings from file fn and stores values in global array arr
	 * @param fn: file to read
	 * @throws IOException
	 */
	public static void readFile(String fn)
	{
		
	}
	
	/**
	 * TO DO
	 * Computes the average rating for each flavor 
	 * @return double[]: array containing average ratings
	 */
	public static double[] getAvgPerFlavor()
	{
		
	
	}
	
	
	/**
	 * TO DO
	 * Computes the average rating for each reviewer
	 * @return array containing average ratings
	 */
	public static double[] getAvgPerReviewer()
	{
		
	
	}
	
	/**
	 * TO DO
	 * Writes the average ratings per flavor and reviewer to output file named file
	 * @param file: output file to write to
	 * @param avgsflavor: array of average ratings per flavor
	 * @param avgsreviewer: array of average ratings per reviewer
	 * @throws IOException
	 */	
	public static void writeAverages(String file, double[] avgsflavor, double[] avgsreviewer)
	{
		
		
	}
	
	
}
