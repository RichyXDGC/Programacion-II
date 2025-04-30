package practica9;

public class Palco extends Boleto {
    public Palco(int numero) {
        super(numero);
    }

    @Override
    public double obtenerPrecio() {
        return 100.0;
    }
}
