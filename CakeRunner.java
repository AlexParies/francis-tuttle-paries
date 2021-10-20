/*
* Activity 1.2.3
*/
public class CakeRunner
{
  public static void main(String[] args)
  {
    System.out.println("My cake:");
    Cake myCake = new Cake();
    myCake.twoTiers();
    myCake.addCandles();
    myCake.show();
    System.out.println("Your cake");
    Cake yourCake = new Cake();
    yourCake.threeTiers();
    yourCake.show();  
    System.out.println("Another cake");
    Cake anotherCake = new Cake();
    anotherCake.show();
    }
}
