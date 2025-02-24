import java.awt.Graphics;

public class Linea {
    private Punto p1;
    private Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public String toString() {
        return "Línea de " + p1 + " a " + p2;
    }

    public void dibujarLinea(Graphics g) {
        g.drawLine((int) p1.x, (int) p1.y, (int) p2.x, (int) p2.y);
    }
}