package GB_java_lessons.lesson_06;

import java.util.Date;

public class Main {
   public static void main(String[] args) {
    Simple simple = Simple.builder()
    .date(new Date())
    .money(258.22)
    .build();

    System.out.println(simple + "\n");

    simple = Simple.builder()
    .comment("some comment")
    .number(12345)
    .build();

    System.out.println(simple + "\n");

    simple = Simple.builder()
    .date(new Date())
    .comment("new ")
    .money(258852.33)
    .number(97421451)
    .simpleName("NAME")
    .build();

    System.out.println(simple + "\n");
   } 
}
