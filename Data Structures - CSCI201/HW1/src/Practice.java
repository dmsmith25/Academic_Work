
public class Practice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] divis_by4 = new int[1];
		for(var i = 0; i <= 200; i++) {
			float real_val = i/4;
			int int_val = i/4;
			
			if(real_val == int_val) {
				divis_by4[divis_by4.length] = i;
			}
		}
		
		System.out.println(4 == 4.0);

	}

}
