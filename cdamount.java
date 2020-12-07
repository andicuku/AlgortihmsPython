
import java.util.*;
public class cdamount {
	public static void main(String[] args) {
		double amount;
		double interestrate;
		int numofmonths;
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the intial deposit amount");
		amount = in.nextInt();
		System.out.println("Enter annual percantage yield");
		interestrate = in.nextDouble();
		System.out.println("Enter maturity period (number of months)");
		numofmonths = in.nextInt();
		System.out.println("Month     CD");
		for (int i = 0;i<numofmonths;i++)
		{
			amount = amount + (amount*interestrate/1200);
			System.out.println(i+1+"     "+amount);
		}
		
	}
}
