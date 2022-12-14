using System.Text.RegularExpressions;

namespace fifth_lesson
{
    class Task34
    {

        // Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
        // Напишите программу, которая покажет количество чётных чисел в массиве.
        // [345, 897, 568, 234] -> 2

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа задаёт случайный массив случайного размера (от 2 до 10) элементов " +
            "(случайные положительными трёхзначные числа) и выводит на экран количество чётных чисел в массиве. ");
            int[] randomArray = GetRandomIntArray();
            PrintNumbersFromArray(randomArray);
            Console.WriteLine(" -> " + GetCountEvensNumbers(randomArray)); 
        }

        public static int[] GetRandomIntArray()
        {
            int[] array = new int[new Random().Next(2, 10)];
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = new Random().Next(100, 1000);
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

        public static int GetCountEvensNumbers(int[] array)
        {
            int count = 0;
            foreach (int i in array)
            {
                if (i % 2 == 0) 
                {
                    count++;
                }
            }
            return count;
        }

    }
}
