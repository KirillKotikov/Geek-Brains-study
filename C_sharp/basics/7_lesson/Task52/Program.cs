using System.Text.RegularExpressions;

namespace seventh_lesson
{
    class Task52
    {

        //Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
        // Например, задан массив:
        // 1 4 7 2
        // 5 9 2 3
        // 8 4 2 4
        // Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задаёт двумерный массив из целых чисел и " +
            "находит среднее арифметическое элементов в каждом столбце. :) ");
            int[,] array = GenerateNewTwoDimensionalArray();
            PrintTwoDimensionalArray(array);
            PrintAverageOfColumnsFromArray(array);
            List<GenerateNewTwoDimensionalArray()> List = new List<>();


        }

        public static int[,] GenerateNewTwoDimensionalArray()
        {
            int[,] array = new int[new Random().Next(2, 10), new Random().Next(2, 10)];
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    array[i, j] = new Random().Next(1, 10);
                }
            }
            return array;
        }

        public static void PrintTwoDimensionalArray(int[,] array)
        {
            Console.WriteLine("Задан следующий массив: ");
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(array[i, j] + " ");
                }
                Console.WriteLine("");
            }
        }
        public static void PrintAverageOfColumnsFromArray(int[,] array)
        {
            Console.Write("Среднее арифметическое каждого столбца: ");
            for (int i = 0; i < array.GetLength(1); i++)
            {
                double sum = 0;
                for (int j = 0; j < array.GetLength(0); j++)
                {
                    sum += array[j, i];
                }
                if (i != array.GetLength(1) - 1)
                {
                    Console.Write(Math.Round(sum / (double)array.GetLength(0), 1) + "; ");
                }
                else
                {
                    Console.WriteLine(Math.Round(sum / (double)array.GetLength(0), 1) + ".");
                }

            }
        }
    }
}