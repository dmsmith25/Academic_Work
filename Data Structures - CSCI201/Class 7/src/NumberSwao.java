
public class NumberSwao {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int num1, num2;
		
		num1 = 100;
		num2 = 200;
		
		System.out.println("before swap() n1: " + num1 + " n2: " + num2);
		
		swap(num1,num2);
		
		System.out.println("after swap() n1: " + num1 + " n2: " + num2);
		
		System.out.println("______________________");
		
		Number numb1 = new Number(100);
		Number numb2 = new Number(200);
		
		System.out.println("before swap2() n1: " + numb1.value + " n2: " + numb2.value);
		
		swap2(numb1,numb2);
		
		System.out.println("after swap2() n1: " + numb1.value + " n2: " + numb2.value);

	}
	
	public static void swap(int n1, int n2) {
		int temp = n1;
		n1 = n2;
		n2 = temp;
		
		System.out.println("in swap() n1: " + n1 + " n2: " + n2);
		
	}
	
	public static void swap2(Number n1, Number n2) {
		int temp = n1.value;
		n1.value = n2.value;
		n2.value = temp;
		
		
		System.out.println("in swap2() n1: " + n1.value + " n2: " + n2.value);
		
	}

}
