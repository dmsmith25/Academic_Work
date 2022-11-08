/*
 * Dean Smith
 * HW3
 * Section Y
 * 
 * I have neither given nor received unauthorized aid on this assignment. - Dean Smith
 */

import java.util.ArrayList;

public class Person {
	
	private String name;
	private boolean explored;
	private String predecessor; 
	private ArrayList<String> FriendsList = new ArrayList<String>();
	
	public Person(String n){
		this.name = n;
	}
	
	public String getName() {
		return this.name;
	}
	
	public ArrayList<String> getFriendsList(){
		return FriendsList;
	}
	
	public boolean getExplored() {
		return explored;
	}
	
	public void setExplored(boolean bool) {
		this.explored = bool;
	}
	
	public String getPredecessor() {
		return this.predecessor;
	}
	
	public void setPredecessor(String n) {
		this.predecessor = n;
	}
	
	

}
