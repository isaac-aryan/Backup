class increment{
	int a=10;
	int b=20;

	public int disp(){
		int c=++a*2;
		int d=a++*2;
		System.out.println("The value of ++a x 2= "+c);
		System.out.println("The value of a++ x 2= "+c);

	}
	public static void main(String[]args){
		increment obj=new increment();
		obj.disp();
	}
}