package Java.Task9;

public class Radio {
	public boolean eingeschaltet;
	public int lautstaerke;
	public double frequenz;

	public Radio() {
		eingeschaltet = true;
		lautstaerke = 5;
		frequenz = 99.9;
	}

	public Radio(boolean istAn, int lautstaerke, double frequenz) {
		eingeschaltet = istAn;
		this.lautstaerke = lautstaerke;
		this.frequenz = frequenz;
	}

	public void lauter(int h) {
		int newVolume = h + lautstaerke;
		if (eingeschaltet && newVolume <= 10) {
			lautstaerke = newVolume;
		}
	}

	public void leiser(int h) {
		int newVolume = h - lautstaerke;
		if (eingeschaltet && newVolume >= 0) {
			lautstaerke = newVolume;
		}
	}

	public void an() {
		eingeschaltet = true;
	}

	public void aus() {
		eingeschaltet = false;
	}

	public String toString() {
		String mode = eingeschaltet ? "an" : "aus";
		return "Radio " + mode + ": Freq=" + frequenz + ", Laut=" + lautstaerke;
	}

	public void waehleSender(double frequenz) {
		if (frequenz > 110.0 || frequenz < 85.0) {
			this.frequenz = 99.9;
		} else {
			this.frequenz = frequenz;
		}
	}
}