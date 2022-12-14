package ru.kotikov.lesson_3;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 1:
        Integer[] ints = new Integer[]{125, 369, 111, 247, 584};
        System.out.println("Arrays.toString(ints) = " + Arrays.toString(ints));
        sort(ints);
        System.out.println("Arrays.toString(ints) = " + Arrays.toString(ints));

        // 2:
        StringList strings = new StringList();
        strings.add("Привет");
        strings.add("Список");
        strings.add("Строк");

        for (String string : strings) {
            System.out.println("string = " + string);
        }

    }

    /*
     * Создать метод, который принимает массив int и сортирует его по последней цифре.
     * Используйте метод Arrays.sort. для его работы создайте свой компаратор.
     * Имеется в виду последняя цифра в записи числа, например в числе 123, последння цифра 3.
     * Надо сделать сортировку, которая учитывает только эту последнюю цифру в числе.
     */
    public static void sort(Integer[] ints) {
        Arrays.sort(ints, new IntsComparatorByLastDigit());
    }

}