/*Encapsulated BankAccount*/

public class BankAccount{
	
	private String acctID; 
	private String acctName; 
	private double balance; 
	private final double AMOUNT = 20;
	
	//empty constructor
	public BankAccount()
	{
		
	}
	
	//non-empty constructor
	public BankAccount(String num)
	{
		acctID = num;
	}
	
	//non-empty constructor
	public BankAccount(String num, String name, double bal)
	{
		acctID = num;
		acctName = name;
		balance = bal;
	}
	
	public void deposit(double bal)
	{
		balance += bal;
	}
	
	public void withdraw(double bal)
	{
		balance -= bal;

	}

	//method overloading
	public void withdraw()
	{
		balance -= AMOUNT;
		
	}
	
	//Setters
	public void setName(String nm)
	{
		acctName = nm;
	}

	
	public void setAcctNum(String num)
	{		
		//convert num to integer

		
		acctID = num;
	}

	public void setBalance(double bal)
	{
		balance = bal;
	}

	
	
	//Getters
	public String getAcctName()
	{
		return acctName;
	}
	
	public String getAcctNum()
	{
		return acctID;
	}
	
		
	public double getBalance()
	{
		return balance;
	}
	
	
	//toString
	public String toString()
	{
		return acctID+" "+acctName+" "+balance;
	}
	

}
