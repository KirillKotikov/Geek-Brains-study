namespace second_lesson
{
    class Task10 {

        // Задача 10: Напишите программу, которая принимает на вход трёхзначное число 
        // и на выходе показывает вторую цифру этого числа.
        // 456 -> 5
        // 782 -> 8
        // 918 -> 1
        static void Main(string[] args) {
            Console.WriteLine("Данная программа выводит на экран вторую цифру из введенного числа =)");
            while (true) {
                Console.Write("Введите число, состоящее не менее чем из 2-ух цифр: ");
                string input = Console.ReadLine().ToString();
                if (!int.TryParse(input, out int number)) {
                    Console.WriteLine("Вы ввели не число!");  
                } else if (input.Length < 2) {
                    Console.WriteLine("Вы ввели число, состоящее менее чем из 2-ух цифр!");  
                } else {
                     Console.WriteLine("Вторая цифра введенного числа = " + input[1]);  
                   break;   
                }
            }
            
        }
    }
}