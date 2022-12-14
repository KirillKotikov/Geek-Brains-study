package ru.kotikov.lesson_5.repository;

public class AdditionCalculator implements Addition {

    @Override
    public int addition(int[] numbers) {
        return numbers[0] + numbers[1];
    }
}
