import java.util.Scanner;
import java.io.*;
public class ReadWrite {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		
		Scanner fr = new Scanner(new File("File1.txt"));
		
		// Read + print every word in file
		while(fr.hasNext()) {
			System.out.println(fr.next());
		}
		
		
		
		
		
		
		fr.close();
		
		readFile();
		
		writeFile();

	}
	
	public static void readFile()throws IOException{
		
		Scanner fr = new Scanner(new File("deposits.txt"));
		
		//For writing to a file
		String outfile = "output.txt";
		BufferedWriter out = new BufferedWriter(new FileWriter(outfile));
		
		//read names + deposits
		while(fr.hasNext()) {
			String name = fr.nextLine();
			int dep = fr.nextInt();
			out.write(dep+"\n");
			fr.nextLine(); // Read and discard new line character
			System.out.println(name+" "+dep);
		}
		
		
		out.close();
		
		
	/*
	 * To Do: Write a method that reads integers from integers from integers.txt
	 * and writes the integers that are > 100 to a seperate file, one per line.
	 */
		
	
		
		
	}
	
	public static void writeFile() throws IOException{
		Scanner fr = new Scanner(new File("integers.txt"));
		
		//For writing to a file
		String outfile = "ints>100.txt";
		BufferedWriter out = new BufferedWriter(new FileWriter(outfile));
		
		while (fr.hasNext()) {
			fr.nextLine();
			while(fr.hasNextInt()) {
				int num = fr.nextInt();
				//System.out.println(num);
				if(num > 100) {
					out.write(num+"\n");
				}
			}
		}
		
		out.close();
		
	}
	

}
