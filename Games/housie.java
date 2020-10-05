import java.io.*;

public class housie
{


	public static void playhousie()throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

		int[] arr=new int[99];
		int ctr=0;
		String tempvar;
		System.out.println("\n\n");
		System.out.println("\t\t\t\t ~HOUSIE~\n\n\n");


		for(ctr=0;ctr<arr.length;ctr++)
		{
			arr[ctr]=0;
		}

		while(ctr<arr.length)
		{
			System.out.println("~Press Enter for the next number~");
			tempvar=br.readLine();
			int i=(int)(Math.random()*100);
			int check=0;

			if(i<=arr.length)
			{
				for(int ctr2=0;ctr2<arr.length;ctr2++)
				{
					if(i!=arr[ctr2])
					{
						check++;
					}
				}
				if(check==99)
				{
					arr[ctr]=i;
					ctr++;
					System.out.println("==> "+i+"\n");
				}
			}
			
		}
	}
}