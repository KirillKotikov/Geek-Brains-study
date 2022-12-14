package ru.kotikov.lesson_3;

import java.util.Comparator;

public class IntsComparatorByLastDigit implements Comparator<Integer> {

    @Override
    public int compare(Integer i1, Integer i2) {
        return i1%10 - i2%10;
    }
}
