package ru.kotikov.lesson_5.utils;

public class Validation {

    public boolean checkString(String str) {
        return !(str == null || str.isBlank());
    }
}
