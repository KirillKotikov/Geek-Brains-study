В данном проекте выполненное домашнее задание по второму уроку:

- Task01:<br/>
Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. 
<br/>Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.
****
- Task02:<br/>
Если необходимо, исправьте данный код:
<br/>
`  try {`<br/>
`  int d = 0;`<br/>
`  double catchedRes1 = intArray[8] / d;`<br/>
`  System.out.println("catchedRes1 = " + catchedRes1);`<br/>
`  } catch (ArithmeticException e) {`<br/>
`  System.out.println("Catching exception: " + e);`<br/>
`  }`
****
- Task03:<br/>
Дан следующий код, исправьте его там, где требуется:<br/>
`  public static void main(String[] args) throws Exception {`<br/>
`  try {`<br/>
`  int a = 90;`<br/>
`  int b = 3;`<br/>
`  System.out.println(a / b);`<br/>
`  printSum(23, 234);`<br/>
`  int[] abc = { 1, 2 };`<br/>
`  abc[3] = 9;`<br/>
`  } catch (Throwable ex) {`<br/>
`  System.out.println("Что-то пошло не так...");`<br/>
`  } catch (NullPointerException ex) {`<br/>
`  System.out.println("Указатель не может указывать на null!");`<br/>
`  } catch (IndexOutOfBoundsException ex) {`<br/>
`  System.out.println("Массив выходит за пределы своего размера!");`<br/>
`  }`<br/>
`  }`<br/>
`  public static void printSum(Integer a, Integer b) throws FileNotFoundException {`<br/>
`  System.out.println(a + b);`<br/>
`  }`
****
- Task04:<br/>
Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
<br/>Пользователю должно показаться сообщение, что пустые строки вводить нельзя.