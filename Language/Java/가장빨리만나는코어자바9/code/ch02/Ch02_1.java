package code.ch02;

import java.time.LocalDate;

/**
 * 1. 달력 출력 프로그램을 수정해서 한 주가 일요일부터 시작하게 하라. 또 줄 넘김은 끝에 한 번만 출력하게 만들어라
 */
public class Ch02_1 {
    public static void printCal(int year, int month) {
        System.out.println(" Sun Mon Tue Wed Thu Fri Sat");

        LocalDate date = LocalDate.of(year, month, 1);
        // 첫 날짜 띄어쓰기
        for (int i=0; i<date.getDayOfWeek().getValue()%7; i++) {
            System.out.printf("    ");
        }

        while(date.getMonthValue() == month) {
            System.out.printf("%4d", date.getDayOfMonth());
            date = date.plusDays(1);

            if (date.getDayOfWeek().getValue() == 7) {
                System.out.println();
            }
        }
    }

    public static void main(String[] args){
        printCal(2023, 7);
    }
}
