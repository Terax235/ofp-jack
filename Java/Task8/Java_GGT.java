import java.io.*;

public class Java_GGT {

	public int ggT(int a, int b) {
		int m = a, n = b;
		int r = 1;
		while (r != 0) {
			int t = m;
			m = (t < n ? n : t);
			n = (t < n ? t : n);
			r = m - n;
			m = n;
			n = r;
		}
		return m;
		


	}

	public static void main(String[] args) {
		Java_GGT c = new Java_GGT();
		System.out.println(c.ggT(104, 78));
	}
}