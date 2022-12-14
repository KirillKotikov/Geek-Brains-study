package GB_java_lessons.lesson_06;

import java.util.Date;

public class Simple {
    private Date date;
    private String comment;
    private int number;
    private double money;
    private String simpleName;

    Simple(Date date, String comment, int number, double money, String simpleName) {
        this.date = date;
        this.comment = comment;
        this.number = number;
        this.money = money;
        this.simpleName = simpleName;
    }

    public static SimpleBuilder builder() {
        return new SimpleBuilder();
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public void setMoney(double money) {
        this.money = money;
    }

    public void setSimpleName(String simpleName) {
        this.simpleName = simpleName;
    }

    public Date getDate() {
        return this.date;
    }

    public String getComment() {
        return this.comment;
    }

    public int getNumber() {
        return this.number;
    }

    public double getMoney() {
        return this.money;
    }

    public String getSimpleName() {
        return this.simpleName;
    }

    public String toString() {
        Date date = this.getDate();
        return "Simple(date=" + date + ", comment=" + this.getComment() + ", number=" + this.getNumber() + ", money=" + this.getMoney() + ", simpleName=" + this.getSimpleName() + ")";
    }

    public static class SimpleBuilder {
        private Date date;
        private String comment;
        private int number;
        private double money;
        private String simpleName;

        public SimpleBuilder date(Date date) {
            this.date = date;
            return this;
        }

        public SimpleBuilder comment(String comment) {
            this.comment = comment;
            return this;
        }

        public SimpleBuilder number(int number) {
            this.number = number;
            return this;
        }

        public SimpleBuilder money(double money) {
            this.money = money;
            return this;
        }

        public SimpleBuilder simpleName(String simpleName) {
            this.simpleName = simpleName;
            return this;
        }

        public Simple build() {
            return new Simple(this.date, this.comment, this.number, this.money, this.simpleName);
        }
    }
}

