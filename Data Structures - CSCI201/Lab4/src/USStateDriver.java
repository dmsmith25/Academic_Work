
public class USStateDriver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		USState st1 = new USState("Vermont", "VT");
		
		st1.setPopulation(620000);
		st1.addNeighbor("Massachusetts");
		st1.addNeighbor("New York");
		
		String neigh = st1.getNeighbors();
		int numneigh = st1.getNumNeighbors();
		
		

	}

}
