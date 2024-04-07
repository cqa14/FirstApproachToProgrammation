package ch.cqa.dictionnary;

public class Main {

	public static void main(String[] args) {
		/*Ceci est un exemple de differents trucs simple 
		 * en java*/
		
		//hello world
		System.out.println("Hello World !");
		
		//variable
		boolean vrai = true;
		boolean faux = false;
		int a = 1;
		int b = 2;
		int c = b - a;
		String nom = "cqa";
		
		//conditions
		if(vrai == faux) {
			//impossible
		} else if("cqa" != nom){
			//impossible
		} else {
			System.out.println("finish");
		}
	
		switch(c) {
		
		case 3:
			System.out.println(" ");
		break;
		
		case 2:
			System.out.println(" ");
		break;
		
		default:
			System.out.println("end");
		break;
		}
		
		//tableaux
		int[] numbers = {1, 2, 3};
		int[][] nb = {{1,2,3},{4,5,6},{0,8,9}};
		
		nb[2][0] = 7;
		
		//boucles
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				System.out.println(nb[i][j]);
			}
		}
		while(c != a + b) {
			c = c + 1;
			System.out.println(c);
		}
		do {
			System.out.println("tut");
		}while(faux != false);
		
		//fonctions
		send("Hello");
		VoidClass.sendMessage();
		
		//objets
		Object object1 = new Object("prout", 20);
		System.out.println(object1.getName());
		
		Object object2 = new Object("gros", 30);
		System.out.println(object2.getName());
		
		object1.sizeDiffrence(object2.getSize());
		
		//heritage
		Cube cubos = new Cube();
		cubos.smiley();
		System.out.println(cubos.figure());
		System.out.println(cubos.getSurname());
		
		Sphere spheros = new Sphere();
		spheros.smiley();
		System.out.println(spheros.figure());
		System.out.println(spheros.getSurname());

	}
	
	//fonction dans la classe
	private static void send(String message) {
		
		System.out.println(message);
		
	}
	
}
