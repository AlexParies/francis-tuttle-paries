/*
 * Activity 1.2.4
 */
public class DogRunner
{
    
    
  public static void main(String[] args)
  {
    Dog myDog = new Dog("jerry");
    myDog.eat("b e a n s",1.5,3);
    myDog.walk(30,"a park?????");
    myDog.play("toy of some sort");
    myDog.setAge(32);
    myDog.sit();
    myDog.speak();

    Dog Daisy = new Dog("Daisy");
    Daisy.eat("kibble", 2);
   
  }
}