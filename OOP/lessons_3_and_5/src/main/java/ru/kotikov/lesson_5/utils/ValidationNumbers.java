package ru.kotikov.lesson_5.utils;

public class ValidationNumbers extends Validation{
    public int[] validTwoNumbers(String numbers) {
        String[] array = numbers.split(" ");
        if (array.length != 2) {
            return null;
        }
        int first;
        int second;
        try {
            first = Integer.parseInt(array[0]);
            second = Integer.parseInt(array[1]);
        } catch (Exception exception) {
            return null;
        }
        return new int[]{first, second};
    }
}
