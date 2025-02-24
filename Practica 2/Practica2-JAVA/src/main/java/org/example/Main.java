import javax.swing.*;
import java.awt.*;

public class Main extends JPanel {
    private Linea linea;
    private Circulo circulo;

    public Main() {

        Punto p1 = new Punto(100, 100);
        Punto p2 = new Punto(300, 300);


        linea = new Linea(p1, p2);
        circulo = new Circulo(p1, 100);

        System.out.println(linea.toString());
        System.out.println(circulo.toString());

        JFrame frame = new JFrame("Dibujando Línea y Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(this);
        frame.setVisible(true);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        linea.dibujarLinea(g);
        circulo.dibujarCirculo(g);
    }

    public static void main(String[] args) {
        new Main();
    }
}