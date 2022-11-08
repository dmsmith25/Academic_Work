public class Debug2 {

	public static void main(String[] args){
		
		method1();
		
	}
	
	public static void method1()
	{
		method2();
		
	}
	
	
	public static void method2()
	{
		method3();
	}
	
	public static void method3()
	{
		int i=0; 
		int j=0;
		int k=0;
		int[] array = new int[10];
		int index = 0;
	
		while( i >=k && k<=j && j+k>=i){
			i+=2;
			k++;
			j=k+1;
			
			
			array[index] = i+j+k;	
			
			if(i > 1000){
				i=0;
				j=0;
				k=0;
			}
			
	
			index++;
			
			
		}
	}
	
}
