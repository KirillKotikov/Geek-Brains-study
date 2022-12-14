using System.Text.RegularExpressions;

namespace eighth_lesson
{
    class Task58
    {

        // Задача 58: Задайте две матрицы. Напишите программу, которая выведет матрицу произведения 
        // элементов двух предыдущих матриц.
        // Например, заданы 2 массива:
        // 1 4 7 2 
        // 5 9 2 3
        // 8 4 2 4
        // 5 2 6 7
        // и
        // 1 5 8 5
        // 4 9 4 2
        // 7 2 2 6 
        // 2 3 4 7
        // Их произведение будет равно следующему массиву:
        // 1 20 56 10
        // 20 81 8 6
        // 56 8 4 24
        // 10 6 24 49

        static void Main(string[] args)
        {
            int[,] array1 = GenerateNewTwoDimensionalArray();
            int[,] array2 = GenerateMatrixOfTwoDimensionalArray(array1);
            Console.WriteLine("Первый массив: ");
            PrintTwoDimensionalArray(array1);
            Console.WriteLine("Второй массив: ");
            PrintTwoDimensionalArray(array2);
            Console.WriteLine("Их произведение будет равно следующему массиву: ");
            int[,] multiplyArray = getMultiplyOfTwoDimensionalArray(array1, array2);
            PrintTwoDimensionalArray(multiplyArray);
        }

        public static int[,] GenerateMatrixOfTwoDimensionalArray(int[,] array) {
            int[,] resultArray = new int[array.GetLength(0), array.GetLength(1)];

            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    resultArray[i, j] = array[j, i];
                }
            }
            return resultArray;
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
        public static int[,] getMultiplyOfTwoDimensionalArray(int[,] array1, int[,] array2)
        {
            int[,] resultArray = new int[array1.GetLength(0), array1.GetLength(1)];
            for (int i = 0; i < array1.GetLength(0); i++)
            {
                for (int j = 0; j < array1.GetLength(1); j++)
                {
                    resultArray[i, j] = array1[i, j] * array2[i, j];
                }
            }
            return resultArray;
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