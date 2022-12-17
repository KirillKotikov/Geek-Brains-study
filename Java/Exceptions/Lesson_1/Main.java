package Exceptions.Lesson_1;

import java.io.File;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        // main.third(null);
        main.arraysFirst(new int[]{1,2}, new int[]{1,5,4});
    }

    // Все исключения в методах непроверяемые.

    // Выбросит ArrayOutOfBoundException
    public void first(int[] first) {
        first[first.length + 1] = 3;
    }

    // Выбросит ArithmeticException
    public void second(int second) {
        second = second / 0;
    }

    // Если ввести null как параметр, выбросит NullPointerException
    public void third(String filePath) {
        File file = new File(filePath);
        file.getName();
    }

    public int[] arraysFirst(int[] first, int[] second) {
        if (first.length != second.length) {
            throw new RuntimeException("У массивов должны быть одинаковые размеры!");
        } else {
            int [] result = new int[first.length];
            for (int i = 0; i < result.length; i++) {
                result[i] = first[i] - second[i];
            }
            return result;
        }
    }

    public int[] arraysSecond(int[] first, int[] second) {
        if (first.length != second.length) {
            throw new RuntimeException("У массивов должны быть одинаковые размеры!");
        } else {
            int [] result = new int[first.length];
            for (int i = 0; i < result.length; i++) {
                result[i] = first[i] / second[i];
            }
            return result;
        }
    }

}