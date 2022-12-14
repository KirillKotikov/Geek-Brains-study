using System.Text.RegularExpressions;

namespace sixth_lesson
{
    class Task43
    {

        // Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, 
        // заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
        // b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа находит точку пересечения двух прямых, " +
                "заданных уравнениями y = k1 * x + b1, y = k2 * x + b2. Значения b1, k1, b2 и k2 задаются пользователем. :) ");
            double b1 = ReadNumberFromConsole("b1");
            double k1 = ReadNumberFromConsole("k1");
            double b2 = ReadNumberFromConsole("b2");
            double k2 = ReadNumberFromConsole("k2");
            WriteInputNumbers(b1, k1, b2, k2);
            WriteResultOfEquation(b1, k1, b2, k2);
        }

        public static double ReadNumberFromConsole(string numberName)
        {
            while (true)
            {
                Console.Write("Введите значение " + numberName + ": ");
                string? inputNumber = Console.ReadLine();
                if (double.TryParse(inputNumber, out double number))
                {
                    return number;
                }
                Console.WriteLine("Вы ввели не число или слишком большое/маленькое число!");
            }
        }

        public static void WriteInputNumbers(double b1, double k1, double b2, double k2)
        {
            Console.Write("b1 = " + b1 + ", k1 = " + k1 + ", b2 = " + b2 + ", k2 = " + k2);
        }
        public static void WriteResultOfEquation(double b1, double k1, double b2, double k2)
        {
            double x = (b2 - b1) / (k1 - k2);
            double y = k1 * x + b1;
            if (!Double.IsNaN(y))
            {
                Console.WriteLine(" -> (" + y + "; " + y + ")");
            }
            else
            {
                Console.WriteLine(" -> Точки пересечения нет!");
            }
        }
    }
}
