using System.Text.RegularExpressions;

namespace eighth_lesson
{
    class Task54
    {

        //Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по возрастанию 
        // элементы каждой строки двумерного массива.
        // Например, задан массив:
        // 1 4 7 2
        // 5 9 2 3
        // 8 4 2 4
        // В итоге получается вот такой массив:
        // 1 2 4 7
        // 2 3 5 9
        // 2 4 4 8

        static void Main(string[] args)
        {
            int[,] array = GenerateNewTwoDimensionalArray();
            Console.WriteLine("Задан следующий массив: ");
            PrintTwoDimensionalArray(array);
            // SortRowsInArray(array);
            // Console.WriteLine("Осортировали строки: ");
            // PrintTwoDimensionalArray(array);
            Console.WriteLine("array[0, 3] = " + array[0, 3]);
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
        public static void SortRowsInArray(int[,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    for (int k = j; k < array.GetLength(1); k++)
                    {
                        int min = array[i, j];
                        if (min > array[i, k]) {
                            min = array[i, k];
                            array[i, k] = array[i, j];
                            array[i, j] = min;
                        }
                    }
                }
            }
        }
    }
}