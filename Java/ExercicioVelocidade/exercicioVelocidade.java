import java.util.Scanner;

import javax.print.event.PrintJobListener;

import java.util.*;

public class exercicioVelocidade {

  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int velocidadeVeiculo;
    int velocidadeMaxima;

    System.out.print("Informe a velocidade do veículo: ");
    velocidadeVeiculo = validarValorInteiro(sc);
    System.out.print("Informe a velocidade máxima: ");
    velocidadeMaxima = validarValorInteiro(sc);

    if (velocidadeVeiculo != 0 & velocidadeMaxima != 0) {
      velocidadeMaxima = velocidadeMaxima + (velocidadeMaxima / 10);
      if (velocidadeVeiculo > velocidadeMaxima) {
        System.out.println("Multado!");
      } else {
        System.out.println("OK!");
      }
    } else {
      System.out.println("Não foi possível aferir a velocidade");
    }
    sc.close();
  }

  private static int validarValorInteiro(Scanner sc) {
    int valorInteiro = 0;

    if (sc.hasNextInt()) {
      valorInteiro = sc.nextInt();
    }

    if (valorInteiro == 0) {
      System.out.println("Velocidade informada é inválida!");
    }
    return valorInteiro;
  }
}