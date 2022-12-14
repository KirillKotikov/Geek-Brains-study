package ru.kotikov.lesson_5.view;

import ru.kotikov.lesson_5.enums.Function;
import ru.kotikov.lesson_5.presenter.Presenter;

import java.util.Scanner;

public class ConsoleView implements View{

    private final Presenter presenter;
    private final Scanner scanner;

    public ConsoleView() {
        this.presenter = new Presenter();
        this.scanner = new Scanner(System.in);
    }

    @Override
    public void start() {
        System.out.println("Это простой калькулятор, который складывает 2 целых числа.\nВведите 2 числа через пробел:");
        System.out.println("Решение: " + presenter.calculate(scanner.nextLine(), Function.Addition));
    }
}
