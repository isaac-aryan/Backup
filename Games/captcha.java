class captcha
{
	public static void func()
	{
		char[] Arr=new char[6];
		boolean capcheck=false,numcheck=false,alphcheck=false;
		int num,ctr=0;
		System.out.println("\t\t\t\t:- Captcha Code Generator -: ");
		for(int ctr2=0;ctr2<1;)
		{
			for(ctr=0;ctr<Arr.length;)
			{
				int i=(int)(Math.random()*1000);
				int check=0;
				if(i<=122)
				{
					if(i<58 && i>47)
					{
						Arr[ctr]=(char)i;
						ctr++;
						numcheck=true;
					}
					if(i<91 && i>64)
					{
						Arr[ctr]=(char)(i);
						ctr++;
						capcheck=true;
					}
					if(i<123 && i>96)
					{
						Arr[ctr]=(char)(i);
						ctr++;
						alphcheck=true;
					}
				}
			}
			if(numcheck==true && capcheck==true && alphcheck==true)
			{
				break;
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