using System.Text.RegularExpressions;

namespace fourth_lesson
{
    class Task27
    {

        // Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
        // 452 -> 11
        // 82 -> 10
        // 9012 -> 12

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа принимает на вход число и выдаёт сумму цифр в числе. :)");
            Console.WriteLine("Сумма цифр у введённого числа = " + GetSumOfNumberFromArray(ConsoleReadNumber()));
        }
        public static int[] ConsoleReadNumber()
        {
            string? input;
            while (true)
            {
                Console.Write("Введите число от 0 до " + int.MaxValue + " включительно): ");
                input = Console.ReadLine();
                if (!int.TryParse(input, out int number)
                || Convert.ToInt32(input) < 0
                || Convert.ToInt32(input) > int.MaxValue)
                {
                    Console.WriteLine("Вы ввели текст или невалидное число!");
                } else break;
            }
            int[] numberArray = new int[input.Length];
            for (int i = 0; i < numberArray.Length; i++)
            {
                numberArray[i] = Convert.ToInt32(input[i].ToString());
            }
            return numberArray;


        }
        public static int GetSumOfNumberFromArray(int[] numbers)
        {
            int sum = 0;
            foreach (int number in numbers)
            {
                sum += number;
            }
            return sum;
        }
    }
}