package ru.kotikov.services;

import ru.kotikov.models.Contact;

import java.io.FileWriter;
import java.io.IOException;

public class FileService {

    public static boolean writeFile(Contact contact) {

        try (FileWriter fileWriter = new FileWriter(contact.getSecondName(), true)) {
            fileWriter.write(contact.toString());
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }
}
