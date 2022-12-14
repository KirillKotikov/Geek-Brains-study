namespace third_lesson
{
    class Task19 {

        // Задача 19
        // Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
        // 14212 -> нет
        // 12821 -> да
        // 23432 -> да
        static void Main(string[] args) {

            Console.WriteLine("Данная программа определяет, является ли введённое число палиндромом :)");

            while (true) 
            {

                Console.Write("Введите число от 0 до " + int.MaxValue + ": ");
                string input = Console.ReadLine();
                Boolean result = true;

                if (!int.TryParse(input, out int number) || Convert.ToInt32(input) < 0) 
                {
                    Console.WriteLine("Вы ввели текст или невалидное число!");
                    continue;  
                } else if (input.Length < 2) 
                {
                    Console.WriteLine("Данное число не является палиндромом!");
                    break;
                }

                char[] numbersArray = input.ToArray(); 
                int length =  numbersArray.Length;
                
                for (int i = 0; i < length/2; i++) 
                {
                    if (!numbersArray[i].Equals(numbersArray[length - 1 - i])) 
                    {
                        result = false;
                        break;
                    }
                }
                if (result) 
                {
                    Console.WriteLine("Данное число является палиндромом!");
                } else 
                {
                    Console.WriteLine("Данное число не является палиндромом!");
                }
                break;
            }
        }
    }
}