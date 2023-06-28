package Uni;

public class Uni {
    public static void main(String[] args) throws Exception {
        Angestellter[] personal = new Angestellter[3];
        personal[0] = new Angestellter(22, 11.5);
        personal[1] = new Professor(121.40);
        personal[2] = new Mitarbeiter(40, 15);
        double sum = 0;
        for (int i = 0; i < personal.length; i++) {
            sum += personal[i].berechneMonatseinkommen();
        }
        System.out.println(sum);
    }
}
