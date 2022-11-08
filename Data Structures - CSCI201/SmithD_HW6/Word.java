/*
 * I have neither given nor received unauthorized aid on this assignment.
 * - Dean Smith
 */


import java.util.ArrayList;

public class Word implements Comparable<Word>
{
	
	private String word = "";
	private ArrayList<String> files = new ArrayList<String>();
	
	Word(String s){
		this.word = s;
	}
	
	public String getWord() { // getter
		return word;
	}
	
	public void setWord(String s) { // setter
		this.word = s;
	}
	
	public ArrayList<String> getFiles() { // getter
		return files;
	}
	
	public void addFile(String s) {
		files.add(s);
	}

	public int compareTo(Word o) { // must be put in to use BST
		if(this.word.compareTo(o.getWord()) < 0) {
			return -1;
		}else if(this.word.compareTo(o.getWord()) > 0) {
			return 1;
		}else {
			return 0;
		}
	}

}
