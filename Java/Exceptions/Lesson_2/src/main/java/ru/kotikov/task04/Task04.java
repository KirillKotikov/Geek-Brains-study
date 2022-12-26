package ru.kotikov.task04;

import java.util.Scanner;

/*
Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
 */
public class Task04 {
    public static void main(String[] args) throws BlankStringException {
        System.out.println("Вы ввели: " + getStringFromConsole());
    }

    public static String getStringFromConsole() throws BlankStringException {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Введите любую строку:");
            String nextLine = scanner.nextLine();
            if (nextLine.isBlank()) {
                System.out.println("Пустые строки вводить нельзя!");
                throw new BlankStringException("Input string must not be blank!");
            }
        return nextLine;
        }
    }
}
