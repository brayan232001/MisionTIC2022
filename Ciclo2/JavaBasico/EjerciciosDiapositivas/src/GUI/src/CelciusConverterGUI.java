import javax.swing.*;
import java.awt.*;

public class CelciusConverterGUI extends JFrame{
    private JPanel mainPanel;
    private JTextField celciusTextFIeld;
    private JLabel celciusLabel;
    private JButton converterButton;
    private JLabel farhenheitLabel;

    public CelciusConverterGUI(String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();
    }

    public static void main(String[] args) {
        JFrame frame = new CelciusConverterGUI("Celcius Converter");
        frame.setVisible(true);
    }
}
