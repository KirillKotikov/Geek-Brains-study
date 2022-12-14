namespace Task8 {

    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Данная программа отображает все чётные числа от 1 до введённого числа (не включительно) =)");
            Console.WriteLine("Введите целое число означающее конец диапазона (до - не включительно): ");
            int end = Convert.ToInt32(Console.ReadLine());

            Console.Write($"Нечётные числа от 1 до {end}: ");
            for (int i = 2; i < end; i+=2) {
                Console.Write($"{i}, ");
            }
        }
    }
}