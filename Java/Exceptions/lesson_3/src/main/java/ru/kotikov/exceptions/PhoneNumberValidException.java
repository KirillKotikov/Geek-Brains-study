package ru.kotikov.exceptions;

public class PhoneNumberValidException extends Exception {

    public PhoneNumberValidException(String message) {
        super(message);
    }
    public PhoneNumberValidException(String message, Exception exception) {
        super(message, exception);
    }
}
