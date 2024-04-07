package ch.cqa.dictionnary;

public class Cube extends Form {
	
	//sous-classe heritage

	public Cube() {
		super("cuby");
		// TODO Auto-generated constructor stub
	}

	@Override
	public String figure() {
		// TODO Auto-generated method stub
		return "cube";	
		}

	@Override
	public int cote() {
		// TODO Auto-generated method stub
		return 6;
	}

	@Override
	public boolean circle() {
		// TODO Auto-generated method stub
		return false;
	}

}
