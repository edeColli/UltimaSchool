package com.example.models;

public class Quadrado extends Retangulo {
    
  public Quadrado(String cor, double lado1) {
    super(cor, lado1);    
  }

  @Override
  public double calcularArea() {
    return Math.pow(super.getLado1(),2);
  }

  @Override
  
  public String toString(){
    return  "Quadrado {" +
      "lado= " + super.getLado1() +
      ", cor=" + super.getCor() + 
      "}";
  }

}
