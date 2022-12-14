using System.Text.RegularExpressions;

namespace third_lesson
{
    class Task21
    {

        // Задача 21
        // Напишите программу, которая принимает на вход координаты двух точек 
        // и находит расстояние между ними в 3D пространстве.
        // A (3,6,8); B (2,1,-7) -> 15.84
        // A (7,-5, 0); B (1,-1,9) -> 11.53

        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа определяет расстояние между двумя координатами в 3D пространстве :)");
            while (true)
            {
                Console.WriteLine("Введите координаты двух точек числами от -99 до 99 (включительно).");
                Console.WriteLine("Шаблон ввода: \"A (-3,69,8); B (25,1,-7)\" (без кавычек!).");
                string input = Console.ReadLine();
                String pattern = @"^A\s\(\s?-?\d{1,2},\s?-?\d{1,2},\s?-?\d{1,2}\);\sB\s\(\s?-?\d{1,2},\s?-?\d{1,2},\s?-?\d{1,2}\)";
                if (!Regex.IsMatch(input, pattern, RegexOptions.IgnoreCase))
                {
                    Console.WriteLine("Координаты введены неверно!");
                    continue;
                }
                Regex regex = new Regex(@"\s?-?\d{1,2},\s?-?\d{1,2},\s?-?\d{1,2}");
                MatchCollection matches = regex.Matches(input);
                int x1 = 0, y1 = 0, z1 = 0, x2 = 0, y2 = 0, z2 = 0;
                if (matches.Count() == 2)
                {
                    for (int i = 0; i < matches.Count(); i++)
                    {
                        string[] numbers = matches[i].Value.Split(",");
                        if (i == 0)
                        {
                            x1 = Convert.ToInt32(numbers[0].Trim());
                            y1 = Convert.ToInt32(numbers[1].Trim());
                            z1 = Convert.ToInt32(numbers[2].Trim());
                        }
                        else
                        {
                            x2 = Convert.ToInt32(numbers[0].Trim());
                            y2 = Convert.ToInt32(numbers[1].Trim());
                            z2 = Convert.ToInt32(numbers[2].Trim());
                        }
                    }
                    double result = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2) + Math.Pow(z2 - z1, 2));
                    Console.WriteLine("Расстояние точек " + input + " в 3D пространстве = " + Math.Round(result, 2));
                    break;
                }
                else
                {
                    Console.WriteLine("Произошла ошибка! Невозможно считать координаты");
                    break;
                }
            }
        }
    }
}