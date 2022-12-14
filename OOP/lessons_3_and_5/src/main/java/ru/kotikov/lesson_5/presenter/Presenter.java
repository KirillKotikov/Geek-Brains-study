package ru.kotikov.lesson_5.presenter;

import ru.kotikov.lesson_5.enums.Function;
import ru.kotikov.lesson_5.repository.Addition;
import ru.kotikov.lesson_5.repository.AdditionCalculator;
import ru.kotikov.lesson_5.utils.ValidationNumbers;

public class Presenter {

    private static final String ERROR_DATA = "Ошибка! Вы ввели некорректные данные! Запустите программу заново и попробуйте снова.";
    private static final String ERROR = "Ошибка!";
    private final Addition addition;
    private final ValidationNumbers validation;

    public Presenter() {
        this.validation = new ValidationNumbers();
        this.addition = new AdditionCalculator();
    }


    public String calculate(String inputString, Function function) {

        if (!validation.checkString(inputString)) return ERROR_DATA;

        int[] numbers = validation.validTwoNumbers(inputString);
        if (numbers == null) return ERROR_DATA;

        switch (function) {
            case Addition: {
                return String.valueOf(addition.addition(numbers));
            }
            default:
                return ERROR;
        }
    }
}
