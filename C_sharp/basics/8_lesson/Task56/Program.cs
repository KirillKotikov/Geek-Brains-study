using System.Text.RegularExpressions;

namespace eighth_lesson
{
    class Task56
    {

        // Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, 
        // которая будет находить строку с наименьшей суммой элементов.
        // Например, задан массив:
        // 1 4 7 2
        // 5 9 2 3
        // 8 4 2 4
        // 5 2 6 7 
        // Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка

        static void Main(string[] args)
        {
            int[,] array = GenerateNewTwoDimensionalArray();
            Console.WriteLine("Задан следующий массив: ");
            PrintTwoDimensionalArray(array);
            SearchAndWriteRowNumberOfArrayWithMinSum(array);
        }

        public static int[,] GenerateNewTwoDimensionalArray()
        {
            int[,] array = new int[4, 4];
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
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(array[i, j] + " ");
                }
                Console.WriteLine("");
            }
        }

        public static void SearchAndWriteRowNumberOfArrayWithMinSum(int[,] array)
        {
            int[] sums = new int[array.GetLength(0)];
            for (int i = 0; i < array.GetLength(0); i++)
            {
                int sum = 0;
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    sum += array[i, j];
                }
                sums[i] = sum;
            }
            int rowNumber = 0;
            int minSum = sums[0];
            for (int i = 1; i < sums.Length; i++)
            {
                if (minSum > sums[i])
                {
                    minSum = sums[i];
                    rowNumber = i;
                }
            }
            Console.WriteLine("Строка с наименьшей суммой элементов -> " + ++rowNumber);
        }
    }
}