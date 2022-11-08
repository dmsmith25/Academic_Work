/*
 * Dean Smith
 * HW3
 * Section Y
 * 
 * I have neither given nor received unauthorized aid on this assignment. - Dean Smith
 */

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
public class SixDegreeDriver {
	
	static ArrayList<Person> peeps = new ArrayList<Person>();
	static ArrayList<String> ques = new ArrayList<String>();

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		ques.add("Queries:");
		Scanner scan = new Scanner(System.in);
		System.out.println("** Six Degree of Separation **");
		readFile("friends.txt");
		ArrayList<String> nameList = setNameList();
		System.out.println("File Reading Complete.");
		boolean done = false;
		String person1 = "";
		String person2 = "";
		
		while(done == false) {
			boolean validPers1 = false;
			while(validPers1 == false){
				System.out.println("Enter the name of the first person: ");
				person1 = scan.nextLine();
				
				if(nameList.contains(person1) == true) {
					validPers1 = true;
				}else {
					System.out.println("Error: " + person1 + " is not in the list.");
				}
			}
			boolean validPers2 = false;
			while(validPers2 == false){
				System.out.println("Enter the name of the second person: ");
				person2 = scan.nextLine();
				
				if(nameList.contains(person2) == true) {
					validPers2 = true;
				}else {
					System.out.println("Error: " + person2 + " is not in the list.");
				}
			}
			ArrayList<String> newChain = findConnection(person1, person2);
			String chain = "";
			
			if(newChain.size() != 0) {
				System.out.println("Relation:");
				for(var i = 0; i < newChain.size(); i++) {
					if (i > 0) {
						chain += " " + newChain.get(i);
					}
					else {
						chain += newChain.get(i);
					}
				}
				ques.add(chain);
				System.out.println(chain);
				int degSep = newChain.size() - 1;
				System.out.println("Degrees of Seperation: " + degSep );
			}else {
				System.out.println("The two people entered are not connected.");
			}
			
			System.out.println("Want to try another query? (y/n) ");
			String resp = scan.nextLine();
			resetPred();
			
			if(resp.equals("n")) {
				done = true;
			}
		}
		
		
		System.out.println("Computing Average Degree of Separation...");
		System.out.println("Average Degree of Separation: " + getAvg());
		writeFile(ques);
		

	}
	
	// This method resets the expolored and predessesor for all peeps
	public static void resetPred() {
		for(int i = 0; i < peeps.size(); i++) {
			peeps.get(i).setExplored(false);
			peeps.get(i).setPredecessor("");
		}
	}
	
	// This method returns the average of the total peeps connection length
	public static float getAvg() {
		int peepSum = 0;
		int counter = 0;
		for(int i = 0; i < peeps.size(); i++) {
			for (int j = 0; j < peeps.size(); j ++) {
				if(j != i) {
					int size;
					if ((findConnection(peeps.get(i).getName(), peeps.get(j).getName()).size() != 0)) {
						size = findConnection(peeps.get(i).getName(), peeps.get(j).getName()).size() - 1;
					}else {
						size = peeps.size() + 1;
					}
					peepSum += size;
					counter++;
				}
					
			}
		}
		float peepSumFlt = peepSum;
		float counterFlt = counter;
		float avg = peepSumFlt / counterFlt;
		
		return avg;
	}
	
	
	// This method returns a list of all the String names of all Person objects in peeps
	public static ArrayList<String> setNameList() {
		ArrayList<String> outputArr = new ArrayList<String>();
		for(int i = 0; i < peeps.size(); i++) {
			outputArr.add(peeps.get(i).getName());
		}
		
		return outputArr;
	}
	
	// This method reads in the friends.txt file
	public static void readFile(String file) throws IOException{
		
		Scanner fr = new Scanner(new File(file));
		
		while(fr.hasNextLine()) {
			
			String line = fr.nextLine();
			String[] names = line.split("\t");
			
			//use first name to create Person
			Person p = new Person(names[0]);
			
			p.setExplored(false);
			
			//rest of names go into friendsList
			for(int i=1; i<names.length; i++) {
				p.getFriendsList().add(names[i]);
				
				
				
			}
			
			peeps.add(p);
			
		}
		
	}
	
	// This file writes the que to the output.txt file
	public static void writeFile(ArrayList<String> line) throws IOException{
		
		//For writing to a file
		String outfile = "output.txt";
		BufferedWriter out = new BufferedWriter(new FileWriter(outfile));
		System.out.println(line.size());
		
		for(int i = 0; i < line.size(); i++) {
			out.write(line.get(i)+"\n");
		}
		out.write("Average Degree of Separation of entire group: " + getAvg());
		out.close();
		
	}
	
	
	// This method inputs a name and returns the person object for that name
	public static Person strToObj(String n) {
		Person p = null;
		for(int i = 0; i < peeps.size(); i++) {
			if(peeps.get(i).getName().equals(n)) {
				p = peeps.get(i);
			}
		}
		
		return p;
	}
	
	// This method finds the connection between the two people input
	public static ArrayList<String> findConnection(String n1, String n2) {
		Person p1 = strToObj(n1);
		Person p2 = strToObj(n2);
		ArrayList<String> chain = new ArrayList<String>();
		resetPred();
		
		
		boolean found = false;
		
		ArrayList<Person> ExploreList = new ArrayList<Person>();
		ExploreList.clear();
		
		ExploreList.add(p1);
		p1.setExplored(true);
		
		Person nextP = p1;

		

		while(found == false) {
			if(nextP == p2) {
				found = true;
			}else {
				for(int i = 0; i < nextP.getFriendsList().size(); i++) {
					String friend = nextP.getFriendsList().get(i);
					Person desc = strToObj(friend);
					if((desc.getExplored() == false)) {
						ExploreList.add(desc);
						desc.setExplored(true);
						if(desc != p1) {
							desc.setPredecessor(nextP.getName());
						}
					}
			
				}
				
				
				if(ExploreList.indexOf(nextP) + 1 == ExploreList.size()) {
					return chain;
				}
				
				nextP = ExploreList.get(ExploreList.indexOf(nextP) + 1);
				
				
			}
			
			
		}
		
		boolean chainFinish = false;
		Person prevPers = p2;
		chain.add(p2.getName());
		
		while(chainFinish == false) {
			chain.add(prevPers.getPredecessor());
			
			
			
			if(prevPers.getPredecessor() == p1.getName()) {
				chainFinish = true;
			}else {
				prevPers = strToObj(prevPers.getPredecessor());
			}
		}
		
		
		ArrayList<String> subChain = new ArrayList<String>();
		
		for(var i = 0; i < chain.size(); i++) {
			subChain.add(chain.get(chain.size() - (i + 1)));
		}
		
		return subChain;
		
	}
	
	

}
