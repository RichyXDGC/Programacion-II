package practica9;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TeatroMunicipalGUI extends JFrame {
    private JRadioButton palcoBtn, plateaBtn, galeriaBtn;
    private JTextField numeroField, diasField;
    private JButton venderBtn, salirBtn;
    private JLabel resultadoLabel;

    public TeatroMunicipalGUI() {
        setTitle("Teatro Municipal");
        setSize(500, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new BorderLayout());
        JLabel titulo = new JLabel("Teatro Municipal", SwingConstants.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 26));
        titulo.setForeground(Color.BLUE);
        topPanel.add(titulo, BorderLayout.CENTER);

        ImageIcon icon = new ImageIcon("2025-04-29_235313.jpg"); 
        Image img = icon.getImage().getScaledInstance(100, 60, Image.SCALE_SMOOTH);
        JLabel imageLabel = new JLabel(new ImageIcon(img));
        topPanel.add(imageLabel, BorderLayout.EAST);

        add(topPanel, BorderLayout.NORTH);

        JPanel centerPanel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL;

       
        palcoBtn = new JRadioButton("Palco");
        plateaBtn = new JRadioButton("Platea");
        galeriaBtn = new JRadioButton("Galería");
        ButtonGroup grupo = new ButtonGroup();
        grupo.add(palcoBtn);
        grupo.add(plateaBtn);
        grupo.add(galeriaBtn);

        JPanel tipoPanel = new JPanel();
        tipoPanel.add(palcoBtn);
        tipoPanel.add(plateaBtn);
        tipoPanel.add(galeriaBtn);

        gbc.gridx = 0; gbc.gridy = 0; gbc.gridwidth = 2;
        centerPanel.add(new JLabel("Datos del Boleto"), gbc);

        gbc.gridy++;
        centerPanel.add(tipoPanel, gbc);

        gbc.gridwidth = 1; gbc.gridy++;
        centerPanel.add(new JLabel("Número:"), gbc);
        gbc.gridx = 1;
        numeroField = new JTextField("1", 10);
        centerPanel.add(numeroField, gbc);

        gbc.gridx = 0; gbc.gridy++;
        centerPanel.add(new JLabel("Cant. Días para el Evento:"), gbc);
        gbc.gridx = 1;
        diasField = new JTextField(10);
        centerPanel.add(diasField, gbc);

        gbc.gridx = 0; gbc.gridy++;
        venderBtn = new JButton("Vende");
        salirBtn = new JButton("Salir");
        centerPanel.add(venderBtn, gbc);
        gbc.gridx = 1;
        centerPanel.add(salirBtn, gbc);

        add(centerPanel, BorderLayout.CENTER);

        
        JPanel bottomPanel = new JPanel();
        resultadoLabel = new JLabel("Número: 1, Precio: 100.0");
        resultadoLabel.setFont(new Font("Arial", Font.BOLD, 14));
        resultadoLabel.setForeground(Color.BLUE);
        bottomPanel.add(resultadoLabel);
        add(bottomPanel, BorderLayout.SOUTH);

        
        venderBtn.addActionListener(e -> venderBoleto());
        salirBtn.addActionListener(e -> System.exit(0));

        setVisible(true);
    }

    private void venderBoleto() {
        try {
            int numero = Integer.parseInt(numeroField.getText());
            int dias = diasField.getText().isEmpty() ? 0 : Integer.parseInt(diasField.getText());
            Boleto boleto;

            if (palcoBtn.isSelected()) {
                boleto = new Palco(numero);
            } else if (plateaBtn.isSelected()) {
                boleto = new Platea(numero, dias);
            } else if (galeriaBtn.isSelected()) {
                boleto = new Galeria(numero, dias);
            } else {
                resultadoLabel.setText("Seleccione un tipo de boleto.");
                return;
            }

            resultadoLabel.setText(boleto.toString());
        } catch (NumberFormatException ex) {
            resultadoLabel.setText("Ingrese datos válidos.");
        }
    }

    abstract class Boleto {
        protected int numero;
        public Boleto(int numero) {
            this.numero = numero;
        }
        public abstract double obtenerPrecio();
        public String toString() {
            return "Número: " + numero + ", Precio: " + obtenerPrecio();
        }
    }

    class Palco extends Boleto {
        public Palco(int numero) {
            super(numero);
        }
        public double obtenerPrecio() {
            return 100.0;
        }
    }

    class Platea extends Boleto {
        private int diasAnticipacion;
        public Platea(int numero, int dias) {
            super(numero);
            this.diasAnticipacion = dias;
        }
        public double obtenerPrecio() {
            return diasAnticipacion >= 10 ? 50.0 : 60.0;
        }
    }

    class Galeria extends Boleto {
        private int diasAnticipacion;
        public Galeria(int numero, int dias) {
            super(numero);
            this.diasAnticipacion = dias;
        }
        public double obtenerPrecio() {
            return diasAnticipacion >= 10 ? 25.0 : 30.0;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TeatroMunicipalGUI());
    }
}
