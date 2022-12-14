namespace Task4
{
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Данная программа определяет наибольшее целое число из двух представленных =)");
            Console.WriteLine("Введите первое целое число: ");
            int first = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите второе целое число: ");
            int second = Convert.ToInt32(Console.ReadLine());
            int max = first > second ? first : second; 
            Console.WriteLine($"Наибольшее число : {max}");
        }
    }
}