//import numgen.*;
import java.io.*;

class game
{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	public void choose()throws IOException, NumberFormatException
	{
		System.out.println("Choose an option..");
		System.out.println("1] Housie");
		System.out.println("2] OTP");
		System.out.println("3] Generate captcha");
		System.out.println("4] Exit");

		int choice=Integer.parseInt(br.readLine());

		switch(choice)
		{
			case 1: System.out.println("\n");
			housie.playhousie();
			break;
			case 2: System.out.println("\n");
			otp.func();
			break;
			case 3: System.out.println("\n");
			captcha.func();
			break;
			case 4: System.out.println("\nEnding Process..");
			break;
			default: System.out.println("Error");
		}
	}

	public static void main(String[]args)
	{
		game g=new game();

		try{
			g.choose();
		}
		catch(IOException ioe)
		{
			System.out.println("Error");
		}
		catch(NumberFormatException nf)
		{
			System.out.println("Error.");
		}
	}
}