import java.io.*;

class quiz
{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	//Football Questions and Football answers

	String[] football={"Who won the Premier League in 2019?", "Who is the highest paid manager in the world?", "Who is the captain of Tottenham Hotspur?", "Which country won the first ever World Cup?", "Who won the golden glove in the 2019 PL season?"};
	String[] footballans={"Liverpool", "Jose Mourinho", "Hugo Lloris", "Uruguay", "Ederson"};

	//Formula 1 Questions and Formula 1 answers
	String[] formula={"Who is the highest paid driver?", "Who was the youngest driver to win a race?", "Name the only American F1 constructor.", "which streaming service documented the season?", "Name the only current Asian driver."};	
	String[] formulaans={"Lewis Hamilton", "Max Verstappen", "Haas", "Netflix", "Alex Albon"};
	
	//Music Questions and Music answers
	String[] music={"Which band recorded the album Abbey Road?", "Who was the drummer for the band The Beatles?", "Name the lead singer of the band Nirvana", "Which country is the band AC/DC from?", "Which is the highest selling album in history?"};
	String[] musicans={"The Beatles", "Ringo Starr", "Kurt Cobain", "Australia", "Thriller"};


	public void func()throws IOException, NumberFormatException
	{
		System.out.println("\t\t\t\tQUIZ\n");
		System.out.println("Choose your category-\n1]Football\n2]Formula 1\n3]Music\n");
		System.out.print("==> ");
		int choice=Integer.parseInt(br.readLine());

		int marks=0;

		//Football Condition
		if(choice==1)
		{
			System.out.println("\t\t\t\t Football \n");
			for(int ctr=1;ctr<=5;ctr++)
			{
				System.out.println("Q" + ctr + ") " + football[ctr-1]);
				System.out.print("==> ");
				String ans=br.readLine();

				if(ans.equalsIgnoreCase(footballans[ctr-1]))
				{
					System.out.println("\n That's correct. Good job! \n");
					marks++;
				}
				else
				{
					System.out.println("\n You have no brains. Educate yourself. \n");
				}
			}
		}

		//Formula 1 Condition
		if(choice==2)
		{
			System.out.println("\t\t\t\t  Formula 1 \n");
			for(int ctr=1;ctr<=5;ctr++)
			{
				System.out.println("Q" + ctr + ") " + formula[ctr-1]);
				System.out.print("==> ");
				String ans=br.readLine();

				if(ans.equalsIgnoreCase(formulaans[ctr-1]))
				{
					System.out.println("\nThat's correct. Good job! \n");
					marks++;
				}
				else
				{
					System.out.println("\n You have no brains. Educate yourslef \n");
				}
			}
		}

		//Music Condition
		if(choice==3)
		{
			System.out.println("\t\t\t\t  Music \n");
			for(int ctr=1;ctr<=5;ctr++)
			{
				System.out.println("Q" + ctr + ") " + music[ctr-1]);
				System.out.print("==> ");
				String ans=br.readLine();

				if(ans.equalsIgnoreCase(musicans[ctr-1]))
				{
					System.out.println("\n That's correct. Good job! \n");
					marks++;
				}
				else
				{
					System.out.println("\n You have no brains. Educate yourself. \n");
				}
			}
		}

		//Marks
		System.out.println("\n\n    Your score: " + marks);
	}

	public static void main(String []args)
	{
		quiz q=new quiz();
		try
		{
			q.func();
		}
		catch(IOException ioe)
		{
			System.out.println("Error");
		}
		catch(NumberFormatException nf)
		{
			System.out.println("Error");
		}
	}
}