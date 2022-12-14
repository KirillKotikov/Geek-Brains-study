package GB_java_lessons.lesson_02;

/*
 * Написать программу, показывающую последовательность действий для игры “Ханойская башня”
 */

public class Task1 {

    public static void main(String[] args) {
        printSubsequenceForHanoyTowerGame(6);
    }

    static void printSubsequenceForHanoyTowerGame(int numberOfRings) {
        if(numberOfRings == 1) {
            System.out.println(numberOfRings + " from first to third");
            return;
        }
        printSubsequenceForHanoyTowerGame(numberOfRings - 1);
        System.out.println(numberOfRings + " from first to third");
        printSubsequenceForHanoyTowerGame(numberOfRings - 1);
    }
}
