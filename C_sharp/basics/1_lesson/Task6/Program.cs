namespace Task6
{
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Данная программа определяет является ли введённое число чётным =)");
            Console.WriteLine("Введите целое число: ");
            int number = Convert.ToInt32(Console.ReadLine());
            if (number % 2 == 0) {
                Console.WriteLine("Введённое число чётное!");    
            } else {
                Console.WriteLine("Введённое число нечётное!");    
            }
            
        }
    }
}