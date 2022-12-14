using System.Text.RegularExpressions;

namespace fifth_lesson
{
    class Task36
    {

        // Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, 
        // стоящих на нечётных позициях.
        // [3, 7, 23, 12] -> 19
        // [-4, -6, 89, 6] -> 0

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задает одномерный массив (размером от 4 до 20), заполненный " + 
            "случайными числами (от 10 до 100) и находит сумму элементов, стоящих на нечётных позициях. :)");
            int[] randomArray = GetRandomIntArray();
            PrintNumbersFromArray(randomArray);
            Console.WriteLine(" -> " + GetSumOfOddIndexesNumbers(randomArray)); 
        }

        public static int[] GetRandomIntArray()
        {
            int[] array = new int[new Random().Next(4, 20)];
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = new Random().Next(10, 100);
            }
            return array;
        }

        public static void PrintNumbersFromArray(int[] randomArray)
        {
            for (int i = 0; i < randomArray.Length; i++)
            {
                if (i == 0)
                {
                    Console.Write("[" + randomArray[i] + ", ");
                }
                else if (i == randomArray.Length - 1)
                {
                    Console.Write(randomArray[i] + "]");
                }
                else
                {
                    Console.Write(randomArray[i] + ", ");
                }
            }
        }

        public static int GetSumOfOddIndexesNumbers(int[] array)
        {
            int sum = array[1];
            for (int i = 3; i < array.Length; i += 2) 
            {
                sum += array[i];
            }
            return sum;
        }
    }
}
