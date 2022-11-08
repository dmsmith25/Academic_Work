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

	}
	
	public static void readFile()throws IOException{
		
		Scanner fr = new Scanner(new File("deposits.txt"));
		
		
		//read names + deposits
		while(fr.hasNext()) {
			String name = fr.nextLine();
			int dep = fr.nextInt();
			fr.nextLine(); // Read and discard new line character
			System.out.println(name+" "+dep);
		}
		
		
		fr.close();
		
		
		
		
		
	}

}
