public class Circulo extends Figura{

  private double raio;
  private static final double PI = 3.14;

  public Circulo(String cor, double raio){
    super(cor);
    this.raio = raio;
  }
  @Override
  public double calcularArea() {
    return PI * Math.pow(raio,2);
  }

  @Override
  public String toString(){
    return "Circulo de cor " + super.getCor() + " e de raio " + raio + ".";
  }
  
}
