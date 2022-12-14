using System.Text.RegularExpressions;

namespace eighth_lesson
{
    class Task62
    {

        // Дополнительная задача
        // Задача 62. Заполните спирально массив 4 на 4.
        // Например, на выходе получается вот такой массив:
        // 1 2 3 4
        // 12 13 14 5
        // 11 16 15 6
        // 10 9 8 7

        static void Main(string[] args)
        {
            int[,] array = new int[5, 6];
            FillTwoDimensionalArrayШтSpiral(array);
            PrintTwoDimensionalArray(array);

        }

        public static void FillTwoDimensionalArrayШтSpiral(int[,] array)
        {
            int number = 1;
            int maxCount = array.GetLength(0) * array.GetLength(1);
            int maxWidth = array.GetLength(1);
            int maxHight = array.GetLength(0);
            int hight = 0;
            int width = 0;
            for (int i = 0; i <= maxCount; i++)
            {

                if (array[hight, width] == 0)
                {
                    array[hight, width] = number;
                    number++;
                }
                else
                {
                    if (width + 1 < maxWidth && array[hight, width + 1] == 0)
                    {
                        if (hight - 1 > -1 && array[hight - 1, width] == 0)
                        {
                            hight--;
                            array[hight, width] = number;
                            number++;
                        }
                        else
                        {
                            width++;
                            array[hight, width] = number;
                            number++;
                        }
                    }

                    else if (hight + 1 < maxHight && array[hight + 1, width] == 0)
                    {
                        hight++;
                        array[hight, width] = number;
                        number++;
                    }
                    else if (width - 1 > -1 && array[hight, width - 1] == 0)
                    {
                        width--;
                        array[hight, width] = number;
                        number++;
                    }
                    else if (hight - 1 > -1 && array[hight - 1, width] == 0)
                    {
                        
                        {
                            hight--;
                            array[hight, width] = number;
                            number++;
                        }
                    }
                }
            }
        }

        public static void PrintTwoDimensionalArray(int[,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(array[i, j] + " ");
                }
                Console.WriteLine("");
            }
        }


    }
}