

public class Debug {

	public static void main(String[] args){
		
		int i=0; 
		int j=0;
		int k=0;
		
		while( i >=k && k<=j && j+k>=i){
						
			i+=2;
			k++;
			j=k+1;
			
			
			
			
			if(i > 1000){
				i=0;
				j=0;
				k=0;
			}
			
			System.out.println("i: "+i);
			System.out.println("j: "+j);
			System.out.println("k: "+k);
			
			
		}
	
	
	}
	
}
