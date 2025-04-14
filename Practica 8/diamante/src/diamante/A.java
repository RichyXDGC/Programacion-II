package diamante;

public class A {
    public int x;
    public int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        this.x++;
        this.z++;
    }

    public void incrementaZ() {
        this.z++;
    }
}