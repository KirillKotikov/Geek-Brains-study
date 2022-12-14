using System.Text.RegularExpressions;

namespace seventh_lesson
{
    class Task47
    {

        //Задача №47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
        // m = 3, n = 4.
        // 0,5 7 -2 -0,2
        // 1 -3,3 8 -9,9
        // 8 7,8 -7,1 9

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задаёт двумерный массив размером m*n (которые вводит пользователь), " +
            "заполненный случайными вещественными числами (от -99.99 до 100) и выводит его содержимое. :) ");
            int m = ReadNumberFromConsole("m");
            int n = ReadNumberFromConsole("n");
            double[,] array = GenerateNewTwoDimensionalArray(m, n);
            WriteSizeAndContentFromTwoDimensionalArray(m, n, array);
        }

        public static double[,] GenerateNewTwoDimensionalArray(int m, int n)
        {
            double[,] array = new double[m, n];
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    array[i, j] = new Random().NextDouble() * new Random().Next(-99, 100);
                }
            }
            return array;
        }
        public static int ReadNumberFromConsole(string numberName)
        {
            while (true)
            {
                Console.WriteLine("Введите натуральное число " + numberName + ": ");
                string? inputNumber = Console.ReadLine();
                if (int.TryParse(inputNumber, out int number) && !(Convert.ToInt32(number) < 1))
                {
                    return Convert.ToInt32(number);
                }
                Console.WriteLine("Вы ввели не число или не натуральное число!");
            }
        }

        public static void WriteSizeAndContentFromTwoDimensionalArray(int m, int n, double[,] array)
        {
            Console.WriteLine("m = " + m + ", n = " + n + ".");
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(Math.Round(array[i, j], 2) + " ");
                }
                Console.WriteLine("");
            }
        }
    }
}
