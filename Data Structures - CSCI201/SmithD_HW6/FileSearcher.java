/*
 * I have neither given nor received unauthorized aid on this assignment.
 * - Dean Smith
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class FileSearcher {
	

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		
		BinarySearchTree<Word> tree = new BinarySearchTree<Word>(); // initialize BST
		
		Scanner scan = new Scanner(System.in);
		
		boolean searching = true;
		
		readFiles(args, tree); // call readFiles method
		
		while(searching == true) {
			System.out.println("Please enter a command (a, s, or q)>>");
			String resp = scan.nextLine();
			
			if(resp.equals("a")) { // if user wants all
				traverse(tree, tree.root); // calls traverse method
				
			} else if (resp.equals("s")) { // if user wants to search
				System.out.println("Word to find>>"); 
				String search = scan.nextLine();
				Word tempWord = new Word(search);
				Word found = tree.find(tempWord);
				if(found != null) { // if word is in tree
					ArrayList<String> files = found.getFiles();
					String fileStr = "";
					for(int i = 0; i < files.size(); i++) {
						fileStr += files.get(i) + " ";
					}
					
					System.out.println("files containing " + found.getWord() + ":  " + fileStr);
				}else { // if word is not in tree
					System.out.println(tempWord.getWord() + " is not found");
				}
				
				
			}else { // if user wants to quit
				searching = false;
			}
		}
		
		

	}
	/*
	 * This method reads in files from the command line and builds the input
	 * Binary Search Tree by making word objects and inserting them into the
	 * tree and the files they were in are associated in the word objects
	 */
	public static void readFiles(String[] s, BinarySearchTree<Word> BST) throws FileNotFoundException {
		for(int i = 0; i < s.length; i++) {
			String fileStr = s[i];
			File file = new File(fileStr);
			
			// if clause
			if(!file.isHidden()&& file.getName().charAt(0)!= '.'){
					
				Scanner fr = new Scanner(file); // Read in file
				String currWord = "";
				while(fr.hasNext()) { // next word (until space)
					String input = fr.next();
					char letter = input.charAt(input.length() - 1); // last char
					if(Character.isLetter(letter) || Character.isDigit(letter)) { //if there is no punct
						currWord = input;
					}else { // if there is punct
						currWord = input.substring(0, input.length() - 1);
					}
					Word w = new Word(currWord); // temporary word object
					if(BST.contains(w) == false){ // if word is not in tree
						w.addFile(fileStr);
						BST.insert(w);
					}else{ // if word is in tree
						Word word = BST.find(w);
						word.addFile(fileStr);
					}
					currWord = "";
				}
			}
		}
	}
	
	/*
	 * This method traverses through every word in the input tree and prints all the words
	 * and what files they are contained in
	 */
	public static void traverse(BinarySearchTree<Word> BST, BinaryNode<Word> t) {
		
		
		if(t != null) { // if current node is null (base case)
			Word wrd = t.element;
			ArrayList<String> files = wrd.getFiles(); // file list for word
			String fileStr = "";
			for(int i = 0; i < files.size(); i++) {
				fileStr += files.get(i) + " ";
			}
			
			System.out.println("files containing " + wrd.getWord() + ":  " + fileStr);
			
			traverse(BST, t.left); //recursive call
			traverse(BST, t.right); // recursive call
		}
		
		
	}

}
