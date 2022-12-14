import java.util.Arrays;

/*
 2. Реализовать алгоритм пирамидальной сортировки (HeapSort)
 */

public class Task2 {

    public static void main(String args[]) {
        System.out.println(Arrays.toString(heapSort(new int[] { 4, 10, 8, 16, 15, 1, 6, 8 })));
    }

    public static int[] heapSort(int array[]) {
        int len = array.length;

        for (int i = len / 2 - 1; i >= 0; i--)
        toBinaryHeap(array, len, i);

        for (int i = len - 1; i >= 0; i--) {
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;

            toBinaryHeap(array, i, 0);
        }
        return array;
    }

    public static void toBinaryHeap(int array[], int len, int i) {
        int max = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < len && array[left] > array[max])
        max = left;

        if (right < len && array[right] > array[max])
        max = right;

        if (max != i) {
            int temp = array[i];
            array[i] = array[max];
            array[max] = temp;

            toBinaryHeap(array, len, max);
        }
    }
}
