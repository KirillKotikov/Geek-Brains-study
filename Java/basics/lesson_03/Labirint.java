package GB_java_lessons.lesson_03;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Labirint {

    public static final int[][] FIELD = {
            { +0, +0, +0, +0, +0, +0, +0, +0, +0, +0, -1 },
            { +0, -1, +0, +0, +0, +0, +0, +0, +0, +0, +0 },
            { +0, -1, +0, +0, +0, -1, +0, -1, -1, +0, 100 },
            { +0, +0, -1, -1, +0, -1, +0, +0, -1, +0, +0 },
            { +0, +0, -1, -1, -1, -1, -1, -1, -1, -1, +0 },
            { +1, +0, -1, +0, +0, -1, -1, -1, +0, +0, +0 },
            { +0, -1, -1, +0, +0, +0, +0, -1, +0, +0, +0 },
            { +0, -1, +0, +0, +0, +0, +0, +0, +0, -1, 100 },
            { +0, +0, +0, -1, -1, +0, +0, +0, +0, -1, -1 },
            { +0, -1, +0, -1, -1, +0, +0, +0, -1, -1, -1 },
            { +0, -1, +0, -1, -1, +0, +0, +0, -1, -1, -1 }
    };
    public static final int START_Y = 5;
    public static final int START_X = 0;
    public static final int[] FIRST_EXIT = { 2, 10 };
    public static final int[] SECOND_EXIT = { 7, 10 };

    public static void main(String[] args) {

        printField(FIELD);
        System.out.println();
        int[][] result = writeMoves(copyDuoArray(FIELD), START_Y, START_X);
        printField(result);
        System.out.println();
        int[] shortWay = getShorterExit(result, FIRST_EXIT, SECOND_EXIT);
        System.out.println("Меньшее количество ходов до выхода с" +
        " координатами = [" + shortWay[0] + "][" + shortWay[1] +
        "]. Количество шагов до этого выхода = " + getStepsFromExit(result,
        shortWay));

    }

    public static void printField(int[][] duoArray) {

        for (int i = 0; i < duoArray.length; i++) {
            for (int j = 0; j < duoArray.length; j++) {
                // System.out.print(FIELD[i][j] + " ");
                if (duoArray[i][j] == +0) {
                    System.out.print("░░░");
                } else if (duoArray[i][j] == -1) {
                    System.out.print("███");
                } else if (duoArray[i][j] == +1) {
                    System.out.print("╢┆╡");
                } else if (duoArray[i][j] == 100) {
                    System.out.print("║║║");
                } else {
                    if (duoArray[i][j] < 10) {
                        System.out.print(" " + duoArray[i][j] + " ");
                    } else {
                        System.out.print(" " + duoArray[i][j]);
                    }
                }
            }
            System.out.println("");
        }
    }

    public static int[][] writeMoves(int[][] duoArray, int y, int x) {

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { y, x });

        int[] point = new int[2];

        while (true) {
            point = queue.poll();

            if (point[0] != 0 && duoArray[point[0] - 1][point[1]] == 0) {
                int[] temp = new int[2];
                duoArray[point[0] - 1][point[1]] = duoArray[point[0]][point[1]] + 1;
                temp[0] = point[0] - 1;
                temp[1] = point[1];
                queue.add(temp);

            }
            if (point[1] != 10 && duoArray[point[0]][point[1] + 1] == 0) {
                int[] temp = new int[2];
                duoArray[point[0]][point[1] + 1] = duoArray[point[0]][point[1]] + 1;
                temp[0] = point[0];
                temp[1] = point[1] + 1;
                queue.add(temp);

            }
            if (point[0] != 10 && duoArray[point[0] + 1][point[1]] == 0) {
                int[] temp = new int[2];
                duoArray[point[0] + 1][point[1]] = duoArray[point[0]][point[1]] + 1;
                temp[0] = point[0] + 1;
                temp[1] = point[1];
                queue.add(temp);

            }
            if (point[1] != 0 && duoArray[point[0]][point[1] - 1] == 0) {
                int[] temp = new int[2];
                duoArray[point[0]][point[1] - 1] = duoArray[point[0]][point[1]] + 1;
                temp[0] = point[0];
                temp[1] = point[1] - 1;
                queue.add(temp);
            }
            if (queue.size() == 0)
                break;
        }
        return duoArray;
    }

    public static int[][] copyDuoArray(int[][] duoArray) {
        int[][] result = new int[duoArray.length][];
        for (int i = 0; i < result.length; i++) {
            result[i] = Arrays.copyOf(duoArray[i], duoArray[i].length);
        }

        return result;
    }

    public static int getStepsFromExit(int[][] duoArray, int[] point) {
        int steps = Integer.MAX_VALUE;
        if (point[0] != 0 && duoArray[point[0] - 1][point[1]] > 0
        && steps > duoArray[point[0] - 1][point[1]]) {
            steps = duoArray[point[0] - 1][point[1]];
        } else if (point[0] != 10 && duoArray[point[0] + 1][point[1]] > 0
        && steps > duoArray[point[0] + 1][point[1]]) {
            steps = duoArray[point[0] + 1][point[1]];
        }
        if (point[1] != 0 && duoArray[point[0]][point[1] - 1] > 0
        && steps > duoArray[point[0]][point[1] - 1]) {
            steps = duoArray[point[0]][point[1] - 1];
        }
        if (point[1] != 10 && duoArray[point[0]][point[1] + 1] > 0
        && steps > duoArray[point[0]][point[1] + 1]) {
            steps = duoArray[point[0]][point[1] + 1];
        }
        return steps + 1;
    }

    public static int[] getShorterExit(int[][] duoArray, int[]... exits) {

        int[] shorterExit = exits[0];
        for (int[] arr : exits) {
            if (getStepsFromExit(duoArray, shorterExit) > getStepsFromExit(duoArray, arr)) {
                shorterExit = arr;
            }
        }
        return shorterExit;
    }
}