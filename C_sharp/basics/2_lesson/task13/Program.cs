namespace second_lesson
{
    class Task13 {

        // Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
        // 645 -> 5
        // 78 -> третьей цифры нет
        // 32679 -> 6
        static void Main(string[] args) {
            Console.WriteLine("Данная программа выводит на экран третью цифру из введенного числа =)");
            while (true) {
                Console.Write("Введите число, состоящее не менее чем из 3-х цифр: ");
                string input = Console.ReadLine().ToString();
                if (!int.TryParse(input, out int number)) {
                    Console.WriteLine("Вы ввели не число!");  
                } else if (input.Length < 3) {
                    Console.WriteLine("Третьей цифры нет!");  
                } else {
                     Console.WriteLine("Третья цифра введенного числа = " + input[2]);  
                   break;   
                }
            }
            
        }
    }
}