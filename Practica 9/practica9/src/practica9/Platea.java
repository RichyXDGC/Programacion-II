package practica9;

public class Platea extends Boleto {
    private int diasAnticipacion;

    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }

    @Override
    public double obtenerPrecio() {
        return diasAnticipacion >= 10 ? 50.0 : 60.0;
    }
}
