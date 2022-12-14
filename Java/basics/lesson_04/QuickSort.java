package GB_java_lessons.lesson_04;

import java.util.Arrays;

public class QuickSort {

    public static void main(String[] args) {
        int[] numbers = { 5, 4, 3, 2, 1 };
        System.out.println(Arrays.toString(numbers));
        quickSort(numbers, 0, numbers.length - 1);
        System.out.println(Arrays.toString(numbers));
    }

    public static void quickSort(int[] numbers, int start, int end) {

        if (start >= end || numbers.length == 0)
            return;

        int midIndex = start + (end - start) / 2;
        int midElement = numbers[midIndex];

        int left = start;
        int right = end;
        while (left <= right) {

            while (numbers[left] < midElement) {
                left++;
            }
            while (numbers[right] > midElement) {
                right--;
            }

            if (numbers[left] >= numbers[right]) {
                int temp = numbers[left];
                numbers[left] = numbers[right];
                numbers[right] = temp;
                left++;
                right--;
            }
        }
        quickSort(numbers, start, midIndex - 1);
        quickSort(numbers, midIndex + 1, end);
    }
}