package practica9;

public class Galeria extends Boleto {
    private int diasAnticipacion;

    public Galeria(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }

    @Override
    public double obtenerPrecio() {
        return diasAnticipacion >= 10 ? 25.0 : 30.0;
    }
}