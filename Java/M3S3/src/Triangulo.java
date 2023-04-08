public class Triangulo extends Figura{

  private double base;
  private double altura;
  public double getBase() {
    return base;
  }

  public Triangulo(String cor, double lado, double altura){
    super(cor);
    this.base = base;
    this.altura = altura;
  }

  public double getAltura() {
    return altura;
  }

  public void setBase(double base) {
    this.base = base;
  }

  public void setAltura(double altura) {
    this.altura = altura;
  }
  
  @Override
  public double calcularArea() {
    return (this.base * this.altura) / 2;
  }
  
  @Override
  public String toString(){
    return "Triangulo {" +
      "base= " + base +
      ", altura= " + altura +
      ", cor=" + super.getCor() + 
    "}";
  }
}
