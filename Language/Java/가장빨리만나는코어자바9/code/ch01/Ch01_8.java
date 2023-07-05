package code.ch01;

import java.util.Scanner;

public class Ch01_8 {
    /**
     * 8. 문자열을 읽어서 비어 있지 않은 부분 문자열을 모두 출력하는 프로그램을 작성하라
     */
    public static String printString(String rawString) {
        return rawString.replace(" ", "");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String rawString = sc.next();
        System.out.println(printString(rawString));
    }
}
