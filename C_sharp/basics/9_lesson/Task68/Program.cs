
namespace ninth_lesson
{
    class Task68
    {

        // Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. 
        // Даны два неотрицательных числа m и n.
        // m = 3, n = 2 -> A(m,n) = 29

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа вычисляет функцию Аккермана с помощью рекурсии =)");
            int m = ReadNumberFromConsole("m");
            int n = ReadNumberFromConsole("n");
            GetStartTextForAkkermansFunction(m, n, "m", "n");
            Console.WriteLine("A(m,n) = " + GetAkkermansFunction(m, n));

        }

        public static int GetAkkermansFunction(int m, int n)
        {
            if (m == 0) return n + 1;
            else if ((m != 0) && (n == 0)) return GetAkkermansFunction(m - 1, 1);
            else return GetAkkermansFunction(m - 1, GetAkkermansFunction(m, n - 1));
        }

        public static void GetStartTextForAkkermansFunction(int start, int end, string startName, string endName)
        {
            Console.Write(startName + " = " + start + "; " + endName + " = " + end + " -> ");
        }

        public static int ReadNumberFromConsole(string numberName)
        {
            while (true)
            {
                Console.Write("Введите значение " + numberName + " (от 1 до " + 4 + "): ");
                string? inputNumber = Console.ReadLine();
                if (int.TryParse(inputNumber, out int number) && number > 0 && number < 4)
                {
                    return number;
                }
                Console.WriteLine("Вы ввели не натуральное или слишком большое число! А может и вообще текст :D");
            }
        }
    }
}