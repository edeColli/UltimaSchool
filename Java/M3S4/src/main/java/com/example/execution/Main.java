package com.example.execution;

import com.example.models.*;
import org.apache.commons.lang3.math.NumberUtils;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        Figura figura = new Retangulo("Amarelo", 4, 5);
        System.out.println("Área do Retangulo " + figura.calcularArea());

        figura = new Quadrado("Azul", 5);
        System.out.println("Área do Quadrado " + figura.calcularArea() );

        figura = new Triangulo("Verde", 3, 8);
        System.out.println("Área do Triângulo " + figura.calcularArea() );

        figura = new Circulo("Rosa",3);
        System.out.println("Área do Circulo " + figura.calcularArea() );
    }
}
