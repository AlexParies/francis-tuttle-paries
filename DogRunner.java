/*
 * Activity 1.2.5
 */
public class DogRunner
{
  public static void main(String[] args)
  {
    Dog d = new Dog("Duke");

    String name = d.getName();
    System.out.println("My name is " + name + " im a dog");
    System.out.println("He is a " + d.isGoodDog() + " good dog.");
    System.out.println(name + " has a new " + d.getToy() +".");
    System.out.println(d.getName()+ " has a new " + d.getToy() +".");
    int hour = d.goOutside();
    int hour2 = d.goOutside()*6;
    System.out.println("duke gous outside for "+hour+" minutes in the morning");
    System.out.println("duke gous outside for "+hour*6+" minutes in the afternoon");
    System.out.println("duke gous outside for "+ hour + 90 +" minutes in the in total");
  }
}