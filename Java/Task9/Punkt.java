package Java.Task9;

public class Punkt {
	public int x;
	public int y;

	public Punkt(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public Punkt() {
		this(0, 0);
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public String toString() {
		return x + "/" + y;
	}

	public Punkt spiegelX() {
		return new Punkt(x, -y);
	}

	public Punkt spiegelY() {
		return new Punkt(-x, y);
	}

	public Punkt spiegelUrsprung() {
		return new Punkt(-x, -y);
	}

	public String diffUrsprung() {
		return x + "/" + y;
	}

	public String diffPunkt(Punkt p) {
		return (x - p.x) + "/" + (y - p.y);
	}
}