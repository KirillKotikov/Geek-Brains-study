using System.Text.RegularExpressions;

namespace seventh_lesson
{
    class Task50
    {

        //Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
        // и возвращает значение этого элемента или же указание, что такого элемента нет.
        // Например, задан массив:
        // 1 4 7 2
        // 5 9 2 3
        // 8 4 2 4
        // 17 -> такого числа в массиве нет

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа на вход принимает позицию элемента в двумерном массиве, " +
                "и возвращает значение этого элемента или же указание, что такого элемента нет. :) ");
            int[,] array = GenerateNewTwoDimensionalArray();
            string index = ReadNumberFromConsole(array.GetLength(0), array.GetLength(1));
            PrintTwoDimensionalArray(array);
            SearchAndWriteNumberFromArray(index, array);

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
        public static string ReadNumberFromConsole(int index0, int index1)
        {
            while (true)
            {
                Console.WriteLine("В заданном массиве " + index0 + " строк(-и) " +
                "и " + index1 + " столбца(-ов).");
                Console.Write("Введите число от 1, где первая цифра будет номером строки, " +
                "а вторая номером столбца: ");
                string? inputNumber = Console.ReadLine();
                if (int.TryParse(inputNumber, out int number))
                {
                    return inputNumber;
                }
                Console.WriteLine("Вы ввели не число!");
            }
        }

        public static void SearchAndWriteNumberFromArray(string index, int[,] array)
        {
            int[] digits = index.Select(c => (int)char.GetNumericValue(c)).ToArray();

            try
            {
                Console.WriteLine(index + " -> " + array[(digits[0]) - 1, (digits[1]) - 1]);
            }
            catch (IndexOutOfRangeException)
            {
                Console.WriteLine(index + " -> такого числа в массиве нет (индекс " + index + " не существует)");
            }
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
    }
}