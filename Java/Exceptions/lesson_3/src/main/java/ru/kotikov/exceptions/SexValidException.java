package ru.kotikov.exceptions;

public class SexValidException extends Exception{
    public SexValidException(String message) {
        super(message);
    }
    public SexValidException(String message, Exception exception) {
        super(message, exception);
    }
}
