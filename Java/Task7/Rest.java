import java.lang.Integer;

public class Rest {
    public String checkModulo(int i, int j) {
        int r = i % j;
        switch (r) {
            case 0:
                return "Der Rest ist null";
            case 2:
            case 3:
            case 5:
            case 7:
                return "Der Rest ist eine einstellige Primzahl";
            default:
                if ((i % j) % 2 != 0)
                    return "Der Rest ist ungerade";
                else
                    return "Keine der Aussagen trifft zu";
        }
    }

    public static void main(String[] args) {
        int i = Integer.parseInt(args[0]);
        int j = Integer.parseInt(args[1]);
        Rest r = new Rest();

        System.out.println(r.checkModulo(i, j));

    }
}
