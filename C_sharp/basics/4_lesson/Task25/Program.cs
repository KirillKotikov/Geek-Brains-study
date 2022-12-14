using System.Text.RegularExpressions;

namespace fourth_lesson
{
    class Task25
    {

        // Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
        // 3, 5 -> 243 (3⁵)
        // 2, 4 -> 16

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа принимает на вход два числа (A и B) " +
            "и возводит число A в натуральную степень B. :)");
            int A = ConsoleReadNumber("A");
            int B = ConsoleReadNumber("B");
            PrintPowResult(A, B);
        }

        public static int ConsoleReadNumber(string numberName)
        {
            string? input;
            int inputNumber = 0;
            while (true)
            {
                Console.Write("Введите число " + numberName + " (от 1 до 35 включительно): ");
                input = Console.ReadLine();
                if (!int.TryParse(input, out int number)
                || Convert.ToInt32(input) < 1
                || Convert.ToInt32(input) > 35)
                {
                    Console.WriteLine("Вы ввели текст или невалидное число!");
                }
                else
                {
                    inputNumber = Convert.ToInt32(input);
                    break;
                }
            }
            return inputNumber;
        }

        public static void PrintPowResult(int numberA, int numberB)
        {
            int result = numberA;
            for (int i = 1; i < numberB; i++)
            {
                result *= numberA;
            }
            Console.WriteLine("Число " + numberA + " в степени " + numberB + " = " + result);
        }
    }
}