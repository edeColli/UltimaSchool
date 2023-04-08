public class App {
    public static void main(String[] args) throws Exception {
        Figura figura = new Retangulo("Preto", 5, 2);
        System.out.println("Área do Retângulo " + figura.calcularArea() );

        figura = new Quadrado("Rosa", 4);
        System.out.println("Área do Quadrado " + figura.calcularArea() );

        figura = new Triangulo("Verde", 4, 10);
        System.out.println("Área do Triângulo " + figura.calcularArea() );

        figura = new Circulo("Azul", 6);
        System.out.println("Área do Circulo " + figura.calcularArea() );
    }
}
