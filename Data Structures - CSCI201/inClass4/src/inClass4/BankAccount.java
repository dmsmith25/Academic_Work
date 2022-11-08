package inClass4;

public class BankAccount {

	
	//data fields - global scope
	private String acctNum, name;
	private double balance;
	final double AMOUNT = 20; //final: value cannot be changed
	
	//constructor - for creating a BankAccount
	public BankAccount(String num) //typically an attribute that is unique to each object
	{
		acctNum = num;
		
		this.acctNum = num; //equivalent to above line explicitly states that acctNum is a data field of this class
		
	}
	
	//empty constructor - no parameters
	public BankAccount() {
			
	}
	
	public BankAccount() {
		
	}
	
	public double getBalance()
	{
		return this.balance;
	}
	
	public void withdraw(double amt) {
		this.balance -= amt;
	}
	
	//method overloading
	public void withdraw() {
		this.balance -= 20;
	}
	
	public void deposit(double amt) {
		this.balance += amt;
	}
	
	//returns String of info about this object
	public String toString() {
		return this.acctNum+" "+this.name+" "+this.balance;
	}
	
	//setter for acctNum
	public void setAcctNum(String n) {
		n = '9'+n;
		
		this.acctNum = n;
	}
	
	//setter for name
	public void setName(String n) {
		this.name = n;
	}

	
	//setter for balance
	public void setBalance(double b) {
		this.balance = b;
	}
	
	
}
