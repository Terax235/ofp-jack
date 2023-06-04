public class Starter {
    public int max(int a, int b) {
        if (a>b) return a;
        else return b; // case b > a OR a == b, both giving the same output
    }

    public static void main(String[] args) {
        Starter s = new Starter();
        System.out.println("Ausgabe: "+s.max(12,13));
    }
}