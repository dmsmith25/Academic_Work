
public class ComparableDriver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		BankAccount acct1 = new BankAccount("12345", "Harry", 500);
		BankAccount acct2 = new BankAccount("67890", "Ron", 5);
		BankAccount acct3 = new BankAccount("11111", "Hermione", 72);
		BankAccount acct4 = new BankAccount("22222", "Ginny", 72000);
		BankAccount acct5 = new BankAccount("33333", "Dumbledore", 1);
		
		BinarySearchTree<BankAccount> tree = new BinarySearchTree<BankAccount>();
		
		tree.insert(acct1);
		tree.insert(acct2);
		tree.insert(acct3);
		tree.insert(acct4);
		tree.insert(acct5);

		tree.printTree(); //inorder

	
	}
	
	
	
		

}
