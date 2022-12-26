package ru.kotikov.utils;

public class InfoValidation {

    public static int checkInfo(String[] strArray) {
        if (strArray.length < 6) return 1;
        if (strArray.length > 6) return 2;
//        if (!split[3].matches("(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((19|20)\\d\\d)")) return 3;
//        if (!split[4].matches("\\d{5,20}")) return 4;
//        if(split[5].length() != 1 || !split[5].matches("f|m")) return 5;
        return 0;
    }
}
