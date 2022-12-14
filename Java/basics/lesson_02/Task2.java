package GB_java_lessons.lesson_02;

import java.util.Arrays;

// Реализовать алгоритм сортировки вставками
public class Task2 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(insertionSort(new int[] { 5, 4, 8, 1, 12, 10, 2 })));
    }

    public static int[] insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int j = i - 1;
            int key = array[i];
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j -= 1;

            }
            array[j + 1] = key;
        }
        return array;
    }
}
