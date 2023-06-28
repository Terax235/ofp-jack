class Alter {
	public String gibBezeichnung(int Alter) {
		if (Alter > 0 && Alter < 18)
			return "Du bist ja noch ein Kind!";
		if (Alter >= 18 && Alter < 67)
			return "Du stehst mitten im Leben!";
		if (Alter >= 67)
			return "Als Rentner hat man es gut!";
		return "Mit Deinem Alter stimmt was nicht!";
	}

	public static void main(String args[]) {
		Alter alterBezeichnung = new Alter();
		System.out.println(alterBezeichnung.gibBezeichnung(44));
	}
}