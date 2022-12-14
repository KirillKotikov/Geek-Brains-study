
namespace ninth_lesson
{
    class Task66
    {

        // Задача 66: Задайте значения M и N. Напишите программу, 
        // которая найдёт сумму натуральных элементов в промежутке от M до N.
        // M = 1; N = 15 -> 120
        // M = 4; N = 8. -> 30

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа выводит на экран сумму натуральных элементов " +
             "в промежутке от M до N (включительно) =)");
            int M = ReadNumberFromConsole("M");
            int N = ReadNumberFromConsole("N");
            GetSumOfNumbersFromRange(M, N, "M", "N");

        }

        public static void GetSumOfNumbersFromRange(int start, int end, string startName, string endName)
        {
            Console.Write(startName + " = " + start + "; " + endName + " = " + end + " -> ");
            int sum = 0;
            for (int i = start; i <= end; i++)
            {
                sum += i;
            }
            Console.WriteLine(sum);
        }

        public static int ReadNumberFromConsole(string numberName)
        {
            while (true)
            {
                Console.Write("Введите значение " + numberName + " (от 1 до " + int.MaxValue/100000 + "): ");
                string? inputNumber = Console.ReadLine();
                if (int.TryParse(inputNumber, out int number) && number > 0 && number < int.MaxValue/100000)
                {
                    return number;
                }
                Console.WriteLine("Вы ввели не натуральное или слишком большое число! А может и вообще текст :D");
            }
        }
    }
}