namespace second_lesson
{
    class Task13 {

        // Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
        // и проверяет, является ли этот день выходным.
        // 6 -> да
        // 7 -> да
        // 1 -> нет
        static void Main(string[] args) {
            Console.WriteLine("Данная программа определяет, является ли введённое число выходным днём в июле 2022 года");
            while (true) {
                Console.Write("Введите число от 1 по 31: ");
                string input = Console.ReadLine().ToString();
                if (!int.TryParse(input, out int number)) {
                    Console.WriteLine("Вы ввели не число!");
                    continue;  
                } 
                int num = int.Parse(input);
                if (num < 1 || num > 31 ) {
                    Console.WriteLine("Вы ввели число не от 1 по 31!");  
                } else {
                    if (num == 2 || num == 3 || num == 9 || num == 10 || num == 16 || 
                    num == 17 || num == 23 || num == 24 || num == 30 || num == 31) {
                        Console.WriteLine(num + " июля - выходной день!");  
                        break;   
                    }
                        Console.WriteLine(num + " июля - будний день!");    
                        break;   
                }
            }
            
        }
    }
}