package Uni;

public class Angestellter {
    public double stdProMonat;
    public double geldProStunde;

    public double berechneMonatseinkommen() {
        return stdProMonat * geldProStunde;
    }

    public Angestellter(double arbeitstdProMonat, double gehaltProStunde) {
        stdProMonat = arbeitstdProMonat;
        geldProStunde = gehaltProStunde;
    }

    public Angestellter() {
        stdProMonat = 0;
        geldProStunde = 0;
    }
}
