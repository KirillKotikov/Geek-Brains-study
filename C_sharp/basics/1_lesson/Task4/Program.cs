namespace Task4
{
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Данная программа определяет наибольшее целое число из трёх представелнных =)");
            Console.WriteLine("Введите первое целое число: ");
            int first = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите второе целое число: ");
            int second = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите третье целое число: ");
            int third = Convert.ToInt32(Console.ReadLine());
            int max = first > second ? first : second; 
            max = max > third ? max : third; 
            Console.WriteLine($"Наибольшее число : {max}");
        }
    }
}