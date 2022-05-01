public class BodyPart{
    String name;
    String mood = "sad";
    public BodyPart(String name){
        this.name = name;
    }

    public void intro(){
        System.out.println("Hello, I am " + this.name + " body part.");
    }
    public void mood(){
        System.out.println(this.name + " is " + this.mood + ".");
    }
}