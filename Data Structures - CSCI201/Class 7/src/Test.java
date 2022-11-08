
public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Mismatch("[()]");

	}
	
	public static void Mismatch(String s) {
		String openS = "([{<";
		
		for(var i = 0; i < s.length(); i++) {
			char character = s.charAt(i);
			if(openS.indexOf(character) > -1) {
				System.out.println(character);
			}
		}
	}

}
