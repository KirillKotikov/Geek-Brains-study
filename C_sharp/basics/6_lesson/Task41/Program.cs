using System.Text.RegularExpressions;

namespace sixth_lesson
{
    class Task41
    {

        // Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
        // 0, 7, 8, -2, -2 -> 2
        // 1, -7, 567, 89, 223-> 3

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа позволяет пользователю ввести определенное количество цифр " +
            "от " + Int32.MinValue + " до " + Int32.MaxValue + " и выводит количество цифр больше нуля (0). :)");
            TakeArrayOfDigitsFromConsoleAndPrintCountOfNumbersGreaterThatZero();
        }

        public static void FillArrayFromConsole(int[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                while (true)
                {
                    Console.Write("Введите число №" + (i + 1) + " от " + Int32.MinValue + " до " + Int32.MaxValue + " - \n");
                    string? inputNumber = Console.ReadLine();
                    if (int.TryParse(inputNumber, out int num))
                    {
                        array[i] = Convert.ToInt32(inputNumber);
                        break;
                    }
                    Console.WriteLine("Вы ввели не число!");
                }
            }
        }

        public static void TakeArrayOfDigitsFromConsoleAndPrintCountOfNumbersGreaterThatZero()
        {
            while (true)
            {
                Console.Write("Введите количество цифр, которое вы хотите ввести: ");
                string? numberOfDigits = Console.ReadLine();
                if (int.TryParse(numberOfDigits, out int number))
                {
                    int[] numbersArray = new int[Convert.ToInt32(numberOfDigits)];
                    FillArrayFromConsole(numbersArray);
                    PrintNumbersFromArray(numbersArray);
                    PrintCountOfDigitsGreaterThanZeroInArray(numbersArray);
                    break;
                }
                Console.WriteLine("Вы ввели не число!");
            }
        }

        public static void PrintCountOfDigitsGreaterThanZeroInArray(int[] array)
        {
            int count = 0;
            foreach (int i in array)
            {
                if (i > 0)
                {
                    count++;
                }
            }
            Console.WriteLine(count);
        }

        public static void PrintNumbersFromArray(int[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                if (i != array.Length - 1)
                {
                    Console.Write(array[i] + ", ");
                }
                else
                {
                    Console.Write(array[i] + " -> ");
                }
            }
        }
    }
}
