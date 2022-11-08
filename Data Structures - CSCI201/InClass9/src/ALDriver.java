import java.util.ArrayList;

public class ALDriver {
	
	
	ArrayList<USState> states  = new ArrayList<USState>();
	
	public static ArrayList<USState> prac(String[] arr) {
		
		return new ArrayList<USState>();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] pr = new int[2];
		
		String st = "";
		System.out.println(st.length());
		
		
		
		//ArrayList of USState objects
		ArrayList<USState> states  = new ArrayList<USState>();
		
		
		states.add(new USState("Vermont", "VT"));
		states.add(new USState("New York", "NY"));
		states.add(new USState("Massachusetts", "MA"));
		states.add(new USState("Maine", "ME"));
		
		//increase population of each state by 100
		for(int i=0; i<states.size(); i++)
			states.get(i).increasePopulation(100);

		
		String s = "hello";
		
		//print 
		for(int i=0; i<states.size(); i++)
			System.out.println(states.get(i)+" "+states.get(i).getPopulation());
		
		
		//set some populations to 0
		states.get(0).setPopulation(0); //VT
		states.get(1).setPopulation(0); //NY
		states.get(3).setPopulation(0); //ME
		
		//....
		
		
		//remove all states with population 0
		//(Doesn't work)
		for(int i=0; i<states.size(); i++) {
			if(states.get(i).getPopulation()==0) {
				System.out.println("removing "+states.get(i));
				states.remove(i);
			}
		}
		
		
		
		/*
		//remove all states with population 0
		//first solution: iterating backwards
		for(int i=states.size()-1; i>=0; i--) {
			if(states.get(i).getPopulation()==0) {
				System.out.println("removing: "+states.get(i));
				states.remove(i);
			}
		}
		*/
		
		
		/*
		//remove all states with population 0
		//second solution (i--)
		for(int i=0; i<states.size(); i++) {
			if(states.get(i).getPopulation()==0) {
				System.out.println("removing 2nd way: "+states.get(i));
				states.remove(i);
				i--;
			}
		}
		*/
		
		
		

	}

}
