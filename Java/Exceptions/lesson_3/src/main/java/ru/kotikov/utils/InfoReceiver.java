package ru.kotikov.utils;

import java.util.Scanner;

public class InfoReceiver {

    public static String getStringFromConsole() {
        Scanner scanner = new Scanner(System.in);
           return scanner.nextLine();
    }

}
