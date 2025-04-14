package diamante;

public class Main {
    public static void main(String[] args) {
    	
        A objA = new A(10, 20);
        B objB = new B(30, 40);
        D objD = new D(50, 60, 70);

        System.out.println("Clase A");
        System.out.println("Antes: x=" + objA.x + ", z=" + objA.z);
        objA.incrementaXZ();
        System.out.println("Después de incrementaXZ(): x=" + objA.x + ", z=" + objA.z);

        System.out.println("\nClase B");
        System.out.println("Antes: y=" + objB.y + ", z=" + objB.z);
        objB.incrementaYZ();
        System.out.println("Después de incrementaYZ(): y=" + objB.y + ", z=" + objB.z);

        System.out.println("\nClase D");
        System.out.println("Antes: x=" + objD.x + ", y=" + objD.getY() + ", z=" + objD.z);
        objD.incrementaXYZ();
        System.out.println("Después de incrementaXYZ(): x=" + objD.x + ", y=" + objD.getY() + ", z=" + objD.z);
    }
}
