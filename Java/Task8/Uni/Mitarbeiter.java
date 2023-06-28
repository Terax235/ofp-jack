package Uni;

public class Mitarbeiter extends Angestellter {
    public Mitarbeiter(double arbeitstdProMonat, double gehaltProStunde) {
        super(arbeitstdProMonat, gehaltProStunde);
    }

    public double berechneMonatseinkommen() {
        return stdProMonat * geldProStunde + 500;
    }
}
