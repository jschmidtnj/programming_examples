//*******************************************************
// Account.java
//
// A bank account class with methods to deposit to, withdraw from,
// change the name on, charge a fee to, and print a summary of the account.
//*******************************************************

public class Account
{
	private double balance;
	private String name;
	private long acctNum;
	private int dayNum;
	private static int numAccounts;
	private static int numDeposits;
	private static double totalAmount;
	private static int numWithdrawals;
	private static int totalDeposits;
	private static double totalWithdrawals; //whenever you want something to stay the same in all methods and not change,
	//you use static. when you want the value of the object to change, you do not use static - they are also 0 by default

	//----------------------------------------------
	//Constructor -- initializes balance, owner, and account number
	//----------------------------------------------
	public Account(double initBal, String owner, long number)
	{
		balance = initBal;
		name = owner;
		acctNum = number;
		numAccounts++;
	}

	//----------------------------------------------
	// Checks to see if balance is sufficient for withdrawal.
	// If so, decrements balance by amount; if not, prints message.
	//----------------------------------------------
	public void resetAccounts()
	{
		numDeposits = 0;
		totalAmount = 0;
		numWithdrawals = 0;
		totalWithdrawals = 0;
		dayNum = 0;
		totalDeposits = 0;
	}
	
	public void newDay()
	{
		dayNum++;
		resetAccounts();
	}
	
	public int getDayNum()
	{
		return dayNum;
	}
	
	public void withdraw(double amount)
	{
		if (balance >= amount)
			balance -= amount;
		else
			System.out.println("Insufficient funds");
		
		numWithdrawals++;
		totalWithdrawals+=amount;
	}
	
	//----------------------------------------------
	// Adds deposit amount to balance.
	//----------------------------------------------
	public void deposit(double amount)
	{
		balance += amount;
		numDeposits++;
		totalAmount+=amount;
		totalDeposits+=amount;
	}
	// get info. on deposits and withdrawals
	public static int getDeposits()
	{
		return totalDeposits;
	}
	
	public static double getNumDeposits()
	{
		return numDeposits;
	}
	
	public static int getNumWithdrawals()
	{
		return numWithdrawals;
	}
	
	public static double getTotalWithdrawals()
	{
		return totalWithdrawals;
	}
	
	//----------------------------------------------
	// Returns balance.
	//----------------------------------------------
	public double getBalance()
	{
		return balance;
	}

	public static int getNumAccounts()
	{
		return numAccounts;
	}

	//----------------------------------------------
	// Returns a string containing the name, account number, and balance.
	//----------------------------------------------
	public String toString()
	{
		return "name " + name + " account number " + acctNum + " balance " + balance + "\n";
	}

	//----------------------------------------------
	// Deducts $10 service fee
	//----------------------------------------------
	public double chargeFee()
	{
		balance = balance - 10;
		return balance;
	}

	//----------------------------------------------
	// Changes the name on the account 
	//----------------------------------------------
	public void changeName(String newName)

	{
		name = newName;
	}

	public void close()
	{
		name = "CLOSED";
		balance = 0;
		numAccounts--;
	}

	public String getName()
	{
		return name;
	}

	public long getAccountNum()
	{
		return acctNum;
	}

	public static Account consolidate(Account acct1, Account acct2)
	{
		if ((acct1.getName()).equals(acct2.getName()) && acct1.getAccountNum() == acct2.getAccountNum())
		{
			Account acct50 = new Account(((acct1.getBalance() + acct2.getBalance())/2), acct1.getName(), 55);
			return acct50;
		}
		else {
			System.out.println("You cannot create an account with the same account number or "
					+ "consolidate two accounts with different names.");
			return null;
		}
	}
	public static void transfer(Account acct3, Account acct4, double amount)
	{
		acct3.withdraw(amount);
		acct4.deposit(amount);
	}

}