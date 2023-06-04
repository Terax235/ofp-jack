public class Discount {
	public static String berechneRabatt(double betrag) {
        double rabatt = 0.08 * betrag;
        double calculation = Math.round((betrag - rabatt)*100.0)/100.0; // Round to two decimal places
		if (betrag > 1000) return "Betrag mit Rabatt: " + calculation;
        return "Zu zahlender Betrag: " + betrag;	
	}
    public static void main(String[] args)
    {
        double rechnungsBetrag = 0.0;
        rechnungsBetrag = Double.parseDouble(args[0]); // Parse double from command line args
        System.out.println(berechneRabatt(rechnungsBetrag)); 
    }    
}