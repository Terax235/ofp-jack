package Java.Task9;

public class Konto {
	public String vorname;
	public String name;
	public String iban;
	public double kontostand;
	public double limit;

	public Konto(String Vorname, String Name, String kontonummer) {
		vorname = Vorname;
		name = Name;
		iban = kontonummer;
		kontostand = 0;
		limit = 0;
	}

	public String toString() {
		return "Kunde: " + vorname + " " + name + ", Konto: " + iban + ", Stand: " + kontostand + ", Limit: " + limit;
	}

	public void einzahlen(double betrag) {
		kontostand += betrag;
	}

	public double auszahlen(double betrag) {
		if (kontostand - betrag < -limit) {
			betrag = kontostand;
		}
		kontostand -= betrag;
		return betrag;
	}

	public double Kontostand() {
		return kontostand;
	}

	public void setLimit(double limit) {
		this.limit = limit;
	}
}