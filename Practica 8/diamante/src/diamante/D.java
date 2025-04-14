package diamante;

public class D extends A {
    private B b;  

    public D(int x, int y, int z) {
        super(x, z); 
        this.b = new B(y, z); 
    }

    public void incrementaXYZ() {
        this.x++;    
        this.b.y++;  
        this.z++;    
    }

    public int getY() {
        return this.b.y;
    }

    public void incrementaZ() {
        super.incrementaZ(); 
        this.b.incrementaZ(); 
    }
}