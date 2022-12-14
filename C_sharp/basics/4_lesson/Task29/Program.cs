using System.Text.RegularExpressions;

namespace fourth_lesson
{
    class Task29
    {

        // Задача 29: Напишите программу, которая задаёт случайный массив случайного размера (от 5 до 10) элементов 
        // (значение элементов от 1 до 40) и выводит на экран массив квадратов этих чисел.
        // 1, 2, 5, 7, 19 -> [2, 4, 25, 49, 361]
        // 6, 1, 33 -> [36, 1, 1089]

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задаёт случайный массив случайного размера (от 5 до 10) элементов " +
            "(значение элементов от 1 до 40) и выводит на экран массив квадратов этих чисел.");
            int[] randomArray = getRandomIntArray();
            printNumbersFromArray(randomArray);
            printCubesFromArrayNumbers(getCubesOfArrayNumbers(randomArray));
        }

        public static int[] getRandomIntArray()
        {
            int[] array = new int[new Random().Next(5, 10)];
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = new Random().Next(1, 40);
            }
            return array;
        }

        public static void printNumbersFromArray(int[] randomArray)
        {
            for (int i = 0; i < randomArray.Length; i++)
            {
                if (i == randomArray.Length - 1)
                {
                    Console.Write(randomArray[i] + " -> ");
                }
                else
                {
                    Console.Write(randomArray[i] + ", ");
                }
            }
        }
        public static double[] getCubesOfArrayNumbers(int[] array)
        {
            double[] result = new double[array.Length];
            for (int i = 0; i < array.Length; i++)
            {
                result[i] = Math.Pow(array[i], 3);
            }
            return result;
        }

        public static void printCubesFromArrayNumbers(double[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                if (i == 0)
                {
                    Console.Write("[" + numbers[i] + ", ");
                }
                else if (i == numbers.Length - 1)
                {
                    Console.WriteLine(numbers[i] + "]");
                }
                else
                {
                    Console.Write(numbers[i] + ", ");
                }
            }
        }
    }
}
