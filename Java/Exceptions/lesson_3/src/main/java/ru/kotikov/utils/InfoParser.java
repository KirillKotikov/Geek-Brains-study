package ru.kotikov.utils;

import ru.kotikov.exceptions.DateValidException;
import ru.kotikov.exceptions.PhoneNumberValidException;
import ru.kotikov.exceptions.SexValidException;
import ru.kotikov.models.Contact;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class InfoParser {

    public static Contact parseInfo(String[] info) throws DateValidException, PhoneNumberValidException, SexValidException {
        String secondName = info[0];
        String firstName = info[1];
        String patronymic = info[2];

        DateFormat df = new SimpleDateFormat("dd.MM.yyyy");
        Date date = null;
        try {
            if (!info[3].matches("(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((19|20)\\d\\d)")) {
                throw new DateValidException();
            }
            date = df.parse(info[3]);
        } catch (ParseException | DateValidException e) {
            throw new DateValidException("Error! Input date = " + info[3] + " of birth is not valid.", e);
        }
        Calendar dateOfBirth = Calendar.getInstance();
        dateOfBirth.setTime(date);

        if (!info[4].matches("\\d{5,20}")) {
            throw new PhoneNumberValidException("Error! Input phone number = " + info[4] + " is not valid. " +
                    "It must contain only number from five to twenty!");
        }
        long phoneNumber = Long.parseLong(info[4]);

        if (!info[5].matches("f|m")) {
            throw new SexValidException("Error! Input sex = " + info[5] + " is not valid.");
        }
        String sex = info[5];

        return new Contact(firstName, secondName, patronymic, dateOfBirth, phoneNumber, sex);
    }
}
