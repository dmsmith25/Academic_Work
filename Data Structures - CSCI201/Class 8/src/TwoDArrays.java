import java.util.Random;

public class TwoDArrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int rows = 4;
		int cols = 6;
		
		int[][] arr2d = new int[rows][cols];
		
		Random rand = new Random();
		
		// row-order traversal
		for(int i=0; i< arr2d.length; i++) {
			
			for(int j=0; j<arr2d[0].length; j++) {
				arr2d[i][j] = rand.nextInt(10);
				//System.out.print(arr2d[i][j] + " "); //prints + stays on same line
			}
			//System.out.println();
		}
		
		BenAndJerrys();

	}
	
	public static void BenAndJerrys() {
		
		
		int reviewers = 10;
		int flavors = 5;
		int maxrating = 10;
		
		int[][] arr2d = new int[reviewers][flavors];
		
		Random rand = new Random();
		
		for(int i=0; i< arr2d.length; i++) {
			
			for(int j=0; j<arr2d[0].length; j++) {
				arr2d[i][j] = rand.nextInt(maxrating) + 1;
				System.out.print(arr2d[i][j] + " "); //prints + stays on same line
			}
			System.out.println();
		}
		
		//System.out.println("length: "  + arr2d.length);
		
		for(int i = 0; i < arr2d[0].length; i++) {
			double sum = 0;
			for(int j = 0; j < arr2d.length; j++) {
				sum += arr2d[j][i];
			}
			double avg = sum / arr2d.length;
			System.out.println(avg);
		}
		
		
		
	}

}
