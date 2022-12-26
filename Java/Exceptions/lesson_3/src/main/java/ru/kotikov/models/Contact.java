package ru.kotikov.models;

import lombok.*;

import java.text.SimpleDateFormat;
import java.util.Calendar;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Contact {

    private String firstName;
    private String secondName;
    private String patronymic;
    private Calendar dateOfBirth;
    private long phoneNumber;
    private String sex;

    @Override
    public String toString() {
        SimpleDateFormat format = new SimpleDateFormat("dd.MM.yyyy");
        return "<" + secondName + "><" + firstName + "><" + patronymic + "><" + format.format(dateOfBirth.getTime())
                + "><" + phoneNumber + "><" + sex + ">\n";
    }
}
