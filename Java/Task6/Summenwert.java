public class Summenwert {
    public static double bruchSumme(int n) {
        double result = 0;
        for (double i = 1; i<=n; i++) {
            double div = (1/i);
            result += div;
        }
        return result;
    }
}