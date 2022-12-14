
namespace FinalCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа из имеющегося массива строк формирует " +
                "массив из строк, длина которых меньше либо равна 3 символа.");
            Console.WriteLine("Если вы хотите сами задать массив строк для программы, " +
                "то введите \"Да\", иначе введите \"Нет\"");
            string[] inputStringArray = GetStringArray();
            Console.WriteLine("Исходный массив: \n" +
            "[ " + string.Join(", ", inputStringArray) + " ]");
            string[] resultArray = FilterArrayByLength(inputStringArray, 3);
            Console.WriteLine("Результат: \n" +
            "[ " + string.Join(", ", resultArray) + " ]");

        }

        public static string[] GetStringArray()
        {
            string[] resultArray;
            while (true)
            {
                Console.Write("Введите ваш выбор: ");
                string? answer = Console.ReadLine();
                if (string.Equals(answer, "Да", StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Вы выбрали самостоятельный ввод строк во входной массив.");
                    int arrayLength;
                    while (true)
                    {
                        Console.Write("Введите количество строк в массиве от 1 до 10 (включительно): ");
                        string? size = Console.ReadLine();
                        if (int.TryParse(size, out int num) && num > 0 && num < 11)
                        {
                            arrayLength = num;
                            break;
                        }
                        Console.WriteLine("Вы ввели неправильное число или вовсе не число! Если хотите выйти из програмы " +
                        "нажмите вместе клавиши \"ctrl + c\".");
                    }
                    resultArray = new string[arrayLength];
                    for (int i = 0; i < arrayLength; i++)
                    {
                        Console.Write("Введите строку для массива №" + (i + 1) + ": ");
                        resultArray[i] = Console.ReadLine();
                    }
                    return resultArray;
                }
                else if (string.Equals(answer, "Нет", StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Вы выбрали использование массива заданного программой.");
                    return new string[]{
                    "hello", "2", "world", ";-)", "1234", "1567", "-2", "coumputer science"
                };
                }
                else
                {
                    Console.WriteLine("Вы ввели невалидный ответ! Введите \"Да\" или \"Нет\".");
                }
            }
        }

        public static string[] FilterArrayByLength(string[] inputArray, int length)
        {
            int outCount = 0;
            foreach (string input in inputArray)
            {
                if (input.Length <= length)
                {
                    outCount++;
                }
            }
            string[] outputArray = new string[outCount];
            outCount = 0;
            foreach (string input in inputArray)
            {
                if (input.Length <= length)
                {
                    outputArray[outCount] = input;
                    outCount++;
                }
            }
            return outputArray;
        }
    }
}

