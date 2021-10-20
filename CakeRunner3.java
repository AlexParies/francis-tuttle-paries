/*
* Activity 1.2.3
*
* Yet another CakeRunner class
*/
public class CakeRunner3
{
  public static void main(String[] args)
  {
    System.out.println("My cake:");
    Cake myCake = new Cake();
    myCake.oneTier();
    myCake.show();
   
    System.out.println("Your cake:");
    Cake yourCake = new Cake();
   
    
    yourCake.show();
  }
}