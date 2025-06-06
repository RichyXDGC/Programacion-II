package coloreados;

public abstract class Figura {
    protected String color;

    public Figura(String color) {
        this.color = color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double area();
    public abstract double perimetro();

    @Override
    public String toString() {
        return "Color: " + color;
    }
}
