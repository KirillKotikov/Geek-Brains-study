package ru.kotikov;

import ru.kotikov.exceptions.DateValidException;
import ru.kotikov.exceptions.PhoneNumberValidException;
import ru.kotikov.exceptions.SexValidException;
import ru.kotikov.models.Contact;
import ru.kotikov.services.FileService;
import ru.kotikov.utils.ErrorPrint;
import ru.kotikov.utils.InfoParser;
import ru.kotikov.utils.InfoReceiver;
import ru.kotikov.utils.InfoValidation;

public class Main {
    public static void main(String[] args) {

        while (true) {
            try {

                System.out.print("Введите данные контакта через пробел в следующем порядке Фамилия Имя Отчество дата_рождения номер_телефона пол.\n" +
                        "Форматы данных:\n" +
                        "\tфамилия, имя, отчество - строки\n" +
                        "\tдата_рождения - строка формата dd.mm.yyyy\n" +
                        "\tномер_телефона - целое беззнаковое число без форматирования\n" +
                        "\tпол - символ латиницей f или m.\n" +
                        "Строка ввода: ");
                String[] splitStringFromConsole = InfoReceiver.getStringFromConsole().split(" ");
                int checkInfo = InfoValidation.checkInfo(splitStringFromConsole);
                if (checkInfo != 0) {
                    System.out.println(ErrorPrint.errorString(checkInfo));
                    continue;
                } else {
                    Contact contact = InfoParser.parseInfo(splitStringFromConsole);
                    if(FileService.writeFile(contact)) {
                        System.out.println("Контакт успешно сохранён!");
                    }
                }
                break;
            } catch (DateValidException | PhoneNumberValidException | SexValidException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}