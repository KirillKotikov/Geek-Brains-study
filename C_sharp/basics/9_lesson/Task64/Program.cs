
namespace ninth_lesson
{
    class Task64
    {

        // Задача 64: Задайте значения M и N. 
        // Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
        // M = 1; N = 5. -> ""1, 2, 3, 4, 5""
        // M = 4; N = 8. -> ""4, 6, 7, 8""

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа выводит на экран все натуральные числа в промежутке от M до N (включительно) =)");
            int M = ReadNumberFromConsole("M");
            int N = ReadNumberFromConsole("N");
            GetNumbersFromRange(M, N, "M", "N");

        }

        public static void GetNumbersFromRange(int start, int end, string startName, string endName)
        {
            Console.Write(startName + " = " + start + "; " + endName + " = " + end + ". -> \"\"");
            for (int i = start; i <= end; i++)
            {
                if (i == end)
                {
                    Console.WriteLine(i + "\"\"");
                }
                else
                {
                    Console.Write(i + ", ");
                }
            }
        }

        public static int ReadNumberFromConsole(string numberName)
        {
            while (true)
            {
                Console.Write("Введите значение " + numberName + " (от 1 до " + int.MaxValue + "): ");
                string? inputNumber = Console.ReadLine();
                if (int.TryParse(inputNumber, out int number) && number > 0)
                {
                    return number;
                }
                Console.WriteLine("Вы ввели не натуральное или слишком большое число! А может и вообще текст :D");
            }
        }
    }
}