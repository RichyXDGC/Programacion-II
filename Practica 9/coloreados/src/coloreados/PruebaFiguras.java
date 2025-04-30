package coloreados;
import java.util.Random;

public class PruebaFiguras {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[5];
        Random rand = new Random();
        String[] colores = {"Rojo", "Verde", "Azul", "Amarillo", "Negro"};

        for (int i = 0; i < figuras.length; i++) {
            int tipo = rand.nextInt(2);
            String color = colores[rand.nextInt(colores.length)];
            if (tipo == 0) {
                double lado = 1 + rand.nextInt(10);
                figuras[i] = new Cuadrado(color, lado);
            } else {
                double radio = 1 + rand.nextInt(10);
                figuras[i] = new Circulo(color, radio);
            }
        }

        
        for (Figura f : figuras) {
            System.out.println(f.toString());
            System.out.printf("Área: %.2f\n", f.area());
            System.out.printf("Perímetro: %.2f\n", f.perimetro());
            if (f instanceof Coloreado) {
                Coloreado c = (Coloreado) f;
                System.out.println("Cómo colorear: " + c.comoColorear());
            }
            System.out.println("#########################################");
        }
    }
}
