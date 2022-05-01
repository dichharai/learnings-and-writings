
public class Person{
    String name;
    String mood = ":(";
    public Person(String name){
        this.name = name;
    }
    public void concern(String bodyPartName){
        System.out.println(this.name + " is concerned about " + bodyPartName + " body part.");

    }
    public void mood(){
        System.out.println(this.name + " is " + this.mood + ".");
    }
    public void washHands(){
        HandWashingTechnique hwt = new HandWashingTechnique();
        hwt.handWashingAction();

    }

}