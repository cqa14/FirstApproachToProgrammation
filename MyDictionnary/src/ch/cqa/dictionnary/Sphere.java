package ch.cqa.dictionnary;

public class Sphere extends Form {
	
	//sous-classe heritage

	public Sphere() {
		super("sphery");
		// TODO Auto-generated constructor stub
	}

	@Override
	public String figure() {
		// TODO Auto-generated method stub
		return "sphere";
	}

	@Override
	public int cote() {
		// TODO Auto-generated method stub
		return 1;
	}

	@Override
	public boolean circle() {
		// TODO Auto-generated method stub
		return true;
	}

}
