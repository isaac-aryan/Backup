public class Admission
{
  public void cal()
  {
    double math=96.5;
    double phy=99.5;
    double chem=93;
    double bio=99;
    double eng=96;
    double french=97;

    double sum=math+phy+chem+bio+eng+french;
    double average=sum/7;

    System.out.println("Math = "+math);
    System.out.println("Physics = "+phy);
    System.out.println("Chemistry = "+chem);
    System.out.println("Biology = "+bio);
    System.out.println("English = "+eng);
    System.out.println("French = "+french);
    System.out.println("Total = "+sum);
    System.out.println("Average = "+average);

    System.out.println("You have applied to 6 universities");

    if (math>92)
      System.out.println("You are eligible for admission at MIT.");
    else
      System.out.println("MIT rejected you.");

    if (phy>94.5)
      System.out.println("You are eligible for admission at Groningen University.");
    else
      System.out.println("Groningen University rejected you");

    if (chem>90)
      System.out.println("You are eligible for admission at Cavendish University.");
    else
      System.out.println("Cavendish rejected you.");

    if (bio>85.5)
      System.out.println("You are eligible for admission at GMC.");
    else
      System.out.println("GMC rejected you.");

    if (eng>93)
      System.out.println("You are eligible for admission at Oxford University.");
    else
      System.out.println("Oxford University rejected you.");

    if (french>90)
      System.out.println("You are eligible for admission at University Of Lyon.");
    else
      System.out.println("University Of Lyon rejected you.");

        if (math>94 && math<101)
        System.out.println("Congratulations! MIT will provide you with a robotics scholarship! ");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");

        if (phy>95 && phy<101)
        System.out.println("Congratulations! Groningen University will provide you with an Artificial Intelligence scholarship!");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");

        if(chem>92 && chem<101)
        System.out.println("Congratulations! Cavendish University will provide you with a science scholarship!");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");

        if (bio>96 && bio<101)
        System.out.println("Congratulations! GMC is providing you with the DIL SE BHARATI scholarship!");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");

        if (eng>94 && eng<101)
        System.out.println("Congratulations! Oxford University will provide you with an english scholarship!");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");


        if(french>93 && french<101)
        System.out.println("Congratulations! University Of Lyon will provide you with a language scholarship!");
        else
        System.out.println("Sorry, you will not recieve any scholarship!");

  }
  public static void main(String args[])
  {
    Admission obj=new Admission();
    obj.cal();
  }
}
