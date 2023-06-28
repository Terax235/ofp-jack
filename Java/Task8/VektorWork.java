package Java.Task8;

public class VektorWork {
    public int[] addVektor(int[] A, int[] B) {
        int total = (A.length > B.length) ? A.length : B.length;
        int[] C = new int[total];
        for (int i = 0; i < total; i++) {
            int sum = 0;
            if (A.length > i)
                sum += A[i];
            if (B.length > i)
                sum += B[i];
            C[i] = sum;
        }
        return C;
    }

}
