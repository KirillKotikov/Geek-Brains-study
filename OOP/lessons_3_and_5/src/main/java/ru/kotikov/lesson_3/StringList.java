package ru.kotikov.lesson_3;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
/*
* Создайте класс, который представляет из себя коллекцию, добавьте 2 метода add и get для работы с коллекцией.
* Реализуйте возможность использования цикла for-each для работы с данной коллекцией.
* Для этого реализуйте интерфейс Iterable и создайте итератор*/
public class StringList implements Iterable<String> {
    private final List<String> strings;

    public StringList() {
        this.strings = new ArrayList<>();
    }

    public void add(String str) {
        this.strings.add(str);
    }

    public String get(int index) {
        return this.strings.get(index);
    }


    @Override
    public Iterator<String> iterator() {
        return new StringListIterator();
    }

    class StringListIterator implements Iterator<String> {

        int index = 0;

        @Override
        public boolean hasNext() {
          return index < strings.size();
        }

        @Override
        public String next() {
            return strings.get(index++);
        }
    }
}
