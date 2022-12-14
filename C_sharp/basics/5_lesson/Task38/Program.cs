using System.Text.RegularExpressions;

namespace fifth_lesson
{
    class Task38
    {

        // Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
        // [3 7 22 2 78] -> 76

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задает одномерный массив (размером от 2 до 20), заполненный " + 
            "случайными числами (от 1 до 100) и находит разницу между максимальным и минимальным элементов массива. :)");
            int[] randomArray = GetRandomIntArray();
            PrintNumbersFromArray(randomArray);
            Console.WriteLine(" -> " + GetMinAndMaxNumberDifference(randomArray)); 
        }

        public static int[] GetRandomIntArray()
        {
            int[] array = new int[new Random().Next(2, 20)];
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = new Random().Next(1, 100);
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

        public static int GetMinAndMaxNumberDifference(int[] array)
        {
            int max = Int32.MinValue;
            int min = Int32.MaxValue;
            foreach (int i in array) 
            {
                if (min > i) 
                {
                    min = i;
                }
                if (max < i) {
                    max = i;
                }
            }
            return max - min;
        }
    }
}
