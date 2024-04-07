package ch.cqa.dictionnary;

public abstract class Form {
	
	//superclass heritage
	
	private String surname;

	public Form(String surname) {
		this.surname = surname;
	}

	public abstract String figure();
	
	public abstract int cote();
	
	public abstract boolean circle();
	
	public void smiley() {
		System.out.println(":-)");
	}
	
	public String getSurname() {
		return surname;
	}

}
