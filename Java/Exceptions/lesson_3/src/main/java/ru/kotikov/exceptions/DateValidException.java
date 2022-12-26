package ru.kotikov.exceptions;

import lombok.NoArgsConstructor;

@NoArgsConstructor
public class DateValidException extends Exception{
    public DateValidException(String message) {
        super(message);
    }
    public DateValidException(String message, Exception exception) {
        super(message, exception);
    }
}
