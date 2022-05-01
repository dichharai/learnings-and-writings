public class Main{

	private static Person jane = new Person("Jane Goodwill");
	private static BodyPart bp = new BodyPart("Hands");

	public static void personAction(){
		jane.concern("Hands");
		jane.mood();

	}

	public static void handsBodyPartAction(){
		bp.intro();
		bp.mood();
	}

	public static void peaceTreaty(){
		System.out.println();
		System.out.println("**Peace Treaty**");
		jane.washHands();
		bp.mood = "happy.";
		jane.mood = ":)";
	}

	public static void result(){
		System.out.println();
		System.out.println("**Result**");
		bp.mood();
		jane.mood();

	}
	public static void main(String[] args){
		personAction();
		handsBodyPartAction();
		peaceTreaty();
		result();
	}
}
