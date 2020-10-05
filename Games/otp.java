public class otp
{


	public static void func()
	{
	int[] Arr={0,0,0,0,0,0};
	int ctr=0;
		System.out.println("\t\t\t\t:- OTP Generator -: ");
		while(ctr<6)
		{
			int i=(int)(Math.random()*10);
			int check=0;

			if(i<=Arr.length)
			{
				for(int ctr2=0;ctr2<Arr.length;ctr2++)
				{
					if(i!=Arr[ctr2])
					{
						check++;
					}
				}
				if(check==6)
				{
					Arr[ctr]=i;
					ctr++;
				}
			}
		}
		System.out.print("\n=> ");
		for(ctr=0;ctr<Arr.length;ctr++)
		{
			System.out.print(Arr[ctr]);
		}
		System.out.println("\n");
	}

}