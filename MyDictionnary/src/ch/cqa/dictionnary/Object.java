package ch.cqa.dictionnary;

public class Object {

	//classe de l'objet
	
	private String name = "prout";
	private int size = 1000;
	
	public Object(String name, int size) {
		
		this.name = name;
		this.size = size;
		
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getSize() {
		return size;
	}

	public void setSize(int size) {
		this.size = size;
	}
	
	public void sizeDiffrence(int sizedif) {
		System.out.println(this.size - sizedif);
	}
	
}
