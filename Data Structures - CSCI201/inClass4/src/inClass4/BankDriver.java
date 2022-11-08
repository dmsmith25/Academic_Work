package inClass4;

public class BankDriver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Scanner scan = new Scanner(...);
		
		BankAccount acct1 = new BankAccount("12345");
		
		acct1.setBalance(100);
		acct1.setName("Dumbledore");
		
		acct1.deposit(50);
		acct1.withdraw(200);
		
		BankAccount acct2 = new BankAccount();
		acct2.setAcctNum("56789");
		
		System.out.println(acct1);

	}

}
