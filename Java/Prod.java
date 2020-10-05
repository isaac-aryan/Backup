//Write a program to enter start number and end number at run time and calculate the product of no.s from start no to end no.

import java.util.*;
public class Prod
{
  public void cal()
  {
    Scanner s=new Scanner(System.in);
    System.out.println("Enter start number..");
    double start=s.nextDouble();
    System.out.println("Enter end number..");
    double end=s.nextDouble();
    double i=start;
    double product=1;
    while (product<= end)
    {
      product=product*1;
      i=i+1;
    }
    System.out.println("Product from "+start+"to"+end+" ="+product);
  }
  public static void main(String args[])
  {
    Prod obj=new Prod();
    obj.cal();
  }
}
