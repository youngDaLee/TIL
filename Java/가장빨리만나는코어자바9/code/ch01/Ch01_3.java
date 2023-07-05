package code.ch01;

import java.util.Scanner;

public class Ch01_3 {
    /**
     * 3. 조건연산자만 사용해 정수 세 개를 읽고 최댓값을 출력하는 프로그램을 작성해라. Math.max를 사용해 같은 프로그램을 작성해라
     */
    public static Integer maxOperator(Integer num1, Integer num2, Integer num3) {
        if (num1 >= num2 && num1 >= num3) {
            return num1;
        } else if (num2 >= num3) {
            return num2;
        } else {
            return num3;
        }
    }

    public static Integer maxMath(Integer num1, Integer num2, Integer num3) {
        return Math.max(Math.max(num1,num2), num3);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer num1 = sc.nextInt();
        Integer num2 = sc.nextInt();
        Integer num3 = sc.nextInt();

        System.out.println(maxOperator(num1, num2, num3));
        System.out.println(maxMath(num1, num2, num3));
    }
}
