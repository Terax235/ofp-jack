public class ArrayWork {
    public double ArrayFunc(double[] w, int func) {
        switch (func) {
            case 1:
                double min = Integer.MAX_VALUE;
                for (int i = 0; i < w.length; i++) {
                    if (w[i] < min)
                        min = w[i];
                }
                return min;
            case 2:
                double max = Integer.MIN_VALUE;
                for (int i = 0; i < w.length; i++) {
                    if (w[i] > max)
                        max = w[i];
                }
                return max;
            case 3:
                double sum = 0;
                for (int i = 0; i < w.length; i++) {
                    sum += w[i];
                }
                return sum / w.length;
            case 4:
                double m = 0;
                for (int i = 0; i < w.length; i++) {
                    m += w[i];
                }
                m += 0.19 * m;
                return m;
            default:
                return 0;
        }
    }

    public static void main(String[] args) {
        int arg = Integer.parseInt(args[0]);
        ArrayWork aw = new ArrayWork();

        double werte[] = { 1.9, 4.6, 99.0, 12.49, 78.99, 0.5, 56.98, 8.90, 119.90, 2.20 };

        System.out.println(aw.ArrayFunc(werte, arg));
    }
}
