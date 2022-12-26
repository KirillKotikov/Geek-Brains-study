package ru.kotikov.task01;

import java.util.NoSuchElementException;
import java.util.Scanner;

/*
* Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
* и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
* вместо этого, необходимо повторно запросить у пользователя ввод данных.
*/
public class Task01 {
    public static void main(String[] args) {
        System.out.println("Вы ввели: " + readAndWriteFloat());
    }

    public static float readAndWriteFloat() {

        float parsed;
        String number = "Нет данных";
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                System.out.println("Введите дробное число (c точкой):");
                number = scanner.nextLine();
                parsed = Float.parseFloat(number);
                break;
            } catch (NumberFormatException | NoSuchElementException ex ) {
                System.out.println("Вы ввели не дробное число (c точкой)! Вы ввели: " + number);
            }
        }
        return parsed;
    }
}