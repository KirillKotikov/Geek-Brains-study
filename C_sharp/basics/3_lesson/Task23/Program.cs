namespace third_lesson
{
    class Task23
    {

        // Задача 23
        // Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
        // 3 -> 1, 8, 27
        // 5 -> 1, 8, 27, 64, 125
        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа принимает на вход целое число от 1 до " + 100 +
            " и выводит таблицу кубов чисел от 1 до введённого числа (включительно!)");
            while (true)
            {
                Console.Write("Введите число от 1 до " + 100 + ": ");

                string input = Console.ReadLine();

                if (!int.TryParse(input, out int number) || number < 1 || number > 100)
                {
                    Console.WriteLine("Вы ввели текст или невалидное число!");
                    continue;
                }

                printCubes(number);
                break;
            }
        }

        static void printCubes(int n)
        {
            Console.Write("Кубы чисел от 1 до " + n + " включительно: ");
            for (int i = 0; i < n;)
            {
                if (i == n - 1)
                {
                    Console.WriteLine(++i * i + ".");
                }
                else
                {
                    Console.Write(++i * i + ", ");
                }
            }
        }
    }
}