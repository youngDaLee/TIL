package code.ch01;

import java.util.Scanner;

public class Ch01_7 {
    static String ADD = "+";
    static String SUB = "-";
    static String MUL = "*";
    static String QUOT = "/";
    static String REM = "%";
    /**
     * 7. 0~4294967295 사이의 정수 두 개를 읽어서 int변수에 저장한 후 부허 없는 합계,차이,곱,몫,나머지를 계산해 표시하는 프로그램을 작성하라(long사용 X)
     * 해결 실패 => unsinged int를 long형으로 저장하는 방법밖에 모르겠음...
     */
    public static String Calcualtor(String mark) {
        Scanner sc = new Scanner(System.in);
        String snum1 = sc.next();
        int num1 = Integer.parseInt(snum1);
        String snum2 = sc.next();
        int num2 = Integer.parseInt(snum2);

        int res = -1;
        if (mark==ADD) {
            res = num1 + num2;
        } else if (mark == SUB) {
            res = num1 - num2;
        } else if (mark == MUL) {
            res = num1 * num2;
        } else if (mark == QUOT) {
            res = num1 / num2;
        } else if (mark == REM) {
            res = num1 % num2;
        }

        String answer = Integer.toUnsignedString(res);
        return answer;
    }

    public static void main(String[]args) {
        System.out.println(Calcualtor("+"));
    }
}
