import java.util.Map;
import java.util.HashMap;

public class HandWashingTechnique{
   Map<String, String> techniques = new HashMap<String, String>();
    private boolean flag = false;
    String step0 = "water";
    String step1 = "soap";
    String step2 = "palm";
    String step3 = "interlaced";
    String step4 = "fingers";
    String step5 = "wrist";
    String step6 = "rinse";
    String step7 = "dry";



    public void loadTechinique(){
        String chunk0 = "0: Wet hands with water.";
        String chunk1 = "1: Apply soap.";
        String chunk2 = "2: Rub hands palms to palms.";
        String chunk3 = "3: Rub the back of each hands with fingers interlaced.\n Rub palms together with fingers interlaced.";
        String chunk4 = "4: Rub with back of fingers to the opposing palms.\nRub each thumb clasped in opposite hands.\nRub the tips of fingers.";
        String chunk5 = "5: Rub each wrist with different hands.";
        String chunk6 = "6: Rise with water.";
        String chunk7 = "7: Dry thoroughly your hands.";

        techniques.put("water", chunk0);
        techniques.put("soap", chunk1);
        techniques.put("palm", chunk2);
        techniques.put("interlaced",chunk3);
        techniques.put("fingers", chunk4);
        techniques.put("wrist", chunk5);
        techniques.put("rinse", chunk6);
        techniques.put("dry", chunk7);
    }

   public void water(){
       System.out.println(techniques.get(step0));
   }
   public void soap(){
       System.out.println(techniques.get(step1));
   }
   public void palm(){
       System.out.println(techniques.get(step2));
   }
   public void interlaced(){
       System.out.println(techniques.get(step3));

   }
   public void fingers(){
        System.out.println(techniques.get(step4));
   }
   public void wrist(){
        System.out.println(techniques.get(step5));
   }
   public void rinse(){
       System.out.println(techniques.get(step6));
   }
   public void dry(){
       System.out.println(techniques.get(step7));
       flag = true;
       loadTechinique();
   }
   public void divider(){
       System.out.println("********************");
   }
   public void handWashingAction(){
        loadTechinique();
        water();
        divider();
        soap();
        divider();
        palm();
        divider();
        interlaced();
        divider();
        fingers();
        divider();
        wrist();
        divider();
        rinse();
        divider();
        dry();
   }

}