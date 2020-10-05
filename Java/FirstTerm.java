//is a comment
public class Academics
{
  public void calc()
  {
    //Review
      System.out.println("REVIEW");

    double math=18;

    double phy=18;
    double chem=18;
    double bio=18;

    double englit=17.5;
    double englang=18;
    double french=19;

    double hist=18;
    double geo=14;

    System.out.println("Maths marks are "+math);
      System.out.println("Physics marks are "+phy);
        System.out.println("Chemistry marks are "+chem);
          System.out.println("Biology marks are "+bio);
            System.out.println("English Literature marks are "+englit);
              System.out.println("English Language marks are "+englang);
                System.out.println("French marks are "+french);
                  System.out.println("History marks are "+hist);
                    System.out.println("Geography marks are "+geo);

// total marks for review
    double sum=math+phy+chem+bio+englit+englang+french+hist+geo;
      System.out.println("Your total marks out of 180 is "+sum);

//average marks for Review
    double average=sum/10;
      System.out.println("Your average is "+average);

//percentages
  double totalperc=sum/180*100;
  double scienceperc=phy+chem+bio/60*100;
  double langperc=englit+englang+french/60*100;
  double socialsperc=hist+geo/40*100;
  double stemperc=math+phy+chem+bio/80*100;

  System.out.println("Your overall percentage is "+totalperc);
    System.out.println("Your Science percentage is "+scienceperc);
      System.out.println("Your Language percentage is "+langperc);
        System.out.println("Your Social Studies percentage is "+socialsperc);
          System.out.println("Your S.T.E.M percentage is "+stemperc);

//Term Exam
  System.out.println("EXAMS");

  double Math=78;

  double Phy=78;
  double Chem=78;
  double Bio=78;

  double Englit=78;
  double Englang=78;
  double French=78;

  double Hist=78;
  double Geo=78;

  double Mathto=Math+math;
  double Phyto=Phy+phy;
  double Chemto=Chem+chem;
  double Bioto=Bio+bio;
  double Englitto=Englit+englit;
  double Englangto=Englang+englang;
  double Frenchto=French+french;
  double Histto=Hist+hist;
  double Geoto=Geo+geo;

  System.out.println("Maths marks out of 80 are "+Math);
    System.out.println("Physics marks out of 80 are "+Phy);
      System.out.println("Chemistry marks out of 80 are "+Chem);
        System.out.println("Biology marks out of 80 are "+Bio);
          System.out.println("English Literature marks out of 80 are "+Englit);
            System.out.println("English Language marks out of 80 are "+Englang);
              System.out.println("French marks out of 80 are "+French);
                System.out.println("History marks out of 80 are "+Hist);
                  System.out.println("Geography marks out of 80 are "+Geo);

                  System.out.println("Marks out of 100 are as follows:");

                  System.out.println("Maths marks out of 100 are "+Mathto);
                    System.out.println("Physics marks out of 100 are "+Phyto);
                      System.out.println("Chemistry marks out of 100 are "+Chemto);
                        System.out.println("Biology marks out of 100 are "+Bioto);
                          System.out.println("English Literature marks out of 100 are "+Englitto);
                            System.out.println("English Language marks out of 100 are "+Englangto);
                              System.out.println("French marks out of 100 are "+Frenchto);
                                System.out.println("History marks out of 100 are "+Histto);
                                  System.out.println("Geography marks out of 100 are "+Geoto);

//Total marks for Exam
Sum=Mathto+Phyto+Chemto+Bioto+Englitto+Englangto+Frenchto+Histto+Geoto;
  System.out.println("Your total marks out of 900 is "+Sum);

//Average marks for EXAMS
Average=Sum/9;
  System.out.println("Your Exam average is "+Average);

  //percentages
    double Totalperc=Sum/900*100;
    double Scienceperc=Phyto+Chemto+Bioto/300*100;
    double Langperc=Englitto+Englangto+Frenchto/300*100;
    double Socialsperc=Histto+Geoto/200*100;
    double Stemperc=Mathto+Phyto+Chemto+Bioto/400*100;

    System.out.println("Your overall percentage of the exams is "+Totalperc);
      System.out.println("Your Science percentage of the exams is "+Scienceperc);
        System.out.println("Your Language percentage of the exams is "+Langperc);
          System.out.println("Your Social Studies percentage of the exams is "+Socialsperc);
            System.out.println("Your S.T.E.M percentage of the exams is "+Stemperc);
  }
  public static void main(String args[]);
  {
    Academics obj=new Academics();
    obj.cal();
  }
}
