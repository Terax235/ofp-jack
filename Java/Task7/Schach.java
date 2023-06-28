import java.lang.Math;

public class Schach {

    public int felder(int cent) {
        int felder = 0;
        double p = 0.0;
        while (p < cent) {
            p = Math.pow(2, felder);
            felder++;
        }
        if (felder == 0)
            return 0;
        return felder - 1;
    }

    public static void main(String[] args) {
        Schach koenigSchach = new Schach();

        int centStuecke = 1000;

        System.out.println(koenigSchach.felder(centStuecke));

    }
}