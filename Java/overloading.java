class overloading
{
    //Overloading Function no. 1
    public void num_calc(int num, char ch)
    {
        if(ch=='s')
        {
            num=num*num;
            System.out.println(num);
        }
        else
        {
            num=num*num*num;
            System.out.println(num);
        }
    }

    //Overloading Function no. 2
    public void num_calc(int a, int b, char ch)
    {
        if(ch=='p')
        {
            int c=a*b;
            System.out.println(c);
        }
        else
        {
            int c=a+b;
            System.out.println(c);
        }
    }

    //Overloading Function no. 3
    public void num_calc(String s1, String s2)
    {
        if(s1.equals(s2)==true)
        {
            System.out.println("The two strings are equal.");
        }
        else
        {
            System.out.println("The two strings are not equal.");
        }
    }

    public static void main(String[] args)
    {
        overloading ov=new overloading();
        ov.num_calc(1,2,'p');
    }
}