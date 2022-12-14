package ru.kotikov.lesson_5;

import ru.kotikov.lesson_5.view.ConsoleView;
import ru.kotikov.lesson_5.view.DesktopView;
import ru.kotikov.lesson_5.view.View;

import java.util.Scanner;

public class Main {
    private final View view;

    public Main(View view) {
        this.view = view;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Выберите тип калькулятора! Наберите 1 для консольного и 2 для десктопного.");
        String str = scanner.next();
        Main main;
        if (str.equals("1")) main = new Main(new ConsoleView());
        else if (str.equals("2")) main = new Main(new DesktopView());
        else {
            System.out.println("Вы ввели неправильный код, прощайте! :)");
            return;
        }
        main.start();
    }

    private void start() {
        this.view.start();
    }
}
