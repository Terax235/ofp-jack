import java.lang.Math;

public class Schach {

    public int felder(int cent) {
        //Ihre Lösung!!
        //Rückgabe: Anzahl der Felder
        int felder = 0;
        double p = 0.0;
        while (p < cent) {
            p = Math.pow(2, felder);
            felder++;
        }
        if (felder == 0) return 0;
        return felder - 1;
    }

    public static void main(String[] args) {
        Schach koenigSchach = new Schach();

        int centStuecke = 1000; //Ausgabe muss bei 1000 Centstücken 9 sein.

        System.out.println(koenigSchach.felder(centStuecke));

    }
}