import java.io.*;
class armstrong
{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	public void check()throws IOException, NumberFormatException
	{
		System.out.println("Enter the number you want to check...");

		int num=Integer.parseInt(br.readLine());
		int acnum=num;
		int total=0;

		while(num>=10)
		{
			int x=num%10;
			num/=10;
			x=x*x*x;
			total+=x;
		}

		num=num*num*num;
		int arm= total+num;

		if(arm==acnum)
		{
			System.out.println(acnum+" is an Armstrong number.");
		}
	}

	public static void main(String[] args)
	{
		armstrong am=new armstrong();

		try
		{
			am.check();
		}

		catch(IOException ioe)
		{
			System.out.println("Input/Output Error");
		}

		catch(NumberFormatException nf)
		{
			System.out.println("Number Format Error.");
		}
	}
}