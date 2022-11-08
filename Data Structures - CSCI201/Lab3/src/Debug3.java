//For Debug Lab

public class Debug3 {

	static int length = 10;
	static int i=0; 
	static int j=0;
	static int k=0;
	static int index = 0;
	
	public static void main(String[] args){
		
	
		method1();
		
		method2();
		
		method3();
	}
		
	public static void method1() {
		//fill first array
		int[] arr = new int[length];
	
		
		while( i >=k && k<=j && j+k<=i){
			
			i+=2;
			k++;
			j=k+1;
		
			arr[index] = i+j+k;	
			
			if(i > 1000){
				i=0;
				j=0;
				k=0;
			}
			index++;
		}
	}

	//fill second array
	public static void method2() {

		int[] arr2 = new int[length];
		
		int i=0;
		int j=0;
		int k=j+1;
		
		
		System.out.println(1);
		
		while(i<arr2.length){
		
			//System.out.println("i: "+i);
			
			k = i+j;
			j= k-2;
			i++;
			
			j*=2;
		}
	}
	
	
	//fill third array
	public static void method3() {
		
		int[] arr3 = new int[length];
		
		for(i=arr3.length-1; i>=arr3.length/2; i--)
		{
			k = 10*i;
			arr3[i] = k%4; 
		}
	}

	
	
	
	
	
}
