package Java.Task9;

public class KFZ {
    public String kennzeichen;
    public int kilometerstand;
    public float tankvolumen;
    public float kraftstoffverbrauch;
    public float kraftstoffmenge;

    public String getKennzeichen() {
        return kennzeichen;
    }

    public int getKMstand() {
        return kilometerstand;
    }

    public float getTankvolumen() {
        return tankvolumen;
    }

    public float getTankinhalt() {
        return kraftstoffmenge;
    }

    public KFZ(String kennzeichen, int kilometerstand, float tankvolumen, float kraftstoffverbrauch,
            float kraftstoffmenge) {
        this.kennzeichen = kennzeichen;
        this.kilometerstand = kilometerstand;
        this.tankvolumen = tankvolumen;
        this.kraftstoffverbrauch = kraftstoffverbrauch;
        this.kraftstoffmenge = kraftstoffmenge;
    }

    public KFZ() {
    }

    public void tanken(float menge) {
        float newTank = kraftstoffmenge + menge;
        kraftstoffmenge = newTank > tankvolumen ? tankvolumen : newTank;
    }

    public boolean fahren(float strecke) {
        float verbrauch = strecke * (kraftstoffverbrauch / 100);
        if (verbrauch > kraftstoffmenge)
            return false;
        kraftstoffmenge -= verbrauch;
        kilometerstand += strecke;
        return true;
    }
}