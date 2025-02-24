import java.awt.Graphics;

public class Circulo {
    private Punto centro;
    private float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public String toString() {
        return "Círculo con centro en " + centro + " y radio " + String.format("%.2f", radio);
    }

    public void dibujarCirculo(Graphics g) {
        g.drawOval((int) (centro.x - radio), (int) (centro.y - radio), (int) (2 * radio), (int) (2 * radio));
    }
}